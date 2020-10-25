import requests
import json
import pytest
import jsonpath


def test_createStudent():
    url = "http://thetestingworldapi.com/api/studentsDetails"

    # Read file content
    file = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/RestApiUsing_PyTest/JsonTestData.json")
    fileinput = file.read()

    # convert to json format
    json_request = json.loads(fileinput)

    # Post the equest
    response = requests.post(url,data=json_request)
    print("Response code :",response.status_code)
    print(response.text)

def test_fetchStudent():
    url = "http://thetestingworldapi.com/api/studentsDetails/40053"

    response = requests.get(url)
    print(response.text)
    json_response = json.loads(response.text)
    print(json_response)

    id = jsonpath.jsonpath(json_response,"data.id")
    print(id[0])
    assert id[0]==40053


def test_updateStudentDetails():
    url = "http://thetestingworldapi.com/api/studentsDetails/40053"

    file = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/RestApiUsing_PyTest/JsonUpdateTestData.json",'r')
    fileinput = file.read()

    json_request = json.loads(fileinput)

    response = requests.put(url,data=json_request)
    json_response = json.loads(response.text)
    print(json_response)
    msg = jsonpath.jsonpath(json_response,"msg")
    print("Message :",msg)
    assert msg.__contains__('update  data success')


def test_deleteStudentDetails():
    url = "http://thetestingworldapi.com/api/studentsDetails/40053"

    response = requests.delete(url)
    print(response.text)

    json_response = json.loads(response.text)
    msg = jsonpath.jsonpath(json_response,"msg")
    assert msg.__contains__('Delete  data success')
