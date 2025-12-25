import requests
import json

# GET : fetching the data from the server
# POST : post is nothing but creating new data in the server
# PUT : updating the existing data in the server as well as creating new data in the server
# DELETE : deleting the existing data in the server

# Note: boolean values in Python are represented as 'True' and 'False' (with uppercase first letters), in JSON file they are 'true' and 'false' (all lowercase).

# ---------------- API testing without token ----------------
def post_api():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    header = {
        "Accept": "text/plain",
        "Content-Type": "application/json"
    }

    request_payload = {
        "id": 154,
        "title": "seshagiri api testing demo",
        "dueDate": "2025-11-23T04:16:47.926Z",
        "completed": True
    }

    response = requests.post(url, headers=header, json=request_payload)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ",statuscode)
    print("response_json : ", response_json)

    assert statuscode == 200
    assert response_json['id'] == 154

    content = response.content
    print("content : ", content)
    req_headers = response.headers
    print("headers : ", req_headers)

#post_api()

# ---------------API testing with token ----------------
def post_api_token():
    url = "https://gorest.co.in/public/v2/users"

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer b5830456aa49b8493fabc4c957b7f558429a073988b4931c5f53c63bb1b5d7f0"
    }

    request_payload = {
        "name": "giri babu 5",
        "email": "giri_babu_5@zemlak.example",
        "gender": "male",
        "status": "active"
    }

    response = requests.post(url, headers=header, json=request_payload)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)

    assert statuscode == 201
    user_ID = response_json['id']
    print("Created user ID : ", user_ID)
    return user_ID

def get_api_token(userID):
    url = f"https://gorest.co.in/public/v2/users/{userID}"

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer b5830456aa49b8493fabc4c957b7f558429a073988b4931c5f53c63bb1b5d7f0"
    }
    response = requests.get(url, headers=header)
    statuscode = response.status_code
    response_json = response.json()

    print("statuscode : ", statuscode)
    print("response_json : ", response_json)

    assert statuscode == 200
    assert response_json['id'] == userID

    print("api is working fine for userID:", userID)

# userID = post_api_token()
# get_api_token(userID)


# ------------ Load the data(payload) from Json file ----------------

def post_api_jsonfile():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    header = {
        "Accept": "text/plain",
        "Content-Type": "application/json"
    }

    json_file = open("./users.json")
    request_payload = json.load(json_file)

    # request_payload = {
    #     "id": 154,
    #     "title": "seshagiri api testing demo",
    #     "dueDate": "2025-11-23T04:16:47.926Z",
    #     "completed": True
    # }

    response = requests.post(url, headers=header, json=request_payload)
    #response = requests.post(url, headers=header, data=json.dumps(request_payload))

    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)

    assert statuscode == 200
    assert response_json['id'] == 155

    content = response.content
    print("content : ", content)
    req_headers = response.headers
    print("headers : ", req_headers)


post_api_jsonfile()


