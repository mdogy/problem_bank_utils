
# Session Summary

## Goal

The main goal is to create a LaTeX PDF from the `data/midterm_question_bank.json` file to help the user select exam questions. The PDF should be well-formatted and include metadata for each question to facilitate the selection process.

## File Status

*   **`src/generate_exam_sample.py`**: This is the main script that will generate the LaTeX file. It includes a command-line interface, logging, and is intended to be the final, production-ready script.

*   **`src/latex_utils.py`**: This file contains the `escape_latex` utility function, which is responsible for escaping special LaTeX characters. This function is currently the source of a bug and is not working as expected.

*   **`src/test_generate_exam_sample.py`**: This is the test file for the `src/generate_exam_sample.py` script. The tests in this file are currently failing because of the bug in the `escape_latex` function.

## Current State

We are currently in the process of debugging the `escape_latex` function. The function is not correctly escaping all special LaTeX characters, which is causing the unit tests to fail. The immediate next step is to fix this function so that all tests in `src/test_generate_exam_sample.py` pass.
