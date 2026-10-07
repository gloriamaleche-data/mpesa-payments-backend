import os
from get_token import get_access_token
from dotenv import load_dotenv
from datetime import datetime
import base64
import requests

load_dotenv()
access_token = get_access_token()
url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

shortcode = os.getenv("DARAJA_SHORTCODE")
passkey = os.getenv("DARAJA_PASSKEY")
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
phone = os.getenv("DARAJA_TEST_PHONE")

raw = shortcode + passkey + timestamp

password = base64.b64encode(raw.encode()).decode()

body = {
    "BusinessShortCode":shortcode,
    "Password":password,
    "Timestamp":timestamp,
    "TransactionType":"CustomerPayBillOnline",
    "Amount":1,
    "PartyA":phone,
    "PartyB":shortcode,
    "PhoneNumber":phone,
    "CallBackURL":"https://example.com/callback",
    "AccountReference": "INV-0001",
    "TransactionDesc":"Payment INV-0001",
}
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.post(url, json=body, headers=headers, timeout=30)

print("Status Code:", response.status_code)
print("Reply:", response.text)
