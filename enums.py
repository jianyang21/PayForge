from enum import Enum

class PaymentStatus(str, Enum):
    INIT = "INIT"
    AUTHORIZED = "AUTHORIZED"
    CAPTURED = "CAPTURED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
