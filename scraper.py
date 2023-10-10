import requests
import os.path
import os
import json
from dotenv import load_dotenv

load_dotenv()

preUrl ='https://nhentai.net/api/gallery/'
print("UID(6 digit code):")
UID = str(input())
url= preUrl+UID

# getting values from .env
headers = os.getenv('headers')
imgHeader = os.getenv('imgHeader')

request = requests.get(url, headers=headers)

rdict = json.loads(request.text)

GID = rdict['media_id']
np = rdict['num_pages']

imgFormat = (rdict['images']['pages'][1]['t'])

#get image format, set up extension
ext = ''
if (imgFormat == 'p'):
    ext = '.png'
elif (imgFormat == 'j'):
    ext = '.jpg'

for x in range(np):
    tUrl = 'https://i.nhentai.net/galleries/' + GID + '/' + str(x+1) + ext 
    print(tUrl)
    import pathlib
    img_data = requests.get(tUrl, headers=imgHeader).content
    Name = str(x) + ext
    with open(Name, 'wb') as handler:
        handler.write(img_data)
