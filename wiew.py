import json

with open('cumatest.json','r') as file:
    cuma = json.load(file)

print(cuma)