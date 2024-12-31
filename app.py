import os
import requests
from dotenv import load_dotenv
from astrapy import DataAPIClient
from langflow import Graph, Node

# Load environment variables
load_dotenv()

# Set up environment variables for Astra DB and Groq
groq_api_key = os.getenv('GROQ_API_KEY')
groq_endpoint = os.getenv('GROQ_ENDPOINT')
astra_api_key = os.getenv('ASTRA_API_KEY')
astra_api_url = os.getenv('ASTRA_ENDPOINT')

# Initialize Astra DB client
client = DataAPIClient(astra_api_key)
db = client.get_database_by_api_endpoint(astra_api_url)
session = db.get_session()

# Langflow Nodes

# Node 1: Fetch engagement data from Astra DB
def fetch_engagement_data(post_type):
    query = f"""
    SELECT AVG(likes) AS avg_likes, AVG(shares) AS avg_shares, AVG(comments) AS avg_comments
    FROM engagement
    WHERE post_type = '{post_type}'
    """
    
    result = session.execute(query)
    
    if result:
        row = result[0]
        return {
            "average_likes": row['avg_likes'],
            "average_shares": row['avg_shares'],
            "average_comments": row['avg_comments']
        }
    else:
        return None

# Node 2: Generate insights using Groq
def generate_insights(avg_likes, avg_shares, avg_comments):
    headers = {
        'Authorization': f'Bearer {groq_api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "likes": avg_likes,
        "shares": avg_shares,
        "comments": avg_comments
    }

    response = requests.post(groq_endpoint, json=data, headers=headers)

    if response.status_code == 200:
        return response.json().get('insight', 'No insight generated.')
    else:
        return f"Error fetching insight from Groq: {response.status_code}"

# Langflow Workflow Setup

# Create the Langflow graph (workflow)
graph = Graph()

# Define the workflow
post_type = "carousel"  # Example post type
engagement_data = fetch_engagement_data(post_type)

if engagement_data:
    avg_likes = engagement_data['average_likes']
    avg_shares = engagement_data['average_shares']
    avg_comments = engagement_data['average_comments']
    
    insights = generate_insights(avg_likes, avg_shares, avg_comments)
    print(insights)
else:
    print("No data found for this post type.")
