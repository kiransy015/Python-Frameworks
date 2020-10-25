import requests
import json
import jsonpath
from requests.auth import HTTPBasicAuth

def test_basicAutentication():
    url = 'https://api.github.com/user'
    response = requests.get(url,auth=HTTPBasicAuth('kiransy015','ctyrkksy@9873015171'))
    print(response.status_code)
    print(response.text)