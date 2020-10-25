import requests
from requests.exceptions import Timeout
#
# response = requests.get('http://localhost:8085/student/list')
# print(response.status_code)
# print(response.text)
#
# print('--------------------------------------------------')
# response = requests.get('http://localhost:8085/student/1')
# print(response.status_code)
# print(response.text)
#
# print('--------------------------------------------------')
# response = requests.get('http://localhost:8085/student/list?programme=Financial Analysis&limit=2')
# print(response.status_code)
# print(response.text)


# print('--------------------Get Call with Params------------------------------')
# response = requests.get('http://localhost:8085/student/list?',params={"programme":"Financial Analysis","limit":"2"})
# #Print status code
# print('Status Code :',response.status_code)
# #Print response text
# print('Response text :',response.text)
# json_response = response.json()
# #Print type of response
# print('Type of response :',type(json_response))
# print(json_response)
# #Print value from the list
# print('First value from the list :',json_response[0])


# print('--------------------Authentication------------------------------')
#
# response = requests.get('https://api.github.com/user', auth=('kiransy015', 'ctyrkksy@9873015171'))
# print(response.status_code)
# print(response.text)


# print('--------------------Timeout------------------------------')
#
# try:
#     response = requests.get('https://api.github.com/user', auth=('kiransy015', 'ctyrkksy@9873015171'),timeout=(0.1,0.1))
# except Timeout:
#     print('The request timed out')
#     print(response.status_code)
#     print(response.text)
# else:
#     print('The request did not time out')
#     print(response.status_code)
#     print(response.text)


print('--------------------Session------------------------------')

with requests.Session() as session:
    session.auth=('kiransy015','ctyrkksy@9873015171')

    # response1 = session.get('https://api.github.com/user')
    # print(response1.status_code)
    # print(response1.text)

    response2 = session.get('https://github.com/kiransy015/Practise-test')
    print(response2.status_code)
    print(response2.text)





