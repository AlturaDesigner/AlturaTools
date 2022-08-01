import requests

url = 'https://api.alturanft.com/api/v2/item/update_primary_image?apiKey=XXXX' # Replace XXXX With Api key from Altura Developer portal https://developer.alturanft.com/
myobj = {'tokenId': 1, 
                'address': '0x4ddee11d87a535ec71817b558d81bda24f4cac7b', # Replace with address of your collection
                'imageIndex': 1} # image index  starts with 0

x = requests.post(url, data = myobj)

print(x.text)
print(x)
