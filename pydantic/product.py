from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = "No Description Provided"

p1 = Product(id=1, name="Laptop", price=999.99)
print(p1)
print(p1.model_dump())
print(p1.model_json_schema())