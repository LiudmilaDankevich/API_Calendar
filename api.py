import requests
from requests.auth import HTTPBasicAuth



payload = {"PhoneNumber": "+375298858590"}
response = requests.post('https://dev.dsync.app:6443/api/Identity/getOTP', json=payload)
json_response = response.json()
otp = json_response["verify_token"]
print(response.text)
print(otp)

data_1={"phone_number": "+375298858590", "verification_token": {otp}, "grant_type": "phone_number_token",
           "client_id": "phone_number_authentication", "client_secret": "secret"}
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
access_token = json_response_1["access_token"]
refresh_token = json_response_1["refresh_token"]
print("access_token = ", access_token)

payload_2 = {"LastName":"Dankev","FirstName":"Milla"}
headers = {"Content-Type": "application/json",
           "Content-Length": "55",
           "Host": "dev.dsync.app:5443",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
           "Accept": "*/*",
           "Authorization": {access_token},
           "Accept-Encoding": "gzip, deflate, br",
           "Connection": "keep-alive" }
response_2 = requests.post('https://dev.dsync.app:5443/api/Profile/save', json=payload_2)
# json_response = response_2.json()
print(response_2)







