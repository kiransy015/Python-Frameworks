import requests
import json
import jsonpath

# API url
url = "http://thetestingworldapi.com/api/studentsDetails"

# Read file content
file = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/DataDrivenTesting/JsonTestData.json",'r')
fileinput = file.read()

# Convert to json format
json_request = json.loads(fileinput)


# Post the content
response = requests.post(url,data=json_request)

print(response.content)
print(response.status_code)

# Validate status code
assert response.status_code==201

