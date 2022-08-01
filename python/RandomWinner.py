import requests
import json
import random
import datetime
from datetime import date
import schedule
import time
import pytz
from random import choices
import ftplib


players = [0, 1, 2, 3, 4, 5, 6]

winner = int(random.randint(199,299))

#update image
url = 'https://api.alturanft.com/api/v2/item/update_primary_image?apiKey=XXXX'
          myobj = {'tokenId': winner,
                          'address': '0x4ddee11d87a535ec71817b558d81bda24f4cac7b',
                          'imageIndex': 1} # Pick index number of image you have chosen when you uploaded files 
          x = requests.post(url, data = myobj)
          print("Winner image updated.")
      
#Then update property


url = 'https://api.alturanft.com/api/v2/item/update_property?apiKey=XXXX'
        myobj = {'tokenId':dobitnik,             'address': '0xf3b083f847b9b49af7e9a42b35e2ae9ebe5960df',
                        'propertyName': '1st Place',
                        'propertyValue': int(winner)}
