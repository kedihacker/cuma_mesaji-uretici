import json
import random
from os import chdir , getcwd

chdir('precius datas')

print(getcwd())

with open('cumatest.json',encoding = 'utf-8') as file:
    cuma_piece = json.load(file)

def get_pieces (area,number): # get specified number of random out of given area
    geri = []
    for i in range(0,number):
        geri.append(random.choice(cuma_piece[area]))
    return geri

def get_piece (area):# get a ramdom piece
    try:
        lol = random.choice(cuma_piece[area])
    except:
        return False
    else:
        return lol
# get what areas avaiable
def get_areas ():# get what areas avaiable
    # print(cuma_piece.keys())
    return list(cuma_piece.keys())
