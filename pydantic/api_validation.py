from typing import Optional, List,Annotated
from pydantic import BaseModel, EmailStr, Field

class CartItem(BaseModel):
    sku: str
    qty: Annotated[int,Field(ge=1)]
    price: Annotated[float,Field(ge=0)]

class CheckoutRequest(BaseModel):
    user_email: EmailStr
    items: List[CartItem]
    coupon_code: Optional[str] = None

incoming_ok = {
    "user_email": "alice@example.com",
    "items": [
        {"sku": "LAP-101", "qty": 1, "price": 49999.99},
        {"sku": "MSE-201", "qty": 2, "price": 799.0},
    ]
}

print("✅ Valid checkout:")
checkout = CheckoutRequest(**incoming_ok)
print(checkout.model_dump())

# Example 2: Invalid (qty=0, bad email)
incoming_bad = {
    "user_email": "alice_at_example.com",
    "items": [
        {"sku": "LAP-101", "qty": 0, "price": 49999.99},
    ]
}

print("\n❌ Invalid checkout:")
try:
    CheckoutRequest(**incoming_bad)
except Exception as e:
    print(e)
