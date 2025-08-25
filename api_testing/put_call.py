import requests

url = "https://reqres.in/api/users/2"

headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

payload = {
    "name": "Vishvambruth",
    "job": "Automation Architect"
}

response = requests.put(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 200
assert response.json()["job"] == "Automation Architect"