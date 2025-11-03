"""
Generates a LaTeX file from a JSON file of questions.

This script takes a JSON file containing a list of questions and generates a
LaTeX file that formats the questions for an exam. The script can be configured
to select a sample of questions and to set the logging level. Optionally, it can
compile the LaTeX to PDF using pdflatex.

Usage:
    python generate_exam_sample.py <input_file> <output_file> [--limit <num_questions>] [--loglevel <level>] [--pdf]
"""

import argparse
import json
import logging
import subprocess
import sys
from pathlib import Path

from json_utils import read_json_file
from latex_utils import write_latex_file


def compile_pdf(tex_file, logger=None):
    """
    Compiles a LaTeX file to PDF using pdflatex.
    
    Args:
        tex_file: Path to the LaTeX .tex file
        logger: Optional logger instance
        
    Returns:
        True if compilation succeeded, False otherwise
    """
    tex_path = Path(tex_file)
    if not tex_path.exists():
        error_msg = f"LaTeX file not found: {tex_file}"
        if logger:
            logger.error(error_msg)
        print(error_msg)
        return False
    
    # Change to the directory containing the tex file so auxiliary files are created there
    work_dir = tex_path.parent
    tex_name = tex_path.name
    
    try:
        # Run pdflatex twice (first pass for references, second for final output)
        # Use -interaction=nonstopmode to prevent hanging on errors
        result1 = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_name],
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        result2 = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_name],
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        pdf_file = tex_path.with_suffix('.pdf')
        
        if pdf_file.exists() and result2.returncode == 0:
            success_msg = f"Successfully compiled {pdf_file}"
            if logger:
                logger.info(success_msg)
            print(success_msg)
            return True
        else:
            error_msg = f"PDF compilation failed. Check pdflatex output: {result2.stderr[:500]}"
            if logger:
                logger.error(error_msg)
                logger.debug(f"pdflatex stdout: {result2.stdout}")
            print(error_msg)
            return False
            
    except subprocess.TimeoutExpired:
        error_msg = "PDF compilation timed out after 60 seconds"
        if logger:
            logger.error(error_msg)
        print(error_msg)
        return False
    except FileNotFoundError:
        error_msg = "pdflatex not found. Please install TeX Live or MiKTeX."
        if logger:
            logger.error(error_msg)
        print(error_msg)
        return False
    except Exception as e:
        error_msg = f"Error during PDF compilation: {str(e)}"
        if logger:
            logger.error(error_msg)
        print(error_msg)
        return False


def main():
    """Main function to generate the LaTeX file."""
    parser = argparse.ArgumentParser(description="Generate a LaTeX file from a JSON file of questions.")
    parser.add_argument("input_file", help="The input JSON file.")
    parser.add_argument("output_file", help="The output LaTeX file.")
    parser.add_argument("--limit", type=int, default=10, help="The number of questions to include in the sample (default: 10 for approval). Use --limit 0 to include all questions.")
    parser.add_argument("--loglevel", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="The logging level.")
    parser.add_argument("--pdf", action="store_true", help="Compile the LaTeX file to PDF using pdflatex.")
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(filename="generate_exam_sample.log", level=args.loglevel, filemode='w')
    logger = logging.getLogger(__name__)

    # Read JSON file
    try:
        questions = read_json_file(args.input_file, logger=logger)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(str(e))
        sys.exit(1)

    # Handle pandas-style JSON format {col: {idx: val}}
    if isinstance(questions, dict) and 'questionId' in questions:
        reformatted_questions = []
        # Get the indices from one of the columns (e.g., questionId)
        indices = list(questions['questionId'].keys())
        for index in indices:
            question_obj = {}
            for key, values in questions.items():
                if index in values:
                    question_obj[key] = values[index]
            reformatted_questions.append(question_obj)
        questions = reformatted_questions

    # Limit questions if requested
    if args.limit and args.limit > 0:
        questions = questions[:args.limit]

    # Generate and write LaTeX file
    write_latex_file(args.output_file, questions)
    logger.info(f"Successfully generated {args.output_file} with {len(questions)} questions.")
    
    # Compile to PDF if requested
    if args.pdf:
        compile_pdf(args.output_file, logger=logger)


if __name__ == "__main__":
    main()