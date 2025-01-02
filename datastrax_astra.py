import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

ASTRA_API_KEY = os.getenv("ASTRA_API_KEY")
ASTRA_ENDPOINT = os.getenv("ASTRA_ENDPOINT")

def fetch_cql_data():
    headers = {
        "X-Cassandra-Token": ASTRA_API_KEY,
        "Content-Type": "application/json",
    }
    # URL for executing CQL queries
    url = f"{ASTRA_ENDPOINT}/api/rest/v2/namespaces/default_keyspace/cql"

    # Define the query
    query = {
        "query": "SELECT * FROM default_keyspace;"
    }

    # Make the POST request
    response = requests.post(url, json=query, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Query Results:")
        for row in data.get("rows", []):
            print(row)
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_cql_data()
