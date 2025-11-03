"""
Acceptance test for full problem bank processing.

This test verifies that the entire question bank can be processed without errors.
It should be run to catch any Unicode or LaTeX compilation issues before deployment.
"""
import sys
import unittest
from pathlib import Path
import tempfile
import os
import subprocess
import shutil

# Add src directory to path so we can import modules
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from json_utils import read_json_file
from latex_utils import escape_latex, generate_latex_document, write_latex_file


class TestAcceptanceFullBank(unittest.TestCase):
    """Acceptance tests for full problem bank processing."""

    @classmethod
    def setUpClass(cls):
        """Set up test data - load the full question bank."""
        data_dir = Path(__file__).parent.parent / "data"
        question_bank_file = data_dir / "midterm_question_bank.json"
        
        if not question_bank_file.exists():
            cls.questions = None
            cls.skip_reason = f"Question bank file not found: {question_bank_file}"
        else:
            try:
                cls.questions = read_json_file(str(question_bank_file))
            except Exception as e:
                cls.questions = None
                cls.skip_reason = f"Failed to load question bank: {e}"

    def test_full_bank_escape_latex_no_errors(self):
        """Test that escape_latex processes all question text without errors."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        errors = []
        for i, question in enumerate(self.questions):
            try:
                # Test question text
                if 'questionText' in question:
                    escape_latex(question.get('questionText', ''))
                
                # Test topic
                if 'topic' in question:
                    escape_latex(question.get('topic', ''))
                
                # Test options
                for option in question.get('options', []):
                    escape_latex(option.get('text', ''))
                
                # Test metadata
                metadata = question.get('metadata', {})
                for key, value in metadata.items():
                    if isinstance(value, str):
                        escape_latex(value)
                        
            except Exception as e:
                errors.append(f"Question {i} (ID: {question.get('questionId', 'unknown')}): {e}")
        
        self.assertEqual(len(errors), 0, 
                        f"Found {len(errors)} errors in escape_latex:\n" + "\n".join(errors[:10]))

    def test_full_bank_generate_latex_no_errors(self):
        """Test that generate_latex_document processes all questions without errors."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        try:
            latex_content = generate_latex_document(self.questions)
            
            # Verify no raw Unicode problematic characters remain
            problematic_unicode = [
                '\u2194',  # LEFT RIGHT ARROW
                '\u00B2',  # Superscript 2
                '\u00B3',  # Superscript 3
                '\u2212',  # Minus sign
            ]
            
            found_unicode = []
            for char in problematic_unicode:
                if char in latex_content:
                    found_unicode.append(f"Unicode {ord(char):04X} ({repr(char)}) still present in output")
            
            self.assertEqual(len(found_unicode), 0,
                          f"Found unescaped Unicode characters:\n" + "\n".join(found_unicode))
            
            # Verify LaTeX structure is valid
            self.assertIn(r'\documentclass{article}', latex_content)
            self.assertIn(r'\begin{document}', latex_content)
            self.assertIn(r'\end{document}', latex_content)
            self.assertIn(r'\usepackage[utf8]{inputenc}', latex_content)
            
        except Exception as e:
            self.fail(f"Failed to generate LaTeX document: {e}")

    def test_full_bank_write_latex_file(self):
        """Test that write_latex_file successfully writes the entire question bank."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.tex', delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        try:
            write_latex_file(tmp_path, self.questions)
            
            # Verify file was created and has content
            self.assertTrue(Path(tmp_path).exists(), "LaTeX file was not created")
            
            file_size = Path(tmp_path).stat().st_size
            self.assertGreater(file_size, 0, "LaTeX file is empty")
            
            # Verify file can be read back
            with open(tmp_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertGreater(len(content), 1000, "LaTeX file content seems too short")
                
        finally:
            # Clean up
            if Path(tmp_path).exists():
                os.unlink(tmp_path)

    def test_full_bank_no_unicode_minus_sign(self):
        """Test that no Unicode minus signs (U+2212) remain in output."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        latex_content = generate_latex_document(self.questions)
        
        # Should not contain Unicode minus sign
        self.assertNotIn('\u2212', latex_content,
                        "Unicode minus sign (U+2212) found in LaTeX output - should be normalized to -")

    def test_full_bank_no_unicode_arrow(self):
        """Test that no Unicode arrows (U+2194) remain in output."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        latex_content = generate_latex_document(self.questions)
        
        # Should not contain Unicode arrow
        self.assertNotIn('\u2194', latex_content,
                        "Unicode arrow (U+2194) found in LaTeX output - should be converted to LaTeX command")

    def test_full_bank_no_unicode_superscript(self):
        """Test that no Unicode superscripts remain in output."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        latex_content = generate_latex_document(self.questions)
        
        # Should not contain Unicode superscripts (including mathematical ones)
        # Common superscripts: ¹²³⁴⁵⁶⁷⁸⁹⁰
        unicode_superscripts = ['\u00B2', '\u00B3', '\u00B9', '\u2070', '\u2074', '\u2075', 
                               '\u2076', '\u2077', '\u2078', '\u2079']
        # Mathematical superscripts (modifier letters): U+1D40 onwards
        # Check for any character in the mathematical superscript range
        found_superscripts = []
        for char in unicode_superscripts:
            if char in latex_content:
                found_superscripts.append(f"Unicode superscript {ord(char):04X} ({repr(char)}) found")
        
        # Check for mathematical superscript characters (U+1D40-U+1D7F, U+2070-U+209F)
        for codepoint in range(0x1D40, 0x1D7F + 1):
            char = chr(codepoint)
            if char in latex_content:
                found_superscripts.append(f"Unicode mathematical superscript {codepoint:04X} ({repr(char)}) found")
        
        # Also check U+2090-U+209F range (subscripts that might appear)
        for codepoint in range(0x2090, 0x209F + 1):
            char = chr(codepoint)
            if char in latex_content:
                found_superscripts.append(f"Unicode subscript {codepoint:04X} ({repr(char)}) found")
        
        self.assertEqual(len(found_superscripts), 0,
                        f"Found Unicode superscripts/subscripts in output:\n" + "\n".join(found_superscripts[:20]))

    def test_full_bank_pdflatex_compilation(self):
        """Test that the generated LaTeX file can be compiled with pdflatex via subprocess."""
        if self.questions is None:
            self.skipTest(self.skip_reason)
        
        # Check if pdflatex is available
        if not shutil.which('pdflatex'):
            self.skipTest("pdflatex not found - skipping compilation test")
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tex_file = Path(tmpdir) / "test_full_bank.tex"
            
            # Generate LaTeX file
            write_latex_file(str(tex_file), self.questions)
            
            # Verify file exists and has content
            self.assertTrue(tex_file.exists(), "LaTeX file was not created")
            self.assertGreater(tex_file.stat().st_size, 0, "LaTeX file is empty")
            
            # Change to temp directory for pdflatex
            original_dir = os.getcwd()
            try:
                os.chdir(tmpdir)
                
                # Run pdflatex (non-interactive mode, don't stop on errors)
                # Run twice (first pass for references, second for final output)
                result1 = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', tex_file.name],
                    capture_output=True,
                    text=True,
                    timeout=180
                )
                
                result2 = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', tex_file.name],
                    capture_output=True,
                    text=True,
                    timeout=180
                )
                
                # Combine output from both runs - pdflatex writes errors to stdout, not stderr
                combined_stdout = result1.stdout + result2.stdout
                combined_stderr = result1.stderr + result2.stderr
                combined_output = combined_stdout + combined_stderr
                
                # Check for Unicode character errors in combined output
                # pdflatex errors typically appear as:
                # ! Package inputenc Error: Unicode character X (U+XXXX)
                unicode_errors = []
                for line in combined_output.split('\n'):
                    line_lower = line.lower()
                    if ('unicode character' in line_lower or 
                        'inputenc error' in line_lower or 
                        'package inputenc error' in line_lower or
                        ('inputenc' in line_lower and 'error' in line_lower)):
                        unicode_errors.append(line.strip())
                
                # Check return codes - non-zero usually means compilation failure
                if result2.returncode != 0 or unicode_errors:
                    if unicode_errors:
                        # Extract Unicode character codes from error messages
                        char_codes = []
                        import re
                        for error in unicode_errors:
                            if 'U+' in error:
                                codes = re.findall(r'U\+([0-9A-F]+)', error, re.IGNORECASE)
                                char_codes.extend(codes)
                        
                        error_msg = (f"pdflatex compilation failed with Unicode errors:\n" + 
                                    "\n".join(unicode_errors[:15]) +
                                    (f"\n\nFound Unicode character codes: {', '.join(sorted(set(char_codes)))}" if char_codes else "") +
                                    f"\n\nReturn code: {result2.returncode}")
                        self.fail(error_msg)
                    elif result2.returncode != 0:
                        # Compilation failed but no Unicode errors found - show output
                        error_lines = [line for line in combined_stdout.split('\n') 
                                     if '!' in line[:5] or 'Error' in line or 'Fatal' in line]
                        self.fail(f"pdflatex compilation failed (return code: {result2.returncode}) but no Unicode errors detected:\n" +
                                "\n".join(error_lines[:25]) +
                                f"\n\nFull stdout (last 50 lines):\n" +
                                "\n".join(combined_stdout.split('\n')[-50:]))
                
                # Check if PDF was created
                pdf_file = tex_file.with_suffix('.pdf')
                if not pdf_file.exists():
                    # PDF wasn't created - compilation failed
                    # Show last 20 lines of output for debugging
                    output_lines = combined_output.split('\n')
                    last_output = "\n".join(output_lines[-20:])
                    self.fail(f"pdflatex compilation failed - PDF not created.\n"
                            f"Return code: {result2.returncode}\n"
                            f"Last output:\n{last_output}")
                
                # PDF was created - verify it has content
                self.assertGreater(pdf_file.stat().st_size, 0, 
                                 "PDF file was created but is empty")
                    
            finally:
                os.chdir(original_dir)

    def test_generate_exam_sample_with_pdf_flag(self):
        """Test that src/generate_exam_sample.py with --pdf flag runs successfully and generates PDF."""
        if self.questions is None:
            self.skipTest(self.skip_reason)

        # Check if pdflatex is available, as the script will use it
        if not shutil.which('pdflatex'):
            self.skipTest("pdflatex not found - skipping test for --pdf flag")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_base_name = "generated_exam"
            output_tex_path = Path(tmpdir) / f"{output_base_name}.tex"
            output_pdf_path = Path(tmpdir) / f"{output_base_name}.pdf"
            output_log_path = Path(tmpdir) / f"{output_base_name}.log"
            output_aux_path = Path(tmpdir) / f"{output_base_name}.aux"

            # Path to the main script
            script_path = Path(__file__).parent.parent / "src" / "generate_exam_sample.py"
            input_file_path = Path(__file__).parent.parent / "data" / "midterm_question_bank.json"

            # Construct the command to run the script with --pdf flag
            command = [
                sys.executable, # Use the same python interpreter that is running the tests
                str(script_path),
                str(input_file_path), # Add input_file as a positional argument
                str(output_tex_path), # Add output_file as a positional argument
                "--pdf"
            ]

            print(f"Running command: {' '.join(command)}") # For debugging in case of failure

            # Execute the script
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=300 # Increased timeout for full generation and compilation
            )

            # Assert that the script ran successfully
            self.assertEqual(result.returncode, 0,
                             f"Script generate_exam_sample.py failed with return code {result.returncode}.\n"
                             f"Stdout:\n{result.stdout}\nStderr:\n{result.stderr}")

            # Verify that the .tex file was created
            self.assertTrue(output_tex_path.exists(), f"LaTeX file {output_tex_path} was not created.")
            self.assertGreater(output_tex_path.stat().st_size, 0, f"LaTeX file {output_tex_path} is empty.")

            # Verify that the .pdf file was created
            self.assertTrue(output_pdf_path.exists(), f"PDF file {output_pdf_path} was not created.")
            self.assertGreater(output_pdf_path.stat().st_size, 0, f"PDF file {output_pdf_path} is empty.")

            # Verify that auxiliary files were created (optional but good for completeness)
            self.assertTrue(output_log_path.exists(), f"Log file {output_log_path} was not created.")
            self.assertTrue(output_aux_path.exists(), f"Aux file {output_aux_path} was not created.")

            # Check for common LaTeX compilation errors in stdout/stderr
            # The script itself should ideally catch and report these, but this is a safeguard
            combined_output = result.stdout + result.stderr
            latex_errors = [line for line in combined_output.splitlines() if "!" in line.strip() or "error" in line.lower()]
            self.assertEqual(len(latex_errors), 0,
                             f"LaTeX compilation errors detected in script output:\n" + "\n".join(latex_errors[:10]))


if __name__ == '__main__':
    unittest.main()

