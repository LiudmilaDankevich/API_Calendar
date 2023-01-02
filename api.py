import requests
from requests.auth import HTTPBasicAuth



payload = {"PhoneNumber": "+375298858590"}
response = requests.post('https://dev.dsync.app:6443/api/Identity/getOTP', json=payload)
json_response = response.json()
otp = json_response["verify_token"]
print(response.text)
print(otp)


# data_1={"phone_number": "+375298858590", "verification_token": f"Bearer {otp}", "grant_type": "phone_number_token",
#            "client_id": "phone_number_authentication", "client_secret": "secret"}
#
# # auth_token=get_auth_token()
# headers = {"Content-Type": "application/x-www-form-urlencoded",
#            "Content-Length": "<calculated when request is sent>",
#            "Host": "<calculated when request is sent>",
#            "User-Agent": "PostmanRuntime/7.30.0",
#            "Accept": "*/*",
#            "Accept-Encoding": "gzip, deflate, br",
#            "Connection": "keep-alive" }
# response_1 = requests.post('https://dev.dsync.app:6443/connect/token', data=data_1, headers=headers)
# json_response_1 = response_1.json()
# print(response_1)

data_1={"phone_number": "+375298858590", "verification_token": {otp}, "grant_type": "phone_number_token",
           "client_id": "phone_number_authentication", "client_secret": "secret"}

# auth_token=get_auth_token()
headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
           "Content-Length": "98",
           "Host": "dev.dsync.app:6443",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
           "Accept": "application/json, text/plain, */*",
           "Accept-Encoding": "gzip, deflate, br",
           "Connection": "keep-alive" }
response_1 = requests.post('https://dev.dsync.app:6443/connect/token', data=data_1, headers=headers)
json_response_1 = response_1.json()
print(response_1.text)






