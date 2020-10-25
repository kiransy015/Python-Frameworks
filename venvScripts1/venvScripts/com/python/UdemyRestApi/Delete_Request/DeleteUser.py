import requests

# API url
url = "https://reqres.in/api/users/2"

# Delete the user
response = requests.delete(url)
print(response.status_code)

assert response.status_code==204