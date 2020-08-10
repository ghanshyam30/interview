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

def get_with_params():
    base_url = "https://reqres.in"
    resource = "/api/users"
    key_params = {"page":2}
    rest_url = base_url + resource
    response = requests.get(rest_url,key_params)
    print(type(response.content))
    # convert bytes to string
    response_string = response.content.decode("utf-8")
    print(f"Now utf-8 converted the response to: {type(response_string)}")
    # change type to dict
    response_dict = json.loads(response_string)
    print(f"after using loads function from json, type of response is: {type(response_dict)}")
    print(response_dict)


# get_request()
# get_with_params()
