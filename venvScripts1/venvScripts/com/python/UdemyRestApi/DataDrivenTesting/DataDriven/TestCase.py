import requests
import json
import jsonpath
import openpyxl
from venvScripts.com.python.UdemyRestApi.DataDrivenTesting.DataDriven import Library

# API url
url = "http://thetestingworldapi.com/api/studentsDetails"

ob = Library.Demo("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/DataDrivenTesting/JsonTestData.xlsx","Sheet1")
rowncnt = ob.getRowCnt()
keylist = ob.getKeyList()

# Read json file
file = open("C:/Kiran Kumar SY/Python/venvScripts1/venvScripts/com/python/UdemyRestApi/DataDrivenTesting/JsonTestData.json",'r')
fileinput = file.read()
json_request = json.loads(fileinput)

for i in range(1,rowncnt+1):
    updatedrequest = ob.updatejsonrequest(i,json_request,"Sheet1",keylist)
    response = requests.post(url,updatedrequest)
    print(response.status_code)
    print(response.text)
    assert response.status_code==201