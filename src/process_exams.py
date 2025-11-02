"""
Processes exam question files to consolidate them into a single JSON file.

This script extracts JSON data from markdown files and combines it with data from
existing JSON files within a specified directory. It then deduplicates the
questions and saves the result to a file named 'midterm_question_bank.json'.

The script is designed to be run from the command line and takes the directory
containing the exam files as an argument.

Usage:
    python process_exams.py
"""
import json
import os
import re

def make_hashable(obj):
    """
    Recursively converts a dictionary or list to a hashable equivalent.
    """
    if isinstance(obj, dict):
        return frozenset((k, make_hashable(v)) for k, v in sorted(obj.items()))
    if isinstance(obj, list):
        return tuple(make_hashable(e) for e in obj)
    return obj

def extract_json_from_markdown(md_content):
    """Extracts JSON content from markdown code blocks."""
    json_blocks = re.findall(r'''```json
(.*?)
```''', md_content, re.DOTALL)
    all_questions = []
    for block in json_blocks:
        try:
            data = json.loads(block)
            if isinstance(data, list):
                all_questions.extend(data)
            else:
                all_questions.append(data)
        except json.JSONDecodeError:
            # Ignore blocks that are not valid JSON
            pass
    return all_questions

def process_exam_files(directory):
    """
    Processes all exam files in a directory to consolidate questions.
    """
    markdown_files = [
        "m01_30_mcq.md",
        "M03_question_bank.md",
        "M04_question_bank.md",
        "M05_ENGR10200_All_MCQ_TestBank.md",
        "M06_question_bank.md",
        "M07_question_bank.md",
        "midterm_exam_questions.md",
    ]
    json_files = [
        "M04_Master_QuestionBank.json",
        "midterm_question_bank.json",
    ]
    
    all_questions = []
    
    # Process markdown files
    for filename in markdown_files:
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                all_questions.extend(extract_json_from_markdown(content))

    # Process JSON files
    for filename in json_files:
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_questions.extend(data)
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass # Ignore empty or invalid JSON files

    # Deduplicate questions
    unique_questions = {}
    for question in all_questions:
        hashable_question = make_hashable(question)
        if hashable_question not in unique_questions:
            unique_questions[hashable_question] = question
            
    final_questions = list(unique_questions.values())

    # Write the result to the output file
    output_filepath = os.path.join(directory, "midterm_question_bank.json")
    with open(output_filepath, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, indent=4)

    return len(final_questions)

if __name__ == "__main__":
    exam_dir = "/mnt/e/City College Dropbox/Michael Grossberg/teaching/25Fall/DSEI10200F25/exams"
    num_questions = process_exam_files(exam_dir)
    print(f"Processed and combined all questions. Total unique questions: {num_questions}")