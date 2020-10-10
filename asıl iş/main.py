import json , random
from os import chdir , getcwd

chdir('precius datas')

print(getcwd())

with open('cumatest.json',encoding = 'utf-8') as file:
    cuma_piece = json.load(file)
