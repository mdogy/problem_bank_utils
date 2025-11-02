import unittest
from generate_exam_sample import generate_question_latex
from latex_utils import escape_latex

class TestLatexGeneration(unittest.TestCase):

    def test_escape_latex(self):
        self.assertEqual(escape_latex("a & b"), r"a \& b")
        self.assertEqual(escape_latex("a % b"), r"a \% b")
        self.assertEqual(escape_latex("a $ b"), r"a $")
        self.assertEqual(escape_latex("a # b"), r"a # b")
        self.assertEqual(escape_latex("a _ b"), r"a _ b")
        self.assertEqual(escape_latex("a { b"), r"a { b")
        self.assertEqual(escape_latex("a } b"), r"a } b")

    def test_generate_question_latex(self):
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
            r"\item \\textcolor{green}{Using data to identify patterns and make informed decisions}",
            r"\item Creating as much data as possible",
            r"\end{enumerate}"
        ]
        expected_latex = "\n".join(expected_lines)
        self.assertEqual(generate_question_latex(question), expected_latex)

if __name__ == '__main__':
    unittest.main()
