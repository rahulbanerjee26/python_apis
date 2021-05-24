from twilio.rest import Client
from dotenv import load_dotenv
import os 


load_dotenv()
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_ACCOUNT_TOKEN = os.environ.get("TWILIO_ACCOUNT_TOKEN")
client = Client(TWILIO_ACCOUNT_SID , TWILIO_ACCOUNT_TOKEN)

calls = client.calls.list(limit=5)

for idx, record in enumerate(calls):
    print(f"{idx}. {record.duration}")

