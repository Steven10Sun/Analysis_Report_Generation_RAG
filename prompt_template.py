import requests

def define_company_prompt(content):
    system_prompt = f"""Analyze the following text chunks and identify the company. 
    Just provide the company and the stock code only.
    Chunks:
    {content}
    """
    return system_prompt

def ask_question_prompt(content, question):
    system_prompt = f"""You are an financial analyst.
    Use the following pieces of retrieved context to answer the question. 
    Use 5 sentences in maximum for question and keep the answer concise.
    Please provide statistic description if available.


    Retrieved context:
    {content}\n

    Question:
    {question}
    """
    return system_prompt

# pending: seperate to 5 report format
def write_report_prompt(content):
    system_prompt = f"""You are a financial report writer. 
    Please combine the text provided and generate a financial analysis report. 
    The report should be about 15 to 20 paragraphs. 
    The report should include the following sections. Please include statistics description and numbers for the points.
    1. Company Overview
    2. Revenue Structure
    3. Profit
    4. Valuation
    5. Summary
    6. Future Outlook
    7. and other details provided.
    
    content is as below:
    {content}
    """
    return system_prompt


def evaulate_keyword_prompt1(keywords, report):
    system_prompt = f"""You are a checker.
    Task:
    Verify if the report covers all the key points listed in the keywords.
    The wording in the report does not need to match the keywords exactly; similar meanings are acceptable.
    Output:
    If report has the message from the keyword, please show the answer with the format below:
    First item: The key point from the keywords.
    Second item: The original text from the report that covers the point.
    Please provide the score indicating how many keywords matched, along with the percentage
    
    keywords:
    {keywords}

    report:
    {report}
    """
    return system_prompt

def validate_response_prompt(question, expected_value, response):
    system_prompt = f"""You are a checker.
    Task:
    Based on the question and expected outcome, verify if the response convey the same meaning with the expected outcome; similar meanings are acceptable. Similar meanings are acceptable.

    Output:
    1 if they present the same message.
    Provide the original sentense of expected message if response is wrong.

    question:
    {question}
    
    expected message:
    {expected_value}

    response:
    {response}
    """
    return system_prompt


def generate_response(prompt, api_key, system_content='you are a assistant'):
    model = 'gpt-4o-mini'
    url = "https://api.ohmygpt.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    return response_json["choices"][0]["message"]["content"]