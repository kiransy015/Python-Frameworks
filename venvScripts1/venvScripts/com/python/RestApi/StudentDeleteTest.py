import requests

response = requests.delete('http://localhost:8085/student/105')
print(response.status_code)
print(response.text)