import requests

url = "https://dummyjson.com/users/2"

payload = {
    "job": "Python SDET"
}

response = requests.patch(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 200
assert response.json()["id"] == 2