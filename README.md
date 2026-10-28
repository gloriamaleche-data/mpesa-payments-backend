# M-Pesa Payments Backend

A Python project that connects invoices to M-Pesa payments using
Safaricom's Daraja API. It requests a payment from a customer's phone
and receives the result on its own API (built using FastAPI).

**Status: work in progress. Sandbox only. No real payments used.**

## What works so far

- Authenticating with the Daraja API (access token)
- Sending an STK Push request in the sandbox
- A FastAPI server that receives Safaricom's callback and logs it

## What's next

- Validating callbacks with Pydantic
- Checking payment status when a callback goes missing
- Saving payments in MySQL and matching them to invoices

## Run it locally

1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in your own sandbox values.
4. Start the server: `uvicorn main:app --reload`
5. To receive callbacks, expose the server with a tunnel such as ngrok
   and put the public address in `DARAJA_CALLBACK_URL`.

## Security notes

- `.env` holds secrets and is never committed.
- Payment logs (`*.jsonl`) are ignored by git.