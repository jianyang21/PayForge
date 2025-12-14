from pydantic import BaseModel
from enums import PaymentStatus
from uuid import UUID
from typing import Optional

class CreatePaymentRequest(BaseModel):
    amount: int
    currency: str
    user_id: str
    idempotency_key: str

class PaymentResponse(BaseModel):
    payment_id: str
    status: PaymentStatus
