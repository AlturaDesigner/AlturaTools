import requests

url = 'https://app.alturanft.com/api/external/item/image?apiKey=XXXX'
myobj = {'tokenId': 1, 
                'collectionId': '0x4ddee11d87a535ec71817b558d81bda24f4cac7b',
                'imageIndex': 1}

x = requests.post(url, data = myobj)

print(x.text)
print(x)
