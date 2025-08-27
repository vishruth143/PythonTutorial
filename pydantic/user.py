from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int

u1=User(id=1,name="Alice",age=25)
print(u1)

try:
    u2=User(id=2,name="Bob",age="Twenty")  # This will raise a validation error
except Exception as e:
    print("Error:", e)