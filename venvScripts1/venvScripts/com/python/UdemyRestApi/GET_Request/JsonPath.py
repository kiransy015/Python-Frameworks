import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# # Send get Request
# response = requests.get(url)
#
# # Parse response to Json format
# json_response = json.loads(response.content)
# # print(json_response)
#
# # fetch value using jsonpath
# pages = jsonpath.jsonpath(json_response,"total_pages")
# print(pages[0])
# assert pages[0]==4


# *********************** fetch first user firstname ********************************
# # get response
# response = requests.get(url)
#
# # convert to json format
# json_response = json.loads(response.content)
#
# # print firstname of first user
# firstname = jsonpath.jsonpath(json_response,"data[0].first_name")
# print("firstname of first user :",firstname[0])



# *********************** fetch firstname of all users ********************************

# # get response
# response = requests.get(url)
#
# # convert to json format
# json_response = json.loads(response.content)
#
# # print firstname of all users
# for i in range(0,3):
#     firstname = jsonpath.jsonpath(json_response,"data["+str(i)+"].first_name")
#     print(firstname[0])










