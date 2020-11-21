#import json
#from base64 import b64encode
from Crypto.Cipher import ChaCha20
#from Crypto.Random import get_random_bytes
#from base64 import b64decode
import requests

url = 'http://192.168.1.21:8000'    # Server location (change to your server)

# Turning the hexadecimal values into bytes.
message = bytes.fromhex("61009c2cdb0b1326bdccfc689a7fb6dec1a6479af2bd4833c4b9b99fa09f634da3")
key = bytes.fromhex("56c358f80430fd6e3da571b06a4b301d26af980f08a509d288d13e70847ddcf4")
nonce = bytes.fromhex("564401756dd4574e")

cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(message)

r = requests.post(url + "/opdracht8", json={"bericht_ontcijferd": plaintext.decode('utf-8')})
result = r.text
print(result)
