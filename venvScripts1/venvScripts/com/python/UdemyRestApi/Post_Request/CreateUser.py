import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users"


# Read file content
file = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/Post_Request/CreateUser.json",'r')
fileinput = file.read();

# convert to json format
jsoninput = json.loads(fileinput)

# post the content
response = requests.post(url,data=jsoninput)
print(response.status_code)
print(response.content)

# Validation Response code
assert response.status_code==201

# Fetch header from the Response
print(response.headers)

# Parse response to json format
jsonresponse = json.loads(response.content)

# Read id of new user
userid = jsonpath.jsonpath(jsonresponse,"id")
print("User id :",userid)

