import os
from dotenv import load_dotenv
import requests
import json
from typing import Optional

# Load environment variables from .env file
load_dotenv()
BASE_API_URL = os.getenv('BASE_API_URL')
LANGFLOW_ID = os.getenv('LANGFLOW_ID')
APPLICATION_TOKEN = os.getenv('APPLICATION_TOKEN')
ENDPOINT = "vulgar"  # The endpoint name of the flow

def is_badwords(sentence: str) -> str:
    """
    Checks if a sentence contains bad or offensive words.
    
    Args:
        sentence (str): The sentence to check.

    Returns:
        str: The extracted output text from the API response.
    """
    return run_flow(sentence, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
             output_type: str = "chat",
             input_type: str = "chat",
             application_token: Optional[str] = None) -> str:
    """
    Sends the input to the LangFlow API and extracts the output text.

    Args:
        message (str): The input message to process.
        output_type (str): The output type (default: "chat").
        input_type (str): The input type (default: "chat").
        application_token (str, optional): The API token for authentication.

    Returns:
        str: The output text extracted from the API response.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if application_token:
        headers = {
            "Authorization": "Bearer " + application_token,
            "Content-Type": "application/json"
        }
    response = requests.post(api_url, json=payload, headers=headers)
    response_data = response.json()
    
    # Extract and return the output text
    try:
        output_text = response_data['outputs'][0]['outputs'][0]['results']['text']['data']['text']
        return output_text
    except (KeyError, IndexError):
        return "Error: Unable to extract the output text from the response."

# Example usage
if __name__ == "__main__":
    # Replace this with the sentence you want to check
    test_sentence = "tu bht bada waala harami hai "
    result = is_badwords(test_sentence)
    print(result)
