import requests

param = {'name':'Kiran','email':'kiran@gmail.com'}
response = requests.get("https://httpbin.org/get",params=param)
print(response.text)