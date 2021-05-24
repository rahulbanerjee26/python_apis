from dotenv import load_dotenv
import os 
import requests

api_endpoint = "https://api.thecatapi.com/v1/breeds"

load_dotenv()
CAT_API_KEY = os.environ.get("CAT_API_KEY")

headers = {
    "x-api-key" : CAT_API_KEY
}
response = requests.get(
    api_endpoint,
    headers = headers
)

for idx, item in enumerate(response.json()):
    print(f"{idx+1}. {item['name']} : {item['description']}")


