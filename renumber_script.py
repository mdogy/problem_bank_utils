import re
from pathlib import Path

def renumber_markdown_questions(filepath):
    """
    Renumber questions in a Markdown file sequentially.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        print(f"Error: File not found at {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    renumbered_lines = []
    question_counter = 1
    
    # Regex to find lines starting with a number followed by a period and a space
    # This identifies the start of a question
    question_start_pattern = re.compile(r"^\d+\.\s")

    for line in lines:
        if question_start_pattern.match(line):
            # Replace the old number with the new sequential number
            renumbered_line = re.sub(r"^\d+\.", f"{question_counter}.", line, 1)
            renumbered_lines.append(renumbered_line)
            question_counter += 1
        else:
            renumbered_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(renumbered_lines)
    
    print(f"Successfully renumbered questions in {filepath}. Total questions: {question_counter - 1}")

if __name__ == "__main__":
    markdown_file = "/mnt/e/City College Dropbox/Michael Grossberg/teaching/25Fall/problem_bank_utils/data/midtermMC2025.md"
    renumber_markdown_questions(markdown_file)
