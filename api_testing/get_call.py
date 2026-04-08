import requests

url = "https://dummyjson.com/users/2"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Assertion Example
assert response.status_code == 200
assert response.json()["id"] == 2