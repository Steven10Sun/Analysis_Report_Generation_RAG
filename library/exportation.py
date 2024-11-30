import os
import json
from datetime import datetime

def export_prompt_response(verion, file_name, prompt_response):
    folder_path = os.path.join(verion, '1_prompt_log')

    # Get the current datetime
    current_datetime = datetime.now().strftime('%Y%m%d%H')

    # Define the JSON file path with datetime suffix
    json_file_path = os.path.join(folder_path, f'{file_name}_{current_datetime}.json')

    # Write JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(prompt_response, json_file, indent=4)

    print(f"JSON data has been exported to {json_file_path}")

def export_article(version, file_name, report):
    folder_path = os.path.join(version, '2_report_log')

    # Get the current datetime
    current_datetime = datetime.now().strftime('%Y%m%d%H')

    # Define the JSON file path with datetime suffix
    report_path = os.path.join(folder_path, f'{file_name}_{current_datetime}.txt')

    # Write JSON data to a file
    with open(report_path, 'w') as txt_file: 
        txt_file.write(report)
        
    print(f"report has been exported to {report_path}")

def export_evaluation_result(file_name, result):
    folder_path = '5_evaluation_log'

    # Get the current datetime
    current_datetime = datetime.now().strftime('%Y%m%d%H')

    # Define the JSON file path with datetime suffix
    report_path = os.path.join(folder_path, f'{file_name}_{current_datetime}.txt')

    # Write JSON data to a file
    with open(report_path, 'w') as txt_file: 
        txt_file.write(result)
        
    print(f"report has been exported to {report_path}")