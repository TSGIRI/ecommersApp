import requests


def get_api():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/12"
    response = requests.get(url)

    statuscode = response.status_code
    response_json = response.json()

    print("statuscode : ",statuscode)
    print("response_json : ", response_json)

    assert statuscode == 200


def put_api():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/12"

    header = {
        "Accept": "text/plain",
        "Content-Type": "application/json"
    }

    request_payload = {
        "id": 15,
        "title": "seshagiri api testing demo - updated 15",
        "dueDate": "2025-12-01T10:00:00.000Z",
        "completed": True
    }

    response = requests.put(url, headers=header, json=request_payload)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)

    assert statuscode == 200
    assert response_json['id'] == 15
    assert response_json['title'] == "seshagiri api testing demo - updated 15"

    content = response.content
    print("content : ", content)
    req_headers = response.headers
    print("headers : ", req_headers)



put_api()
#get_api()