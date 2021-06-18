from json import dumps
from base64 import b64encode

def encrypt(data):
    key = 'qw8J'
    ordinals = []

    for index, ch in enumerate(data):
        ordinals.append(ord(ch) ^ ord(key[index % len(key)]))

    return ''.join([chr(o) for o in ordinals])

data = {
    "showpassword": "yes",
    "bgcolor": "#ffffff"
}

json = dumps(data)
encrypted_json = encrypt(json)
based_data = b64encode(bytes(encrypted_json, 'utf-8'))

print(based_data.decode('utf-8'))
