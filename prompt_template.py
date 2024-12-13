import requests

def define_company_prompt(content):
    system_prompt = f"""Analyze the following text chunks and identify the company. 
    Just provide the company and the stock code only.
    Chunks:
    {content}
    """
    return system_prompt


def company_overview_prompt(questions):
    system_prompt = f"""
You task is to perform following actions.
1. Analyse the questions delimited by triple backticks. 
2. Extract the questions that is related to company overview from the list below. 
```{questions}```

Provide at least 8 most relevant questions form the list above. Can be more questions if available.

Output format as json. No any additional formatting or backticks
key is question, value is ""

Expected output:
{{question: "", question: "", '''}}

"""
    return system_prompt
    
def revenue_structure_prompt(questions):
    system_prompt = f"""
You task is to perform following actions.
1. Analyse the questions delimited by triple backticks. 
2. Extract the questions that is related to revenue structure from the list below. 
```{questions}```

Provide at least 8 most relevant questions form the list above. Can be more questions if available.

Output format as json. No any additional formatting or backticks
key is question, value is ""

Expected output:
{{question: "", question: "", '''}}

"""
    return system_prompt

def profit_prompt(questions):
    system_prompt = f"""
You task is to perform following actions.
1. Analyse the questions delimited by triple backticks. 
2. Extract the questions that is related to profit from the list below. 
```{questions}```

Provide at least 8 most relevant questions form the list above. Can be more questions if available.

Output format as json. No any additional formatting or backticks
key is question, value is ""

Expected output:
{{question: "", question: "", '''}}

"""
    return system_prompt

def valuation_prompt(questions):
    system_prompt = f"""
You task is to perform following actions.
1. Analyse the questions delimited by triple backticks. 
2. Extract the questions that is related to valuation from the list below. 
```{questions}```

Provide at least 8 most relevant questions form the list above. Can be more questions if available.

Output format as json. No any additional formatting or backticks
key is question, value is ""

Expected output:
{{question: "", question: "", '''}}

"""
    return system_prompt


def future_outlook_prompt(questions):
    system_prompt = f"""
You task is to perform following actions.
1. Analyse the questions delimited by triple backticks. 
2. Extract the questions that is related to future outlook from the list below. 
```{questions}```

Provide at least 8 most relevant questions form the list above. Can be more questions if available.

Output format as json. No any additional formatting or backticks
key is question, value is ""

Expected output:
{{question: "", question: "", '''}}

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


def write_sector_prompt(specific_topic, topic):
    system_prompt = f"""You are a financial report writer helping company to write a {topic} report.
    Write a summary based on the contents delimited by triple backticks.
    
    The report audience is analyst. 
    So, keep the statistics and number in detail if the content provides.

    Generate 200 to 500 words. 
    
    contents: ```{specific_topic}```

    """
    return system_prompt


def write_report_prompt(content):
    system_prompt = f"""You are a financial report writer. 
    Format the text delimited by triple backticks.
    You have the following task to do:
    1. provide a title for each element of the list
    2. write a report using all the content from the list
    4. keep all the content and all the number from the list in detail. Do not summarise the content avoiding lose the number.
    5. 15 to 20 paragraphs for the whole report. 

    at the end of the report, add a summary to summarize the main points from the report.
    
    ```{content}```
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
    Based on the question and expected outcome, verify if the response convey the same meaning with the expected outcome; 
    similar meanings are acceptable. Similar meanings are acceptable.

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