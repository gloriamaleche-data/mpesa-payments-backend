from fastapi import FastAPI, Request
from datetime import datetime, timezone
from models import DarajaCallBackModel
from pydantic import ValidationError
import uuid
import json

app = FastAPI()


@app.post("/mpesa/callback")
async def mpesa_callback(request: Request):
    tracer_id = str(uuid.uuid4())
    outcome = None
    arrival_time = datetime.now(timezone.utc).isoformat()
    raw_bytes =  await request.body()

    decoded = raw_bytes.decode("utf-8", errors="backslashreplace")

    record = {
        "tracer_id": tracer_id,
        "received_at": arrival_time,
        "raw_body": decoded
    }
    with open("raw_callbacks.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    try:
        parsed_callback = json.loads(decoded)
    except json.JSONDecodeError:
        outcome = "not_json"

    if outcome is None:
        try:
            validated_callback = DarajaCallBackModel.model_validate(parsed_callback)
            outcome = "validated"
        except ValidationError as e:
            outcome = "invalid_shape"

    outcome_results = {"tracer_id": tracer_id, "timestamp": arrival_time, "outcome": outcome, "callback": parsed_callback}

    with open("callback_outcomes.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(outcome_results) + "\n")

    return {"ResultCode": 0, "ResultDesc": "Accepted"}