import requests

requestheaders = {'T1':'Req1','T2':'Req2'}

response = requests.get("https://httpbin.org/get",headers=requestheaders)
print(response.text)