"""
Utility functions for JSON file operations.
"""

import json
import re
import logging


def read_json_file(filepath, logger=None):
    """
    Reads a JSON file and returns the parsed data.
    
    Args:
        filepath: Path to the JSON file
        logger: Optional logger instance for error logging
        
    Returns:
        Parsed JSON data (list or dict), or None if error occurs
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the JSON is invalid
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        error_msg = f"Input file not found: {filepath}"
        if logger:
            logger.error(error_msg)
        raise
    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON in input file: {filepath}"
        if logger:
            logger.error(error_msg)
        raise


def write_json_file(filepath, data, indent=4, logger=None):
    """
    Writes data to a JSON file.
    
    Args:
        filepath: Path to the output JSON file
        data: Data to write (must be JSON-serializable)
        indent: Number of spaces for indentation (default: 4)
        logger: Optional logger instance for info logging
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
    
    if logger:
        logger.info(f"Successfully wrote JSON file: {filepath}")


def extract_json_from_markdown(md_content):
    """
    Extracts JSON content from markdown code blocks.
    
    Args:
        md_content: String containing markdown content
        
    Returns:
        List of parsed JSON objects extracted from markdown code blocks
    """
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

