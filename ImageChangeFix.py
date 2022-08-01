import requests

url = 'https://api.alturanft.com/api/v2/item/update_primary_image?apiKey=XXXX'
myobj = {'tokenId': 1, 
                'address': '0x4ddee11d87a535ec71817b558d81bda24f4cac7b',
                'imageIndex': 1}

x = requests.post(url, data = myobj)

print(x.text)
print(x)
