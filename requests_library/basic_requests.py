import requests
import json

def get_request():
    base_url = "https://reqres.in"
    resource = "/api/users"
    rest_url = base_url + resource
    response = requests.get(rest_url)
    print(type(response.content))
    # convert bytes to string
    response_string = response.content.decode("utf-8")
    print(f"Now utf-8 converted the response to: {type(response_string)}")
    # change type to dict
    response_dict = json.loads(response_string)
    print(f"after using loads function from json, type of response is: {type(response_dict)}")
    print(response_dict)

'''
How to create request with query parameters
How to get Dictionary response 
How to track any specific response values
'''
def get_with_params():
    base_url = "https://reqres.in"
    resource = "/api/users"

    # How to create request with query parameters
    key_params = {"page":2}
    rest_url = base_url + resource
    response = requests.get(rest_url,key_params)
    print(type(response.json()))

    # How to get Dictionary response 
    response_dict = response.json()
    print(response_dict)
    
    # How to track any specific response values
    data_records = response_dict["data"]
    for item in data_records:
        if item["id"] == 7:
            print(item["email"])

get_request()
get_with_params()
