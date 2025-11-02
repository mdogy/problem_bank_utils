# Gemini Project Guidelines

This document provides instructions for the Gemini agent working on this project. Adherence to these guidelines is mandatory.

## 1. Project Goal

The primary goal of this project is to generate well-formatted LaTeX PDFs from a JSON question bank located at `data/midterm_question_bank.json`. The main script for this is `src/generate_exam_sample.py`.

## 2. Core Development Workflow: Test-Driven Development (TDD)

This project strictly follows a Test-Driven Development (TDD) workflow for all changes, including bug fixes and new features.

**You MUST follow these steps for every code modification:**

1.  **Write a Failing Test:** Before writing any implementation code, create a new test case in the appropriate file under the `test/` directory that reproduces the bug or specifies the new feature.
2.  **Confirm Failure:** Run the test suite and confirm that the new test fails as expected.
3.  **Implement the Fix/Feature:** Write or modify the application code (primarily in the `src/` directory) only to the extent necessary to make the new test pass.
4.  **Verify All Tests Pass:** Run the entire test suite to ensure your changes have not introduced any regressions. All tests must pass before the task is considered complete.
5.  **Update Documentation:** If your changes affect usage or functionality, update `README.md` and other relevant documentation.

## 3. File Architecture

-   **`src/generate_exam_sample.py`**: Main entry point. Handles argument parsing and orchestrates the PDF generation. Keep this file minimal.
-   **`src/latex_utils.py`**: Contains all functions related to generating and manipulating LaTeX code.
-   **`src/json_utils.py`**: Contains helper functions for reading and writing JSON files.
-   **`src/general_utils.py`**: For general-purpose helper functions.
-   **`data/midterm_question_bank.json`**: The primary data source for questions.
-   **`test/`**: Contains all tests. Unit tests are in `test/test_generate_exam_sample.py`, and acceptance tests are in `test/test_acceptance_full_bank.py`.

## 4. Key Commands

-   **Running Tests:** Use the project's testing framework to execute all tests in the `test/` directory.
-   **Generating PDF:** The main script supports a `--pdf` flag to compile the generated `.tex` file into a PDF using `pdflatex`.
