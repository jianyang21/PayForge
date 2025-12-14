from fastapi import FastAPI, HTTPException
from models import CreatePaymentRequest
from services import create_payment, authorize_payment, capture_payment

app = FastAPI(title="Payment Gateway Simulator")

@app.post("/payments")
async def create_payment_api(req: CreatePaymentRequest):
    return await create_payment(req.dict())


@app.post("/payments/{payment_id}/authorize")
async def authorize_payment_api(payment_id: str):
    try:
        return await authorize_payment(payment_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/payments/{payment_id}/capture")
async def capture_payment_api(payment_id: str):
    try:
        return await capture_payment(payment_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
