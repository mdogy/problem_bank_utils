# Problem Bank Utilities

Python utilities for working with exam question banks, quizzes, and homework questions. This project provides tools to process, consolidate, and generate LaTeX-formatted exam documents from JSON question banks.

## Project Structure

```
problem_bank_utils/
├── data/                    # Question bank data files
│   └── midterm_question_bank.json
├── src/                     # Source code modules
│   ├── generate_exam_sample.py  # Main script: Generate LaTeX from JSON
│   ├── process_exams.py         # Main script: Consolidate exam files
│   ├── json_utils.py             # JSON file operations
│   ├── latex_utils.py            # LaTeX generation utilities
│   └── general_utils.py          # General utility functions
├── test/                    # Unit tests
│   └── test_generate_exam_sample.py
└── README.md               # This file
```

## Features

- **Question Bank Processing**: Consolidate questions from multiple JSON and Markdown files
- **LaTeX Generation**: Generate well-formatted LaTeX PDFs for exam question selection
- **Question Metadata**: Display question ID, topic, difficulty, and Bloom's taxonomy level
- **Answer Highlighting**: Automatically highlight correct answers in green
- **Deduplication**: Remove duplicate questions when consolidating files

## Requirements

- Python 3.6+
- pdflatex (for compiling generated LaTeX files)

## Usage

### Generating LaTeX Documents from Question Banks

The `generate_exam_sample.py` script generates LaTeX files from JSON question banks.

#### Basic Usage

Generate a sample of 10 questions (default) for formatting approval:

```bash
python src/generate_exam_sample.py data/midterm_question_bank.json output.tex
```

Generate all questions:

```bash
python src/generate_exam_sample.py data/midterm_question_bank.json output.tex --limit 0
```

Generate a specific number of questions:

```bash
python src/generate_exam_sample.py data/midterm_question_bank.json output.tex --limit 25
```

#### Command-Line Options

- `input_file`: Path to the input JSON file containing questions (required)
- `output_file`: Path to the output LaTeX file (required)
- `--limit N`: Number of questions to include (default: 10). Use `0` to include all questions
- `--loglevel LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO
- `--pdf`: Automatically compile the LaTeX file to PDF using pdflatex (requires pdflatex to be installed)

#### Compiling LaTeX to PDF

**Option 1: Automatic compilation (recommended)**

Use the `--pdf` flag to automatically compile the LaTeX file:

```bash
python src/generate_exam_sample.py data/midterm_question_bank.json output.tex --pdf
```

This will generate the LaTeX file and automatically compile it to PDF using pdflatex.

**Option 2: Manual compilation**

After generating the LaTeX file, compile it manually:

```bash
pdflatex output.tex
```

### Processing and Consolidating Exam Files

The `process_exams.py` script consolidates questions from multiple markdown and JSON files.

#### Usage

Edit the `exam_dir` variable in `process_exams.py` to point to your exam files directory, then run:

```bash
python src/process_exams.py
```

This script will:
1. Extract JSON questions from markdown files containing JSON code blocks
2. Load questions from existing JSON files
3. Deduplicate questions based on content
4. Save the consolidated question bank to `midterm_question_bank.json`

#### Supported File Formats

**Markdown Files** (JSON in code blocks):
- `m01_30_mcq.md`
- `M03_question_bank.md`
- `M04_question_bank.md`
- `M05_ENGR10200_All_MCQ_TestBank.md`
- `M06_question_bank.md`
- `M07_question_bank.md`
- `midterm_exam_questions.md`

**JSON Files**:
- `M04_Master_QuestionBank.json`
- `midterm_question_bank.json`

## Utility Modules

### `json_utils.py`

Functions for JSON file operations:

- `read_json_file(filepath, logger=None)`: Read and parse JSON files with error handling
- `write_json_file(filepath, data, indent=4, logger=None)`: Write data to JSON files
- `extract_json_from_markdown(md_content)`: Extract JSON from markdown code blocks

### `latex_utils.py`

Functions for LaTeX generation:

- `escape_latex(text)`: Escapes all LaTeX special characters (`&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^`, and backslash) to prevent compilation errors. Also normalizes Unicode characters:
  - U+2212 MINUS SIGN → regular hyphen
  - U+2194 LEFT RIGHT ARROW → `$\leftrightarrow$`
  - Unicode superscripts (², ³, etc.) → `$^{2}$`, `$^{3}$`, etc.
  - Critical for handling text with underscores (e.g., `statsmodels.na_viz`), dollar signs, Unicode characters, and other special characters.
- `generate_question_latex(question)`: Generate LaTeX for a single question
- `generate_latex_document(questions, question_separator)`: Generate complete LaTeX document
- `write_latex_file(filepath, questions, question_separator)`: Write LaTeX document to file

### `general_utils.py`

General utility functions:

- `make_hashable(obj)`: Convert nested structures to hashable form
- `deduplicate_items(items)`: Remove duplicates from a list

## Question JSON Format

Questions should follow this structure:

```json
{
    "questionId": "M01-Q01",
    "questionType": "Multiple Choice",
    "questionText": "What is Data Science mainly about?",
    "topic": "M1a – What is Data Science?",
    "options": [
        {
            "optionId": "M01-Q01-O1",
            "text": "Using data to identify patterns and make informed decisions",
            "isCorrect": true
        },
        {
            "optionId": "M01-Q01-O2",
            "text": "Creating as much data as possible",
            "isCorrect": false
        }
    ],
    "metadata": {
        "difficulty": "Easy",
        "blooms": "Understand"
    }
}
```

## Testing

Run all tests from the project root:

```bash
python -m unittest discover test -v
```

Or run a specific test file:

```bash
python -m unittest test.test_generate_exam_sample -v
```

### Acceptance Tests

**Important**: Before deploying or generating the full problem bank, run the acceptance tests:

```bash
python test/test_acceptance_full_bank.py
```

These tests verify that:
- The entire question bank can be processed without errors
- All Unicode characters are properly converted (arrows, superscripts, minus signs)
- The generated LaTeX document is valid
- No problematic Unicode characters remain in the output

This acceptance test should **always pass** before generating PDFs for the full question bank.

## Output Format

The generated LaTeX documents include:

1. **Metadata Table**: Question ID, Topic, Difficulty, and Bloom's taxonomy level
2. **Question Text**: Formatted as a subsection
3. **Multiple Choice Options**: Numbered list with correct answers highlighted in green
4. **Spacing**: Questions separated with vertical space for readability

All special characters in question text, options, and metadata are automatically escaped to ensure LaTeX compilation succeeds. This includes underscores (common in package names like `statsmodels.na_viz`), dollar signs, percent signs, and other LaTeX special characters.

## Logging

Both scripts generate log files:

- `generate_exam_sample.log`: Logs from the LaTeX generation script

Log levels can be configured via command-line arguments.

## License

This project is for internal academic use.
