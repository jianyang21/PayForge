from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)

db = client.payment_gateway
payments_collection = db.payments
ledger_collection = db.ledger
idempotency_collection = db.idempotency
