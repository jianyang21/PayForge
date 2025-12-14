# PayForge

PayForge is a backend-first payment gateway and orchestration service that models how real-world payment systems operate. It focuses on correctness, reliability, and system design rather than UI-driven checkout flows.

---

## Overview

PayForge simulates the core responsibilities of a payment gateway by enforcing strict payment state transitions, preventing duplicate charges using idempotent APIs, and recording all monetary movement through an immutable ledger. The system is designed to act as a payment orchestrator and can be extended to integrate with real payment processors via asynchronous workflows.

---

## Key Features

- State-driven payment lifecycle  
- Idempotent payment creation to prevent duplicate charges  
- Immutable ledger for financial correctness  
- Clean separation of API, business logic, and data layers  
- Designed for extensibility with real payment processors  

---

## Payment Lifecycle

INIT → AUTHORIZED → CAPTURED
↓
FAILED / REFUNDED




---

## Tech Stack

- Backend: FastAPI  
- Database: MongoDB  
- Async Driver: Motor  
- Language: Python  
- API Documentation: Swagger UI  

---


---

## API Endpoints

- `POST /payments`
- `POST /payments/{payment_id}/authorize`
- `POST /payments/{payment_id}/capture`

---

## Running Locally

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload



