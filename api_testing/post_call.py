import requests

url = "https://dummyjson.com/users/add"

payload = {
    "name": "Vishvambruth",
    "job": "SDET"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 201
assert response.json()["id"] is not None