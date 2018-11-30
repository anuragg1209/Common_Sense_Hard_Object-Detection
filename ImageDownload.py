from bs4 import BeautifulSoup
from socket import socket
import requests
import urllib.error
import urllib.request
import http.cookiejar
import httplib2


import os

import json

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),"html.parser")


query = input("Road with pedestrian")# you can change the query for the image  here
print(query)
image_type="Country"
query= query.split()
query='+'.join(query)
print(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)
#add the directory for your image here
DIR="/Users/abidhapandey/Desktop/data_analysis/"+(query.split('+'))[0]+"/"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print("there are total" , len(ActualImages),"images")


###print images
for i , (img , Type) in enumerate( ActualImages):
        req = urllib.request.Request(img, headers= header)
        raw_img = urllib.request.urlopen(req).read()

        if not os.path.exists(DIR):
            os.mkdir(DIR)
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print(cntr)
        if len(Type)==0:
            f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
        else :
            f = open(DIR + image_type + "_"+ str(cntr)+"."+Type, 'wb')


        f.write(raw_img)
        f.close()

