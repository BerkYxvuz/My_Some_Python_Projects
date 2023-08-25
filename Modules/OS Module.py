import os

# result = os.name #bulunduğun dosyanın konumu


# os.chdir('C:\\Users\\beek6\OneDrive\Masaüstü') #bu şekilde istediğimiz yere konumu yönlendirebiliriz

#eğer os.chdir('..') kullanırsak bulunduğumuz konmunun bir gerisine gider
#ve arka arkaya os.chdir(..) kullanırsak onun üstüne tekrar geriye gider
#veya direkt os.chdir('../..') yazabiliriz


# os.mkdir("Test") #bu kodu kullanarak dosya oluşturabiliriz (üstte belirttiğimiz konumda) eğer belirtmediysek şuanda bulunan dosyaya
#yani Modules klasörüne atar

#Dosya isim değiştirme
# os.rename("Klasör Adı","Yeni Klasör Adı")

# Dosya silme
# os.rmdir("klasör")
# os.removedirs("klasör/klasör")

#istediğimiz dizini önceden belirip oluşturmak yerine şöyle yapabiliriz
# os.makedirs('C:\\Users\\beek6\OneDrive\Masaüstü\Test/YeniKlasör') diyerek oluşturabilirz.

#listeleme

#result = os.listdir() #kullanarak belirttiğimiz konumdaki klasörleri listeler

#istediğimiz uzantıdaki tüm dosyaları listelemeyi şöyle yapabiliriz.

#for dosya in os.listdir():
#   if dosya.endswith('.py'):
#       print(dosya)

#belirtilen dizinden çeşitli bilgiler alma en son ne zaman kullanıldı kaç bayt vs.

#en son kullanılan zamanı saniyeden normal tarihe değiştirelim

# import datetime

# result = os.stat("datetimemodule.py")

# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # son değiştirilme tarihi

# print(result)

#uygulama açmak

# os.system("notepad.exe")

#************ path *************

# os.path.abspath("OS Module.py") #dosyanın konumun alıyoruz

# os.path.dirname("C:\\Users\\beek6\PycharmProjects\Projects\AllProjects\Modules\OS Module.py")#dizin ismini alıyruz

# #birlikte de kullanabiliriz

# test = os.path.dirname(os.path.abspath("OS Module.py"))

# aradığımız dosya,klasör belirtilen dizinde var mı diye kontrol etmek

# test = os.path.exists("C:\\Users\\beek6\PycharmProjects\Projects\AllProjects\Modules\OS Module.py")

# Dizin mi diye kontrol etme

# test = os.path.isdir("C:\\Users\\beek6\PycharmProjects\Projects\AllProjects\Modules\OS Module.py")

# Klasör mü diye kontrol etme

# test = os.path.isfile("C:\\Users\\beek6\PycharmProjects\Projects\AllProjects\Modules\OS Module.py")

# ayrı dizinleri birleştirme

# test = os.path.join("C:\\","Test")

# dizinleri bölme

# test = os.path.split("C:\\")

# uzanti ve ismi bölme

# test = os.path.splitext("OS Module.py")

# print(test)