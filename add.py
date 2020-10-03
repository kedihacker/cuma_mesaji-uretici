import json 
from os import remove
yazılacaklar = {


}
try:   
    with open('cumayedek.json','a',encoding='utf8')as yedek:
        yedek.truncate(0)
        with open('cumatest.json','r',encoding='utf8')as asıl:
            backup = json.load(asıl)
        yedek.write(json.dumps(backup))
        yazılacaklar = backup
except:
    pass
print(type(yazılacaklar))

def bilgial(ad):
    if ad in yazılacaklar:
        print('girilen tür var!! parti naiy naniy')
        while True:
            print(ad)
            giriş = input('q hariç heryeş yazılacak q çıkış : ')
            if giriş == 'q':
                return True
                
            else:
                yazılacaklar[ad].append(giriş)
    else:
        giriş = input('Aradığın tür yok abicim. Ekleyeleimli yoksa gerimi atak Girdiğin {} : '.format(ad))
        if giriş == 'evet':
            yazılacaklar[ad] = []
            return True
        else:
            return False

while True:
    giriş = input('girilecek tür yazın : ')
    if giriş == 'q':
        break
    elif giriş == 'database drop':
        if input('gerçekten ise vallahi billahi yaz : ') == 'vallahi billahi':
            with open('cumatest.json','r+',encoding='utf8') as file:
                file.truncate(0)
            yazılacaklar = {}
            print('database droplandı inş yanlışlıkla yapmışşındır amin')
            break
    else:
        if True == bilgial(giriş):
            print('işlem tamamlandı')
        else:
            print('sikinti var')


with open('cumatest.json','r+',encoding='utf8') as file:
    file.truncate(0)
    
    
    writeorder = json.dumps(yazılacaklar)
    file.write(writeorder)

