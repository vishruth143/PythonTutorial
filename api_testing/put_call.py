import requests

url = "https://dummyjson.com/users/2"

payload = {
    "name": "Vishvambruth",
    "job": "Automation Architect"
}

response = requests.put(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 200
assert response.json()["id"] == 2