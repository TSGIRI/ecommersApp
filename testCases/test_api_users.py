import uuid

import pytest

from utilities.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    endpoint = "users"
    response = api_client.get(endpoint)

    statuscode = response.status_code
    response_json = response.json()

    print("statuscode : ", statuscode)
    print("response_json : ", response_json)

    assert statuscode == 200
    assert len(response_json) > 0


def test_create_user(api_client):
    endpoint = "users"
    request_payload = {
        "name": "giri babu",
        "username": "qa user1",
        "email": "test123#gmail.com"
    }
    response = api_client.post(endpoint, request_payload)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)
    assert statuscode == 201
    assert response_json['name'] == "giri babu"


def test_update_user(api_client):
    endpoint = "users/1"
    request_payload = {
        "name": "giri babu t",
        "username": "qa user1",
        "email": "test123#gmail.com"
    }
    response = api_client.put(endpoint, request_payload)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)
    assert statuscode == 200

def test_delete_user(api_client):
    endpoint = "users/1"

    response = api_client.delete(endpoint)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)
    assert statuscode == 200

def test_create_user_jsonfile(api_client, load_user_data):
    endpoint = "users"
    # request_payload = {
    #     "name": "giri babu",
    #     "username": "qa user1",
    #     "email": "test123#gmail.com"
    # }

    user_data = load_user_data["new_user"]  # ✅ dictionary access, that's why we need to use []
    print(user_data)

    unique_email = f"{uuid.uuid4().hex[:8]}@example.com"   # Generate a unique email
    user_data['email'] = unique_email

    response = api_client.post(endpoint, user_data)
    statuscode = response.status_code
    response_json = response.json()
    print("statuscode : ", statuscode)
    print("response_json : ", response_json)
    assert statuscode == 201


# pytest -s -v testCases/test_api_users.py  (if we run html report will be generated in the root folder)
# pytest -s -v testCases/test_api_users.py --html=Reports\api_test_report.html