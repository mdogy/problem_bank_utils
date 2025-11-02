"""
Unit tests for LaTeX generation functionality.
"""
import sys
import unittest
from pathlib import Path

# Add src directory to path so we can import modules
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from latex_utils import escape_latex, generate_question_latex


class TestLatexGeneration(unittest.TestCase):

    def test_escape_latex(self):
        """Test that all LaTeX special characters are properly escaped."""
        self.assertEqual(escape_latex("a & b"), r"a \& b")
        self.assertEqual(escape_latex("a % b"), r"a \% b")
        self.assertEqual(escape_latex("a $ b"), r"a \$ b")
        self.assertEqual(escape_latex("a # b"), r"a \# b")
        self.assertEqual(escape_latex("a _ b"), r"a \_ b")
        self.assertEqual(escape_latex("a { b"), r"a \{ b")
        self.assertEqual(escape_latex("a } b"), r"a \} b")
        self.assertEqual(escape_latex("statsmodels.na_viz"), r"statsmodels.na\_viz")
        self.assertEqual(escape_latex("~"), r"\textasciitilde{}")
        self.assertEqual(escape_latex("^"), r"\textasciicircum{}")
        self.assertEqual(escape_latex("\\"), r"\textbackslash{}")

    def test_generate_question_latex(self):
        """Test LaTeX generation for a question with standard content."""
        question = {
            "questionId": "M01-Q01",
            "questionType": "Multiple Choice",
            "questionText": "What is Data Science mainly about?",
            "topic": "M1a – What is Data Science?",
            "options": [
                {
                    "optionId": "M01-Q01-O1",
                    "text": "Using data to identify patterns and make informed decisions",
                    "isCorrect": True
                },
                {
                    "optionId": "M01-Q01-O2",
                    "text": "Creating as much data as possible",
                    "isCorrect": False
                }
            ],
            "metadata": {
                "difficulty": "Easy",
                "blooms": "Understand"
            }
        }

        expected_lines = [
            r"\begin{tabular}{|l|l|}",
            r"\hline",
            r"**Question ID:** & M01-Q01 \\ \hline",
            r"**Topic:** & M1a – What is Data Science? \\ \hline",
            r"**Difficulty:** & Easy \\ \hline",
            r"**Blooms:** & Understand \\ \hline",
            r"\end{tabular}",
            r"",
            r"\subsection*{What is Data Science mainly about?}",
            r"\begin{enumerate}",
            r"\item \textcolor{green}{Using data to identify patterns and make informed decisions}",
            r"\item Creating as much data as possible",
            r"\end{enumerate}"
        ]
        expected_latex = "\n".join(expected_lines)
        self.assertEqual(generate_question_latex(question), expected_latex)

    def test_generate_question_latex_with_special_characters(self):
        """Test LaTeX generation for a question with special characters that need escaping."""
        question = {
            "questionId": "M02-Q05",
            "questionType": "Multiple Choice",
            "questionText": "What package is used for statsmodels.na_viz?",
            "topic": "M2a – Data Visualization",
            "options": [
                {
                    "optionId": "M02-Q05-O1",
                    "text": "Use statsmodels.na_viz for visualization",
                    "isCorrect": True
                },
                {
                    "optionId": "M02-Q05-O2",
                    "text": "Use pandas.plot() with 50% accuracy",
                    "isCorrect": False
                },
                {
                    "optionId": "M02-Q05-O3",
                    "text": "Cost is $100 per license",
                    "isCorrect": False
                }
            ],
            "metadata": {
                "difficulty": "Medium",
                "blooms": "Apply"
            }
        }

        result = generate_question_latex(question)
        
        # Verify that special characters are properly escaped in the output
        self.assertIn(r"statsmodels.na\_viz", result)
        self.assertIn(r"50\%", result)
        self.assertIn(r"\$100", result)
        self.assertIn(r"\subsection*{What package is used for statsmodels.na\_viz?}", result)
        
        # Verify correct answer is highlighted
        self.assertIn(r"\textcolor{green}", result)

    def test_escape_latex_unicode_minus_sign(self):
        """Test that Unicode minus sign (U+2212) is handled properly for LaTeX."""
        # Unicode minus sign U+2212 (not regular hyphen -)
        unicode_minus = "\u2212"
        result = escape_latex(f"k{unicode_minus}1 dummies")
        
        # Should convert to regular hyphen or be LaTeX-safe
        # LaTeX can handle this with utf8 inputenc, but we should normalize to ASCII
        self.assertNotIn(unicode_minus, result)
        self.assertIn("-", result)  # Should contain regular hyphen

    def test_generate_question_latex_with_unicode_minus(self):
        """Test LaTeX generation with Unicode minus sign that caused pdflatex errors."""
        question = {
            "questionId": "M03-Q10",
            "questionType": "Multiple Choice",
            "questionText": "What is the correct approach?",
            "topic": "Regression",
            "options": [
                {
                    "optionId": "M03-Q10-O1",
                    "text": f"Dropping the intercept and using k\u22121 dummies and one interaction",
                    "isCorrect": True
                }
            ],
            "metadata": {
                "difficulty": "Medium",
                "blooms": "Apply"
            }
        }
        
        result = generate_question_latex(question)
        
        # Should not contain raw Unicode minus sign
        self.assertNotIn("\u2212", result)
        # Should contain escaped or normalized version
        self.assertIn("k-1", result)

    def test_escape_latex_unicode_arrow(self):
        """Test that Unicode arrow (U+2194 ↔) is handled properly for LaTeX."""
        unicode_arrow = "\u2194"  # LEFT RIGHT ARROW
        result = escape_latex(f"Calibration {unicode_arrow} Adjusted R²")
        
        # Should not contain raw Unicode arrow
        self.assertNotIn(unicode_arrow, result)
        # Should contain LaTeX-safe replacement (e.g., ↔ → \leftrightarrow or text representation)
        self.assertIn("Calibration", result)
        self.assertIn("Adjusted", result)

    def test_escape_latex_unicode_superscript(self):
        """Test that Unicode superscripts are converted to LaTeX superscript commands."""
        # Test various superscript characters
        superscript_2 = "\u00B2"  # ²
        superscript_3 = "\u00B3"  # ³
        superscript_1 = "\u00B9"  # ¹
        
        result_2 = escape_latex(f"R{superscript_2}")
        result_3 = escape_latex(f"R{superscript_3}")
        result_1 = escape_latex(f"R{superscript_1}")
        
        # Should contain LaTeX superscript commands
        self.assertIn(r"R$^{2}$", result_2)  # or \textsuperscript{2} or similar
        self.assertIn(r"R$^{3}$", result_3)
        self.assertIn(r"R$^{1}$", result_1)
        
        # Should not contain raw Unicode superscript
        self.assertNotIn(superscript_2, result_2)

    def test_escape_latex_unicode_mathematical_superscript(self):
        """Test that Unicode mathematical superscripts (like U+1D40 ᵀ) are converted."""
        # U+1D40 is MATHEMATICAL SCRIPT CAPITAL T (modifier letter)
        mathematical_superscript_T = "\u1D40"  # ᵀ
        result = escape_latex(f"w{mathematical_superscript_T}x")
        
        # Should not contain raw Unicode mathematical superscript
        self.assertNotIn(mathematical_superscript_T, result)
        # Should contain LaTeX-safe version (converted to regular T or superscript)
        self.assertIn("w", result)
        self.assertIn("x", result)

    def test_escape_latex_greek_letters(self):
        """Test that Greek letters (σ, μ, etc.) are converted to LaTeX commands."""
        # Common Greek letters that appear in math
        sigma = "\u03C3"  # σ (lowercase sigma)
        mu = "\u03BC"  # μ (lowercase mu)
        result_sigma = escape_latex(f"σ(z)=e^z")
        result_mu = escape_latex(f"mean μ and std σ")
        
        # Should not contain raw Greek letters
        self.assertNotIn(sigma, result_sigma)
        self.assertNotIn(mu, result_mu)
        
        # Should contain LaTeX Greek commands
        self.assertIn("sigma", result_sigma.lower())  # Either \sigma or $\\sigma$
        self.assertIn("mu", result_mu.lower())

    def test_escape_latex_mathematical_symbols(self):
        """Test that mathematical symbols (≥, ∑, ∫, etc.) are converted to LaTeX commands."""
        # Mathematical symbols found in acceptance test
        geq = "\u2265"  # ≥ (greater than or equal)
        summation = "\u2211"  # ∑ (summation)
        integral = "\u222B"  # ∫ (integral)
        
        result_geq = escape_latex(f"x {geq} 0")
        result_sum = escape_latex(f"{summation} x_i")
        result_int = escape_latex(f"{integral} f(x)dx")
        
        # Should not contain raw Unicode symbols
        self.assertNotIn(geq, result_geq)
        self.assertNotIn(summation, result_sum)
        self.assertNotIn(integral, result_int)
        
        # Should contain LaTeX commands
        self.assertTrue("geq" in result_geq.lower() or "ge" in result_geq.lower(), 
                       f"Expected 'geq' or 'ge' in result, got: {result_geq}")
        self.assertIn("sum", result_sum.lower())
        self.assertIn("int", result_int.lower())

    def test_generate_question_latex_with_unicode_arrow_and_superscript(self):
        """Test LaTeX generation with Unicode arrow and superscript that caused pdflatex errors."""
        question = {
            "questionId": "M04-Q20",
            "questionType": "Multiple Choice",
            "questionText": "What is the relationship?",
            "topic": "Statistics",
            "options": [
                {
                    "optionId": "M04-Q20-O1",
                    "text": f"Calibration \u2194 Adjusted R\u00B2",
                    "isCorrect": True
                }
            ],
            "metadata": {
                "difficulty": "Medium",
                "blooms": "Apply"
            }
        }
        
        result = generate_question_latex(question)
        
        # Should not contain raw Unicode characters
        self.assertNotIn("\u2194", result)  # arrow
        self.assertNotIn("\u00B2", result)  # superscript 2
        
        # Should contain LaTeX-safe versions
        self.assertIn("Calibration", result)
        self.assertIn("Adjusted", result)


if __name__ == '__main__':
    unittest.main()

