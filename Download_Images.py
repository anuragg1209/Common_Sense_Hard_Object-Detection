from bs4 import BeautifulSoup
from socket import socket
import requests
import urllib.error
import urllib.request
import http.cookiejar
import httplib2
import os
import json
import argparse

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),"html.parser")

def img_dwnld(soup,DIR,header):
    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print("there are total" , len(ActualImages),"images")
    #print images
    for i, (img, Type) in enumerate(ActualImages):
            req = urllib.request.Request(img, headers= header)
            raw_img = urllib.request.urlopen(req).read()

            if not os.path.exists(DIR):
                os.mkdir(DIR)
            counter = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            print(counter) #counting downloaded images
            if len(Type)==0:
                f = open(DIR + image_type + "_"+ str(counter)+".jpg", 'wb')
            else:
                f = open(DIR + image_type + "_"+ str(counter)+"."+Type, 'wb')
            f.write(raw_img)
            f.close()
if(__name__=='__main__'):
    parser = argparse.ArgumentParser(description='Code to download images',
                                     usage="\n\npython Image_Download.py"
                                           "\t --output_dir "
                                           "\t --download")
    parser.add_argument('--output_dir',
                        action='store',
                        dest='output_dir',
                        required=True,
                        help='Directory where downloaded images will be  stored')
    parser.add_argument('--download',
                        action='store',
                        required=True,
                        help='enter  name of the item to download its images')
    args = parser.parse_args()
    image_type = "test"
    query=f"{args.download}"
    query=query.split()
    query = '+'.join(query)
    DIR = f"{args.output_dir}" +"/"+ (query.split('+'))[0] + "/"
    url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
    print(f"Downloading images from: {url}")
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup=get_soup(url,header)
    img_dwnld(soup,DIR,header)
