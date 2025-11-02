"""
Generates a LaTeX file from a JSON file of questions.

This script takes a JSON file containing a list of questions and generates a
LaTeX file that formats the questions for an exam. The script can be configured
to select a sample of questions and to set the logging level.

Usage:
    python generate_exam_sample.py <input_file> <output_file> [--limit <num_questions>] [--loglevel <level>]
"""

import argparse
import json
import logging

from latex_utils import escape_latex


def generate_question_latex(question):
    """Generates the LaTeX for a single question."""
    lines = []

    # Metadata
    lines.append("\begin{tabular}{|l|l|}")
    lines.append("\hline")
    lines.append(f"**Question ID:** & {escape_latex(question.get('questionId', 'N/A'))} \\ \hline")
    lines.append(f"**Topic:** & {escape_latex(question.get('topic', 'N/A'))} \\ \hline")
    lines.append(f"**Difficulty:** & {escape_latex(question.get('metadata', {}).get('difficulty', 'N/A'))} \\ \hline")
    lines.append(f"**Blooms:** & {escape_latex(question.get('metadata', {}).get('blooms', 'N/A'))} \\ \hline")
    lines.append("\end{tabular}")
    lines.append("\n")

    # Question text
    lines.append(f"\\subsection*{{{escape_latex(question.get('questionText', ''))}}}")

    # Options
    if question.get("questionType") == "Multiple Choice":
        lines.append("\begin{enumerate}")
        for option in question.get("options", []):
            text = escape_latex(option.get("text", ""))
            if option.get("isCorrect"):
                lines.append(f"\\item \\textcolor{{green}}{{{text}}}")
            else:
                lines.append(f"\\item {text}")
        lines.append("\end{enumerate}")

    return "\n".join(lines)


def main():
    """Main function to generate the LaTeX file."""
    parser = argparse.ArgumentParser(description="Generate a LaTeX file from a JSON file of questions.")
    parser.add_argument("input_file", help="The input JSON file.")
    parser.add_argument("output_file", help="The output LaTeX file.")
    parser.add_argument("--limit", type=int, help="The number of questions to include in the sample.")
    parser.add_argument("--loglevel", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="The logging level.")
    args = parser.parse_args()

    logging.basicConfig(filename="generate_exam_sample.log", level=args.loglevel, filemode='w')

    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            questions = json.load(f)
    except FileNotFoundError:
        logging.error(f"Input file not found: {args.input_file}")
        return
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in input file: {args.input_file}")
        return

    if args.limit:
        questions = questions[:args.limit]

    latex_preamble = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{xcolor}
\usepackage{enumitem}

\begin{document}
"""

    latex_postamble = r"""
\end{document}
"""

    latex_body = ""
    for question in questions:
        latex_body += generate_question_latex(question)
        latex_body += "\\vspace{1cm}\n\n"

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(latex_preamble + latex_body + latex_postamble)

    logging.info(f"Successfully generated {args.output_file} with {len(questions)} questions.")


if __name__ == "__main__":
    main()