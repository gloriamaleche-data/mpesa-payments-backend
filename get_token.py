import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
key = os.getenv("DARAJA_CONSUMER_KEY")
secret = os.getenv("DARAJA_CONSUMER_SECRET")

def get_access_token() -> str:
    response = requests.get(
        url=url,
        params={"grant_type": "client_credentials"},
        auth=(key, secret),
        timeout=15,
    )
    print(f"Status code: {response.status_code}")
    response.raise_for_status()
    return response.json()["access_token"]

if __name__ == "__main__":
    print(get_access_token())