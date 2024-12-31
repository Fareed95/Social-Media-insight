from astrapy import DataAPIClient
from dotenv import load_dotenv
import os
load_dotenv()


astra_api_key = os.getenv('ASTRA_API_KEY')
astra_api_url = os.getenv('ASTRA_ENDPOINT')

client = DataAPIClient(astra_api_key)
db = client.get_database_by_api_endpoint(astra_api_url)
print(f"Connected to Astra DB: {db.list_collection_names()}")
