import json 
from os import remove
with open('cumayedek.json','a')as yedek:
    yedek.truncate(0)
    with open('cumatest.json','r')as asıl:
        backup = asıl.read()
    yedek.write(backup)

while True:
    break

with open('cumatest.json','r+') as file:
    file.truncate(0)
    
    
    writeorder = json.dumps(yazılacaklar)
    file.write(writeorder)

