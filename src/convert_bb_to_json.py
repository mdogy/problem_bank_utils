import argparse
import json
import os
import xml.etree.ElementTree as ET
import re

def get_formatted_text(element):
    """
    Recursively finds and returns the text from a mat_formattedtext element,
    handling nested tags.
    """
    if element is None:
        return ""
    
    # Find the mat_formattedtext tag
    mat_formatted_text_element = element.find('.//mat_formattedtext')
    if mat_formatted_text_element is not None:
        # Use a regex to strip HTML tags
        text = mat_formatted_text_element.text or ""
        return re.sub('<[^<]+?>', '', text)
    return ""

def parse_bb_quiz(input_dir, output_file):
    """
    Parses a Blackboard quiz export and converts it to a JSON file.

    Args:
        input_dir (str): The directory containing the unzipped Blackboard quiz files.
        output_file (str): The path to the output JSON file.
    """
    try:
        # 1. Find the question pool file from imsmanifest.xml
        manifest_path = os.path.join(input_dir, 'imsmanifest.xml')
        if not os.path.exists(manifest_path):
            print(f"Error: 'imsmanifest.xml' not found in {input_dir}")
            return

        with open(manifest_path, 'r') as f:
            manifest_content = f.read()
        pool_file_name = re.search(r'<resource.*?type=\"assessment/x-bb-qti-pool\".*?bb:file=\"(.*?)\".*?>', manifest_content, re.DOTALL)
        if pool_file_name:
            pool_file_name = pool_file_name.group(1)
        else:
            print("Error: Could not find question pool file in 'imsmanifest.xml'.")
            return

        if not pool_file_name:
            print("Error: Could not find question pool file in 'imsmanifest.xml'.")
            return

        # 2. Parse the question pool file (e.g., res00001.dat)
        pool_path = os.path.join(input_dir, pool_file_name)
        if not os.path.exists(pool_path):
            print(f"Error: Question pool file '{pool_file_name}' not found.")
            return

        pool_tree = ET.parse(pool_path)
        pool_root = pool_tree.getroot()

        questions = []
        
        # The actual questions are within <item> tags
        for item in pool_root.findall('.//{*}item'):
            question_data = {}
            
            # Get question title
            question_data['title'] = item.get('title')
            
            presentation = item.find('.//{*}presentation')
            if presentation is None:
                continue

            # Find the material tag which contains the question text
            question_data['question_text'] = get_formatted_text(presentation)

            # Find the response processing logic to get the correct answer
            resprocessing = item.find('.//{*}resprocessing')
            correct_answer_id = None
            if resprocessing is not None:
                for respcondition in resprocessing.findall('.//{*}respcondition'):
                    setvar = respcondition.find('.//{*}setvar')
                    if setvar is not None and (setvar.text == '100' or setvar.text == 'SCORE.max'):
                        condition_var = respcondition.find('.//{*}varequal')
                        if condition_var is not None:
                            correct_answer_id = condition_var.text
                            break

            # Find the answer choices
            answers = []
            response_lid = presentation.find('.//{*}response_lid')
            if response_lid is not None:
                for response_label in response_lid.findall('.//{*}response_label'):
                    answer_id = response_label.get('ident')
                    answer_text = get_formatted_text(response_label)
                    is_correct = (answer_id == correct_answer_id)
                    answers.append({
                        'text': answer_text,
                        'correct': is_correct
                    })
            
            question_data['answers'] = answers
            questions.append(question_data)

        # 3. Write to JSON
        with open(output_file, 'w') as f:
            json.dump({"questions": questions}, f, indent=4)

        print(f"Successfully converted {len(questions)} questions to {output_file}")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the script from the command line."""
    parser = argparse.ArgumentParser(description='Convert Blackboard quiz export to JSON.')
    parser.add_argument('input_dir', help='The directory containing the unzipped Blackboard quiz files.')
    parser.add_argument('output_file', help='The path to the output JSON file.')
    
    args = parser.parse_args()
    
    parse_bb_quiz(args.input_dir, args.output_file)

if __name__ == '__main__':
    main()