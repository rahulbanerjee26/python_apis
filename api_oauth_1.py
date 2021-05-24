import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode
import webbrowser

load_dotenv()
CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.environ.get("GITHUB_CLIENT_SECRET")
REDIRECT_URI = "https://httpbin.org/anything"

params = {
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": "user"
}

endpoint = "https://github.com/login/oauth/authorize"
endpoint = endpoint + '?' + urlencode(params)
webbrowser.open(endpoint)

code = input("Enter the Code: ")
print("Got Code")

params = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": REDIRECT_URI,
    "code": code,
}
endpoint = "https://github.com/login/oauth/access_token"
response = requests.post(endpoint, params=params, headers = {"Accept": "application/json"}).json()
access_token = response['access_token']
print("Got Access Token")

session = requests.session()
session.headers = {"Authorization": f"token {access_token}"}

base_api_endpoint = "https://api.github.com/user"

response = session.get(base_api_endpoint)
print(response)

response = session.get(base_api_endpoint + '/repos')
print(response)

response = session.get(base_api_endpoint + '/emails')
print(response)