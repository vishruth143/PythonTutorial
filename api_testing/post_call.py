import requests

url = "https://reqres.in/api/users"

headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}


payload = {
    "name": "Vishvambruth",
    "job": "SDET"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 201
assert response.json()["name"] == "Vishvambruth"