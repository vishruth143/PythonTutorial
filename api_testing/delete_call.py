import requests

url = "https://reqres.in/api/users/2"

headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.text)  # Usually empty

# Assertion Example
assert response.status_code == 204