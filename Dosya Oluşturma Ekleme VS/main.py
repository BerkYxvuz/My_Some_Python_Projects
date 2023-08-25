#Dosya oluşturmak ve açmak için open() fonksiyonu kullanılır.
#Kullanımı: open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_modu ==> dosyayı hangi amaçla açtığınızı belirtir.

# "w": (Write) Yazma modu. Dosyayı konumda oluşturur.
# "a": (Append) Ekleme modu.Dosyayı konumda oluşturur.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# file.read() Parantez içerisinde bir değer yoksa tüm dosyayı okur fakat örneğin 5 girilirse 5 harfi metinden okur.
# file.readline() İlk satırı okur.
# Detay! Python'a her okuma komutu verdiğinde eğer dosyayı baştan açmamışsan kaldığı yerden devam ederek okur.
SinifSayaci = 0
def SinifOlustur():
    global SinifSayaci,tumsiniflar
    try:
        open(f'Sınıf{SinifSayaci}', 'x', encoding='utf-8')
    except:
        print("Bu Sınıf Zaten Var")
    SinifSayaci += 1
SinifOlustur()
def OgrenciEkle(x,y):
    global tumsiniflar
    try:
        file = open(f'Sınıf{y}', "a", encoding='utf-8')
        file.write(f"{x}\n")
        file.close()
    except Exception as ex:
        print(ex)
    finally:
        print(f"Öğrenci Belirttiğiniz Sınıf{y}'a Eklendi.")
#Öğrenci Eklemek İçin X yerine isim ve soyisimi Y yerine sınıfını yazınız.
OgrenciEkle(str(input("Öğrencinin İsmi Ve Soyismini Giriniz: ")), int(input("Sınıf Numarasını Giriniz: ")))