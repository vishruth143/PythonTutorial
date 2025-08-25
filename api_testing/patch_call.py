import requests

url = "https://reqres.in/api/users/2"

payload = {
    "job": "Python SDET"
}

headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 200
assert response.json()["job"] == "Python SDET"