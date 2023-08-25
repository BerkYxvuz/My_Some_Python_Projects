import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

# result = df.groupby("Departman")

# belirli bir grubu yazdırma
# for name, group in df.groupby("Departman"):
#     print(f'{name} {group}')

# Kolonun içinden belli bir ismi alma
# örneğin semtler den kadıköy

# result = df.groupby("Semt").get_group("Kadıköy")
#
# result = df.groupby("Departman").sum() # tüm yaşları ve maaşları toplar
#
# result = df.groupby("Departman").mean() # tümünün ortalmasını alır

# result = df.groupby("Departman")["Maaş"].mean() # Maaş ortalamasını alır
#
# result = df.groupby("Semt")["Yaş"].mean() # Semte göre yaş ortalmasını alır
#
# result = df.groupby("Semt")["Çalışan"].count() # Semte göre çalışan sayısını alır.
#
# result = df.groupby("Departman")["Yaş"].max() # Departmana göre en büyük yaşı alır

# result = df.groupby("Departman")["Maaş"].max()["Muhasebe"] # Departmana göre en büyük maaşı alır ve sadece nuhasebeyi alır

result = df.groupby("Departman").agg(np.mean) # departmana göre ortalama alır.

print(result)