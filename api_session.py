from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os 
import requests

load_dotenv()
GITHUB_API_TOKEN = os.environ.get("GITHUB_API_TOKEN")

base_api_endpoint = "https://api.github.com/user"

auth = HTTPBasicAuth("rahulbanerjee26", GITHUB_API_TOKEN)

session = requests.Session()
session.auth = auth

response = session.get(base_api_endpoint + '/repos')

for idx, item in enumerate(response.json()):
    print(f"{idx+1}. {item['name']}")

response = session.get(base_api_endpoint + '/emails')
for idx, item in enumerate(response.json()):
    print(f"{idx+1}. {item['email']}")




