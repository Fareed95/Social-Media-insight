from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import requests
from typing import Optional
import os 
from dotenv import load_dotenv
load_dotenv()

BASE_API_URL = os.getenv('BASE_API_URL')
LANGFLOW_ID = os.getenv('LANGFLOW_ID')
FLOW_ID = os.getenv('FLOW_ID')
APPLICATION_TOKEN = os.getenv('APPLICATION_TOKEN')
endpoint = os.getenv('endpoint')

# Define the input data model for the request
class InsightRequest(BaseModel):
    input_type: str

# FastAPI app setup
app = FastAPI()

def insight(input_type):
    TWEAKS = {
        "TextInput-jY7jv": {
            "input_value": input_type
        }
    }
    return run_flow("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
              output_type: str = "chat",
              input_type: str = "chat",
              tweaks: Optional[dict] = None,
              application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    response_json = response.json()
    try:
        output_text = response_json['outputs'][0]['outputs'][0]['results']['text']['data']['text']
        return output_text
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"Error parsing response: {e}")

@app.post("/insight/")
async def get_insight(request: InsightRequest):
    input_type = request.input_type
    result = insight(input_type)
    return {"insight": result}
