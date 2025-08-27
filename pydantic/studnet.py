from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Annotated

class Student(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=40)]  # Name must be between 3 and 40 characters
    age: Annotated[int, Field(ge=18, le=60)]  # Age must be between 18 and 60
    gpa: Annotated[float, Field(ge=0, le=10)]
    email: EmailStr
    website: AnyUrl


s1 = Student(name="Bob", age=25, gpa=8.9, email="bob@bob.com", website="http://www.bob.com")
print(s1)

try:
    s2 = Student(name="Alice", age=16, gpa=12.5, email="notaemail", website="notaurl")
    print(s2)
except Exception as e:
    print(e)