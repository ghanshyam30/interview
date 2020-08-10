import requests
import json

def post_basic():
    base_url = "https://reqres.in"
    resource = "/api/users"

    api_url = base_url + resource

    header_params = {"Content-Type":"application/json"}
    payload = {"name":"Dummy User","job":"leader"}
    
    response = requests.post(api_url,data=payload)
    print(response.status_code)
    print("Resp: ",response.json())
    print("If ok:",response.ok)
    print("Reqest object:",type(response.request.url))
    print("Reqest object headers:",type(response.request.headers))
    headers_received = response.request.headers
    headers_dict = dict(headers_received)
    print("Headers dict:",headers_dict)
    print("Shold be keep-alive :",headers_dict['Connection'])
    assert headers_dict['Connection'] == 'keep-alive'
    print("Reqest object body:",type(response.request.body))

post_basic()