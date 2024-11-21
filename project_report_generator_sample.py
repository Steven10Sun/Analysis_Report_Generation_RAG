import PyPDF2
import requests

# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text


# Step 2: Prepare role-specific questions
balance_sheet_questions = [
    "What are the total assets?",
    "What are the total liabilities?",
    # Add more questions related to the balance sheet
]

income_statement_questions = [
    "What is the company's net income?",
    "What are the total revenues?",
    # Add more questions related to the income statement
]

background_questions = [
    "Provide an overview of the company.",
    "What is the industry context?",
    # Add more questions for background information
]

strategy_questions = [
    "What are the strategic recommendations for the company?",
    # Add more questions for strategic insights
]

# Step 3: Function to generate answers
def generate_answer(context, question, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "messages": [
            {"role": "system", "content": "You are a summarizing assistant."},
            {"role": "user", "content": f"Context: {context} Question: {question}"}
        ],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# Step 4: Aggregate answers for each role
def generate_summary(answers, api_key):
    summary_prompt = "Summarize the following answers into a comprehensive paragraph:\n\n" + "\n\n".join(answers)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "messages": [
            {"role": "system", "content": "You are a summarizing assistant."},
            {"role": "user", "content": summary_prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# Example usage
pdf_path = "path/to/your/annual_report.pdf"
api_key = "your_openai_api_key"
context = extract_text_from_pdf(pdf_path)

# Collect answers for each role
roles_questions = {
    "Balance Sheet Analyst": balance_sheet_questions,
    "Income Statement Analyst": income_statement_questions,
    "Background Generator": background_questions,
    "Strategy Maker": strategy_questions
}

role_answers = {role: [] for role in roles_questions}

for role, questions in roles_questions.items():
    for question in questions:
        answer = generate_answer(context, question, api_key)
        role_answers[role].append(f"Q: {question}\nA: {answer}\n")

# Summarize answers for each role
summaries = {}
for role, answers in role_answers.items():
    summaries[role] = generate_summary(answers, api_key)

# Combine role summaries into a final report
final_report = "Analytics Report\n\n"
for role, summary in summaries.items():
    final_report += f"Role: {role}\n{summary}\n\n"

print(final_report)


#################### from Ming ####################

import requests


def get_answers(context, key):

    model = 'gpt-4o-mini'
    url = "https://api.ohmygpt.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    if type(context) == list:
        messages = []
        for i, c in enumerate(context):
            if i % 2 == 0:
                role = "user"
            else:
                role = "assistant"
            messages.append({"role": role, "content": c})
        data = {
            "model": model,
            "messages": messages,
            "temperature": 0.7
        }
    else:
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": context}
            ],
            "temperature": 0.7
        }
    while True:
        response = requests.post(url, headers=headers, json=data)
        # check if the response is successful
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(response.text)
            raise ValueError("Error in the response")
        response_json = response.json()

        # Parse the JSON response
        # response_data = json.loads(response_json)
        assistant_reply = response_json["choices"][0]["message"]["content"]
        break

        # # check if it is a json
        # try:
        #     json.loads(assistant_reply)
        #     break
        # except:
        #     print(assistant_reply)
        #     pass
    return assistant_reply



key = "sk-NAWSSGI7999d18B51046T3BlBkFJ514d034054e342cc99c3"
print(get_answers("How are you today?", key))
