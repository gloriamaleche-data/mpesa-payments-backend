from fastapi import FastAPI, Request
import json

app = FastAPI()


@app.post("/mpesa/callback")
async def mpesa_callback(request: Request):
    payload = await request.json()

    print(json.dumps(payload, indent=2))

    with open("callbacks.json1", "a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")

    return {"ResultCode": 0, "ResultDesc": "Accepted"}