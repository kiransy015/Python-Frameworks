import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get Request
response = requests.get(url)

# Display Response Content and Response Header
print("Response Content :",response.content)
print("Response Header :",response.headers)

# Validate StatusCode
assert response.status_code==200

# fetch Response Header
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))

# fetch cookies
print(response.cookies)
# fetch encoding
print(response.encoding)
# fetch elapsedtime
print(response.elapsed)


