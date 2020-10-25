import requests
import json
import jsonpath


def test_AddNewStudent():
    url = "http://thetestingworldapi.com/api/studentsDetails"

    # Read file content
    f = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/DataDrivenTesting/JsonTestData.json")
    fileinput = f.read()
    json_request = json.loads(fileinput)

    response = requests.post(url,data=json_request)
    json_response = json.loads(response.content)
    global id
    id = jsonpath.jsonpath(json_response,"id")
    print("Student id :",id[0])


# def test_addTechSkills():
#     url = "http://thetestingworldapi.com/api/technicalskills/"+str(id[0])
#
#     # Read file content
#     f = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/DataDrivenTesting/TechSkills.json",'r')
#     fileinput = f.read()
#     json_request = json.loads(fileinput)
#
#
#     json_request['id'] = int(id[0])
#     json_request['st_id'] = int(id[0])
#     print("Student Technical details :",json_request)
#     response = requests.post(url,data=json_request)
#     print(response.text)
#     print(response.status_code)
#
#
# def test_addAddress_dtls():
#     url = "http://thetestingworldapi.com/api/addresses/"+str(id[0])
#
#     #Read file content
#     f = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/DataDrivenTesting/addressdtls.json")
#     fileinput = f.read()
#     json_request = json.loads(fileinput)
#
#     json_request['stId']=int(id[0])
#     print("Student address details :",json_request)
#     response = requests.post(url,data=json_request)
#     print(response.text)
#     print(response.status_code)
#
#
#
# def test_finalStudentDetails():
#     url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
#
#     response = requests.get(url)
#     print(response.text)
#     print(response.status_code)











