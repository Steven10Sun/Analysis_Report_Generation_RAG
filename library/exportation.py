import os
import json
from datetime import datetime

def export_prompt_response(file_name, prompt_response):
    folder_path = '1_prompt_log'

    # Get the current datetime
    current_datetime = datetime.now().strftime('%Y%m%d_%H%M')

    # Define the JSON file path with datetime suffix
    json_file_path = os.path.join(folder_path, f'{file_name}_{current_datetime}.json')

    # Write JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(prompt_response, json_file, indent=4)

    print(f"JSON data has been exported to {json_file_path}")

def export_article(file_name, report):
    folder_path = '2_report_log'

    # Get the current datetime
    current_datetime = datetime.now().strftime('%Y%m%d_%H%M')

    # Define the JSON file path with datetime suffix
    report_path = os.path.join(folder_path, f'{file_name}_{current_datetime}.txt')

    # Write JSON data to a file
    with open(report_path, 'w') as txt_file: 
        txt_file.write(report)
        
    print(f"report has been exported to {report_path}")

