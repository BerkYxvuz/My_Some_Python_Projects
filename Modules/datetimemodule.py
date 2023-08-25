from datetime import datetime
from datetime import timedelta

#Şuan ki zamanı alma

suan = datetime.now()
# print(suan)

#suan değişkeninden sadece gün ay gibi verileri tek tek almak.

# print(suan.day)
# print(suan.month)
# print(suan.year)

#daha açıklayıcı datetime.now koduyla eş değer bir kodumuz var

# result = datetime.ctime(suan)
# print(result)

#Günleri ayları teker teker seçmenin daha esnek bir yolu
# result = datetime.strftime(suan, '%Y') #yılı aldık
# result = datetime.strftime(suan, '%X') #saati aldık
# result = datetime.strftime(suan, '%D') #Gün'ü aldık
# result = datetime.strftime(suan, '%A') #Gün'ü string aldık
# result = datetime.strftime(suan, '%B') #Ay'ı string aldık
# #toplu da kullanılabilir
# result = datetime.strftime(suan, '%Y %B %A')
# print(result)

#Burada bilgiler dt de kullanılan kodda soldan sağa %A gibi belirterek stringi gerçek tarihe çeviriyoruz.

# t = '15 April 2019 hour 11:00:15'
# dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
# artık istediğimizi seçebiliriz
# dtyil = dt.year #gibi
# print(dt)

#Daha başka bilgiler belli bir tarihi saniyeye dönüştürme

birthday = datetime(1938, 11, 10, 9, 5, 0)

# result = datetime.timestamp(birthday) # datetime to saniye
# result = datetime.fromtimestamp(result)  # saniye to datetime

result = datetime.fromtimestamp(0) #bilgisayarların zamanı tuttuğu en erken tarih

# result = suan - result #timedelta
# result = result.days

# tarihe zaman ekleme veya çıkarma

result = suan - timedelta(days=366)

print(result)