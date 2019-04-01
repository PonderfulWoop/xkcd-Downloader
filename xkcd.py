import urllib.request
import requests
import random

current_url = 'http://xkcd.com/info.0.json'
resp = requests.get(current_url)
current_num = int(resp.json()['num'])

ip = input("Enter number of comics to download : ")
k = 0
while(k < int(ip)):
    rd = random.randint(1, current_num)
    url = 'http://xkcd.com/'+str(rd)+'/info.0.json'
    resp = requests.get(url)
    print('Downloading comic', k)
    urllib.request.urlretrieve(resp.json()['img'], resp.json()['title']+'.png')
    print('Done')
    k = k + 1

print('Thanks for trying out xkcd-Downloader')

