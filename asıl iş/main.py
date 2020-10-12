import json , random
from os import chdir , getcwd

chdir('precius datas')

print(getcwd())

with open('cumatest.json',encoding = 'utf-8') as file:
    cuma_piece = json.load(file)
for x in range(1,2):
    print(random.choice(cuma_piece['söz']).strip(),random.choice(cuma_piece['kutlama']))