import requests
import os
from dotenv import load_dotenv
import webbrowser
from urllib.parse import urlencode

load_dotenv()
GENIUS_CLIENT_ID = os.environ.get("GENIUS_CLIENT_ID")
GENIUS_CLIENT_SECRET = os.environ.get("GENIUS_CLIENT_SECRET")

parameters = {
    'client_id': GENIUS_CLIENT_ID,
    'redirect_uri': 'https://httpbin.org/anything',
    'response_type': 'code',
    'scope': 'me'
}
endpoint = "https://api.genius.com/oauth/authorize"
endpoint = endpoint + '?' + urlencode(parameters)
webbrowser.open(endpoint)
code = input("Enter the Code: ")

print(code)
parameters = {
    "code": code,
    "client_id": GENIUS_CLIENT_ID,
    "client_secret": GENIUS_CLIENT_SECRET,
    "redirect_uri": 'https://httpbin.org/anything',
    "response_type": "code",
    "grant_type": "authorization_code"
}

response = requests.post("https://api.genius.com/oauth/token", params = parameters).json()
print(response)
access_token = response["access_token"]

session = requests.session()
session.headers = {"authorization": f"Bearer {access_token}"}

base_api_endpoint = "https://api.genius.com/account"

response = session.get(base_api_endpoint)
print(response)