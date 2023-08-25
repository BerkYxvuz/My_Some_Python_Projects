import requests
import json

api_url = requests.get("https://api.genelpara.com/embed/para-birimleri.json")

dovizler = json.loads(api_url.text)

alinan_doviz = input('Alınacak Döviz: ')

result = float(dovizler[alinan_doviz]['alis'])

satilacak_try = int(input('Satılacak TRY Miktarı: '))

alinanpara = satilacak_try / result

sonuc = round(alinanpara, 2)

print(f'{alinan_doviz}: ' + str(sonuc))