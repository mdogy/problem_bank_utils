import re
import csv
from pathlib import Path

def convert_md_to_brightspace_csv(md_filepath, csv_filepath):
    """
    Converts a markdown file with multiple-choice questions to a Brightspace-compatible CSV.
    """
    md_path = Path(md_filepath)
    if not md_path.exists():
        print(f"Error: Markdown file not found at {md_path}")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Split the content by questions. Each question starts with a number followed by a period.
    # We use a positive lookahead to keep the delimiter.
    questions_raw = re.split(r'\n(?=\d+\.)', md_content.strip())

    csv_rows = []

    for question_block in questions_raw:
        if not question_block.strip():
            continue

        lines = question_block.strip().split('\n')
        
        # First line is the question text
        question_text_line = lines[0]
        # Remove the initial number and period
        question_text = re.sub(r'^\d+\.\s*', '', question_text_line).strip()

        csv_rows.append(['NewQuestion', 'MC'])
        csv_rows.append(['QuestionText', question_text])

        # Subsequent lines are options
        option_lines = [line.strip() for line in lines[1:] if line.strip()]        
        for option_line in option_lines:
            is_correct = option_line.startswith('*')
            
            # Clean the option text
            # Remove the asterisk and the letter (e.g., "*a)" or "a)")
            option_text = re.sub(r'^\*?[a-z]\)\s*', '', option_line).strip()
            
            points = '100' if is_correct else '0'
            csv_rows.append(['Option', points, option_text])

    # Write to CSV file
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)
        
    print(f"Successfully converted {len(questions_raw)} questions to {csv_filepath}")

if __name__ == "__main__":
    md_file = "/mnt/e/City College Dropbox/Michael Grossberg/teaching/25Fall/problem_bank_utils/data/midtermMC2025.md"
    csv_file = "/mnt/e/City College Dropbox/Michael Grossberg/teaching/25Fall/problem_bank_utils/data/brightspace_upload.csv"
    convert_md_to_brightspace_csv(md_file, csv_file)
