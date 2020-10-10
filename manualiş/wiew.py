import json
import os
os.chdir('precius datas')
with open('cumatest.json','r',encoding='utf8') as file:
    cuma = json.load(file)
for x in cuma['söz']:
    print(x)