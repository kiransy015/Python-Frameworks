import requests


# print('--------------------------------------------------')
# res = requests.get("http://localhost:8085/student/list")
# print(res.text)
# print(res.status_code)


# print('--------------------------------------------------')
# res = requests.get("http://localhost:8085/student/1")
# print(res.status_code)
# print(res.text)


# print('--------------------------------------------------')
# res = requests.get("http://localhost:8085/student/list?programme=Financial Analysis&limit=3")
# print(res.status_code)
# print(res.text)


# print('--------------------Get Call with Params------------------------------')
# res = requests.get("http://localhost:8085/student/list",params={"programme":"Financial Analysis","limit":"3"})
# # Print Status code
# print(res.status_code)
# # Print text
# print(res.text)
# # Print type
# print(type(res))
# # Convert to json
# json_res = res.json()
# # Print json res
# print(json_res)
# # Print type
# print(type(json_res))
# # Print the value
# print(json_res[0]['id'])


# print('--------------------Authentication------------------------------')
# res = requests.get('https://api.github.com/user',auth=('kiransy015','ctyrkksy@9873015171'))
# print(res.status_code)
# print(res.text)
from requests import auth, Timeout
from urllib3.util import timeout

# print('--------------------Timeout------------------------------')
# try:
#     res = requests.get('https://api.github.com/user',auth=('kiransy015','ctyrkksy@9873015171'),timeout=(0.1,0.1))
# except Timeout:
#     print('Connection Timedout')
#     print(res.status_code)
#     print(res.text)
# else:
#     print('Connected')
#     print(res.status_code)
#     print(res.text)


# print('--------------------Session------------------------------')
# with requests.session() as session:
#     session.auth=('kiransy015','ctyrkksy@9873015171')
#
#     res1 = session.get('https://api.github.com/user')
#     print(res1.status_code)
#     print(res1.text)
#
#     res2 = session.get('https://github.com/kiransy015/Practise-test')
#     print(res2.status_code)
#     print(res2.text)


print('--------------------Post Operation------------------------------')






















