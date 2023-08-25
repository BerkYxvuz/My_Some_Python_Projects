#Liste içinden sadece sayı olan verileri almak.
liste = ["15","30","25","AB","SD","1","1T","2U"]
def ListControl(list):
    for x in liste:
        try:
            sonuc = int(x)
            print(sonuc)
        except ValueError:
            continue
#ListControl(liste)

#Kullanıcı 'q' değerini girmediği sürece girilen inputun sayı olup olmadığını kontrol eden program.
def SayiMiDegilMi():
    x = None
    while x != 'q':
        x = input('Değer Giriniz: ')
        try:
            sayi = int(x)
            print(f'{sayi} Geçerli Bir Sayı Değeri Girildi.')
        except:
            print(f'< {x} > Geçerli Bir Sayı Değeri Değil!')

#SayiMiDegilMi() Fonksiyon Başlatma

#Girilen Şifrede Türkçe Karakter Var mı Kontrol Eden Fonksiyon.
def TurkishWordHunter():
    import re
    gecerlimi = False
    while gecerlimi == False:
        password = input('Şifrenizi Giriniz: ')
        if not re.search("[ıİşŞçÇöÖüÜğĞ]", password):
            print("Şifre Geçerli.")
            gecerlimi = True
        else:
            print("Şifre Türkçe Karakter İçeriyor Bu Yüzden Geçersiz.")
            gecerlimi = False
#TurkishWordHunter()

def FaktoriyelHesapla(x):
    x = int(x)
    if x < 0:
        raise ValueError('Değer Negatif Olmamalı!')
    result = 1
    for i in range(1, x+1):
        result *= i
    print(result)
#FaktoriyelHesapla()

#Liste içinden faktöriyel olabilecek sayıları bul ve faktöriyellerini hesapla.
SayiListesi = [1,3,7,8,"10A","4"]
def ListedenFakHesapla(z):
    for i in z:
        try:
            FaktoriyelHesapla(i)
            print(i)
        except:
            print(f'{i} Değeri Faktöriyele Dönüştürülemedi.')
            continue
ListedenFakHesapla(SayiListesi)