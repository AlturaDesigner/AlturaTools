
import requests
import json
import schedule
import ftplib

response = requests.get('https://app.alturanft.com/api/external/item?apiKey=XXXX&collectionId=0xf3b083f847b9b49af7e9a42b35e2ae9ebe5960df')
        test = response.json()

        print(test)

        with open("data.json", "w") as outfile:
            json.dump(test, outfile)
            print("Data Ready.")
            
token = test['items'][vario]['tokenId']
print(token)

url = 'https://api.alturanft.com/api/v2/item/update_property?apiKey=XXXX'
                myobj = {'tokenId':token,             'address': '0xf3b083f847b9b49af7e9a42b35e2ae9ebe5960df',
                                'propertyValue': int(token) + 1}


                x = requests.post(url, data = myobj)
