import requests

response = requests.get('http://localhost:8085/student/list?programme=Computer Science&limit=3')
json_resp = response.json();
print(type(json_resp))

print("First Student details :",json_resp[0]['id'])