import pytest
import requests


def test_get_request():
    # url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    url ="https://gorest.co.in/public/v2/users?status=active&gender=male"

    header = {
        "Content_Type": "application/json"
    }

    response = requests.get(url, headers=header)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)
    assert statuscode == 200
    #print("response_text : ",  response.text)


