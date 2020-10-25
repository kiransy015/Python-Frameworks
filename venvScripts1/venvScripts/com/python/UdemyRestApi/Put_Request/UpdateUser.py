import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users/2"

# Read file content
file = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/Put_Request/UpdateUser.json",'r')
fileinput = file.read()

# convert to json format
jsonrequest = json.loads(fileinput)

# Update the user
response = requests.put(url,jsonrequest)

# Validate Response code
assert response.status_code==200

# Fetch updatedAt value
jsonresponse = json.loads(response.content)
print(jsonresponse)
updatedAt = jsonpath.jsonpath(jsonresponse,"updatedAt")
print("UpdatedAt :",updatedAt[0])