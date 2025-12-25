
import requests

# GET : fetching the data from the server
# POST : post is nothing but creating new data in the server
# PUT : updating the existing data in the server as well as creating new data in the server
# DELETE : deleting the existing data in the server

def get_api():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    response = requests.get(url)

    statuscode = response.status_code
    get_content = response.content
    req_headers = response.headers

    print("statuscode : ",statuscode)
    print("content : ", get_content)
    print("headers : ", req_headers)

    print("response_json : ",response.json())
    assert statuscode == 200
    print("api is working fine")



def get_api_petID(petID):
    #petID = int(input("Enter petID to fetch details: "))

    url = f"https://petstore.swagger.io/v2/pet/{petID}"
    response = requests.get(url)

    statuscode = response.status_code
    get_content = response.content
    req_headers = response.headers
    response_json = response.json()

    print("statuscode : ",statuscode)
    print("content : ", get_content)
    print("headers : ", req_headers)
    print("response_json : ", response_json)

    assert statuscode == 200
    assert response_json['id'] == petID

    print("api is working fine for petID:", petID)


#get_api()
#get_api_petID(5)

# API with parameters:  parameters are sent in the URL to filter the data, after ? symbol
def get_api_parameters():

    url = "https://gorest.co.in/public/v2/users?page=1&per_page=3"

    params = {
        "page": 1,
        "per_page": 3
    }
    response = requests.get(url, params=params)

    statuscode = response.status_code
    response_json = response.json()
    get_content = response.content
    req_headers = response.headers

    print("statuscode : ",statuscode)
    print("response_json : ", response_json)
    print("content : ", get_content)
    print("headers : ", req_headers)

    assert statuscode == 200

    print("api with parameters is working fine")

get_api_parameters()

