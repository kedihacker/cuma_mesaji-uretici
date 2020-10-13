try:
    import sys
    import requests
    import PIL
    import os

    from bs4 import BeautifulSoup as bs
    from random import randint as random

except ImportError as err:
    print(f"Import Error in {sys.argv[0]}:\n{err}")
    sys.exit()

open("srcs.txt", "w").write("")
os.system("mkdir images")

url = "https://www.gettyimages.in/photos/rose?mediatype=photography&phrase=rose&sort=mostpopular"

r = requests.get(url)
soup = bs(r.content, "lxml")

image_src_list = list()
images = soup.findAll("img")

for image in images:
    if "src" in str(image):
        src = str(image).split("src=\"")[-1].split("\"")[0]
        if "https" in str(src):
            image_src_list.append(src)

for src in image_src_list:
    if src:
        open("srcs.txt", "a").write(f"{src}\n")

print(f"Fihished with ({len(image_src_list)}) images.")
print("Starting download..")

lines = open("srcs.txt", "r").readlines()
for url in lines:
    r = requests.get(url)

    open(f"images/{''.join([str(random(0, 9)) for n in range(9)])}.png", "wb").write(r.content)
    print(f"%{round(lines.index(url)/len(lines)*100, 2)}")