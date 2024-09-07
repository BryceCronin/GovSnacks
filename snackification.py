import requests

def snackify_meal(document, openai_api_key, interests):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        # Check if interests are specified and customize the prompt accordingly

        if interests:  # If interests are not empty or whitespace
            prompt = f"The following is a report of proceedings from Parliament House in Australia. Focus on the following issues of interest: {interests}. It is political, so try to be unbiased. Please summarize them in an easily understandable way: {document}."
        else:
            prompt = f"The following is a report of proceedings from Parliament House in Australia. It is political, so try to be unbiased. Please summarize it into an easily understandable summary: {document}."

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    #f"The following is a report of proceedings from Parliament House in Australia, can you please summarise it into an easily understandable summary. {document}."
                    "content": prompt
                }
            ],
            "max_tokens": 1000
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        #print(response.json())
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print("An error occurred while snackifying content:", e)