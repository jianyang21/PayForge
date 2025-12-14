from uuid import uuid4
from enums import PaymentStatus
from database import payments_collection, ledger_collection, idempotency_collection
from datetime import datetime

async def create_payment(data):
    # Idempotency check
    existing = await idempotency_collection.find_one(
        {"key": data["idempotency_key"]}
    )
    if existing:
        return existing["response"]

    payment_id = str(uuid4())

    payment = {
        "_id": payment_id,
        "user_id": data["user_id"],
        "amount": data["amount"],
        "currency": data["currency"],
        "status": PaymentStatus.INIT,
        "created_at": datetime.utcnow()
    }

    await payments_collection.insert_one(payment)

    response = {
        "payment_id": payment_id,
        "status": PaymentStatus.INIT
    }

    await idempotency_collection.insert_one({
        "key": data["idempotency_key"],
        "response": response
    })

    return response


async def authorize_payment(payment_id):
    payment = await payments_collection.find_one({"_id": payment_id})

    if not payment:
        raise Exception("Payment not found")

    if payment["status"] != PaymentStatus.INIT:
        raise Exception("Invalid state transition")

    await payments_collection.update_one(
        {"_id": payment_id},
        {"$set": {"status": PaymentStatus.AUTHORIZED}}
    )

    return {"payment_id": payment_id, "status": PaymentStatus.AUTHORIZED}


async def capture_payment(payment_id):
    payment = await payments_collection.find_one({"_id": payment_id})

    if not payment:
        raise Exception("Payment not found")

    if payment["status"] != PaymentStatus.AUTHORIZED:
        raise Exception("Invalid state transition")

    # Ledger entry (immutable)
    ledger_entry = {
        "payment_id": payment_id,
        "debit_account": "USER_WALLET",
        "credit_account": "MERCHANT_ACCOUNT",
        "amount": payment["amount"],
        "created_at": datetime.utcnow()
    }

    await ledger_collection.insert_one(ledger_entry)

    await payments_collection.update_one(
        {"_id": payment_id},
        {"$set": {"status": PaymentStatus.CAPTURED}}
    )

    return {"payment_id": payment_id, "status": PaymentStatus.CAPTURED}
