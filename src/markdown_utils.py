"""
Utility functions for Markdown generation.
"""

import string

def generate_question_markdown(question, question_number):
    """
    Generates the Markdown for a single question.
    
    Args:
        question: Dictionary containing question data
        question_number: The number of the question in the list
        
    Returns:
        String containing Markdown-formatted question
    """
    lines = []

    # Question text
    question_text = question.get('questionText', '').replace('\n', ' ') # Ensure no newlines in question text
    lines.append(f"{question_number}. {question_text}")
    lines.append("") # Blank line after question

    # Options
    if question.get("questionType") == "Multiple Choice":
        options = question.get("options", [])
        for i, option in enumerate(options):
            letter = string.ascii_lowercase[i]
            text = option.get("text", "")
            
            # Mark the correct answer with an asterisk
            if option.get("isCorrect"):
                lines.append(f"    *{letter}) {text}")
            else:
                lines.append(f"    {letter}) {text}")

    return "\n".join(lines)

def generate_markdown_document(questions):
    """
    Generates a complete Markdown document from a list of questions.
    
    Args:
        questions: List of question dictionaries
        
    Returns:
        String containing complete Markdown document
    """
    markdown_body = []
    for i, question in enumerate(questions):
        markdown_body.append(generate_question_markdown(question, i + 1))
    
    return "\n\n".join(markdown_body)

def write_markdown_file(filepath, questions):
    """
    Writes a Markdown document to a file.
    
    Args:
        filepath: Path to output Markdown file
        questions: List of question dictionaries
    """
    markdown_content = generate_markdown_document(questions)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)
