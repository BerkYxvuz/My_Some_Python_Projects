import math


def OrtHesapla(satir):
    global kimlikbilgileri,ortalama
    ortalama = 0
    satir = satir[:-1]
    liste = satir.split(':')
    kimlikbilgileri = liste[0]
    notlar = liste[1]
    notlar = notlar.split(',')
    for i in notlar:
        ortalama += int(i)
    ortalama = ortalama/3
    ortalama = math.floor(ortalama)
    if ortalama >= 75 and ortalama < 85:
        print(f'Sayın {kimlikbilgileri} {ortalama} Ortalama İle Teşekkür Aldınız')
    elif ortalama >= 85:
        print(f'Sayın {kimlikbilgileri} {ortalama} Ortalama İle Takdir Aldınız')
    else:
        print(f'Sayın {kimlikbilgileri} {ortalama} Ortalama İle Belge Alamadınız')


def NotOku():
    with open("sinif_notlari.txt", "r", encoding="utf-8") as file:
        for i in file:
            OrtHesapla(i)
def NotKaydet():
    with open('sinif_notlari.txt', 'r', encoding='utf-8') as file:
        fielz = open('sinif_ortalamalari.txt', 'w', encoding='utf-8')
        for x in file:
            x = x[:-1]
            splitter = x.split(':')
            isim = splitter[0]
            nots = splitter[1]
            nots = nots.split(',')
            not1 = nots[0]
            not2 = nots[1]
            not3 = nots[2]
            hesaplanan = 0
            hesaplanan = int(not1) + int(not2) + int(not3)
            hesaplanan /= 3
            hesaplanan = math.floor(hesaplanan)

            fielz.write(f'{isim}: {hesaplanan}\n')
def NotGir():
    ad = str(input("Ad: "))
    soyad = str(input("Soyad: "))
    n1 = str(input("Not 1: "))
    n2 = str(input("Not 2: "))
    n3 = str(input("Not 3: "))
    with open("sinif_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + n1 + ',' + n2 + ',' + n3 + "\n")

while True:
    islem = input('1- Ortalama Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\nİşlem Seç: ')

    if islem == '1':
        NotOku()
    elif islem == '2':
        NotGir()
    elif islem == '3':
        NotKaydet()
    else:
        break