import urllib.request
import requests
import random

current_url = 'http://xkcd.com/info.0.json'
resp = requests.get(current_url)
current_num = int(resp.json()['num'])

while(True):
    rd = random.randint(1, current_num)
    url = 'http://xkcd.com/'+str(rd)+'/info.0.json'
    resp = requests.get(url)

    urllib.request.urlretrieve(resp.json()['img'], resp.json()['title']+'.png')
    print('done!!')
    k = input('press 1 to download another one, 0 to quit: ')

    if int(k) is 0:
        break

print('Thanks for trying out xkcd-Downloader')

