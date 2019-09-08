# importing google_images_download module
from google_images_download import google_images_download
import argparse
import shutil
import os
from os import path

# creating object
response = google_images_download.googleimagesdownload()

#search_queries=['Vehicles going uphill or downhill','Vehicles driving within speed limits']

def downloadimages(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 10,
                 "print_urls": False,
                 "size": "medium",
                 }   #"aspect_ratio": "panoramic"
    try:
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 10,
                     "print_urls": True,
                     "size": "medium"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass

def rename_file(folder): # Function to rename multiple files
    i = 1

    for filename in os.listdir("downloads/"+folder):
        dst = "test" + str(i) + ".jpg"
        src = "downloads/"+folder +"/"+ filename
        dst = "downloads/"+folder +"/"+ dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1

def move_files(folder): #moving all downloaded images to Images folder
    if not os.path.exists('static/Images'):
        os.mkdir('static/Images')
    img=[i for i in os.listdir(f"downloads/{folder}/")]
    for i in img:
        source=f'downloads/{folder}/{i}'
        dst="C:/Users/anurag/Downloads/darkflow-master/darkflow-master/sample_img/"
        shutil.copy(source,dst)
    for i in img:
        src=f'downloads/{folder}/{i}'
        shutil.move(src, 'static/Images')
    shutil.rmtree("downloads")

# Driver Code
if(__name__=='__main__'):
    parser = argparse.ArgumentParser(description='Code to download images from google',
                                     usage="\n\npython Image_Download.py"
                                           "\t --download")


    parser.add_argument('--download',
                        action='store',
                        required=True,
                        help='enter  name of the item to download its images')
    args = parser.parse_args()
    #for query in search_queries:
    downloadimages(args.download)
    rename_file(args.download)
    move_files(args.download)
    print()
