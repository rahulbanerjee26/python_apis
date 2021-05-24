from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os 
import requests

load_dotenv()
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_ACCOUNT_TOKEN = os.environ.get("TWILIO_ACCOUNT_TOKEN")

api_endpoint = f'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Calls.json?PageSize=5'

auth = HTTPBasicAuth(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_TOKEN)

response = requests.get(api_endpoint , auth = auth)

for idx, item in enumerate(response.json()['calls']):
    print(f"{idx+1}. {item['duration']}")
