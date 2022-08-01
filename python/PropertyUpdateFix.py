import requests
url = 'https://app.alturanft.com/api/external/item/property?apiKey=XXXX'
myobj = {'tokenId':1,             'collectionId': '0x4ddee11d87a535ec71817b558d81bda24f4cac7b',
                'propertyName': 'NameHere',
                'propertyValue': 'ValueHere'}

x = requests.post(url, data = myobj)

print(x.text)
print(x)
