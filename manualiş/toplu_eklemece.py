import json
içerik = {}
with open('cumatest.json','r',encoding='utf8') as file:
    içerik = json.load(file)

with open('imece/test.txt','a+',encoding='utf8')as file:
    for x in içerik['söz']:
        file.write(x+'\n')
        print(x)