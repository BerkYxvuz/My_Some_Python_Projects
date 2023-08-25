import numpy as np
'''
result = np.array([1, 3, 5 ,7 ,9])
result = np.arange(1,10) # 1 den 9'a kadar yazdırır.
result = np.arange(10,100,3) # 3 er 3 er artar
result = np.zeros(10) # 10 tane sıfır üretir floattır
result = np.ones(10) # 10 tane bir gelir floattır
result = np.linspace(0,100,5) # 0 dan 100 e kadar 5 e böler yani 25,50,75,100 olr
result = np.linspace(0,5,5) # 0 dan 5 e kadar 5 e böler
result = np.random.randint(0,10) # 0 ile 9 arasında bir sayı üretir
result = np.random.randint(20) # 19 a kadar herhangi bir sayı üretir
result = np.random.randint(1,10,3) # 3 tane sayı üretir
result = np.random.rand(5) # 0 ile 1 arasında 5 tane sayı üretir
result = np.random.randn(5) # 0 il 1 arasında negatif sayılarda üretir

np_array = np.arange(50)
np_multi = np_array.reshape(5, 10) # 5 e 10 luk bir matris oluşturur
print(np_multi.sum(axis=1)) # satırları toplar
'''
'''
rnd_numbers = np.random.randint(1,100,10)
result = rnd_numbers.max() # en büyük sayıyı alır
result = rnd_numbers.min() # en küçük sayıyı alır
result = rnd_numbers.mean() # Bütün sayıların ortalamasını alır
result = rnd_numbers.argmax() # En büyük sayının indexini alır
result = rnd_numbers.argmin() # En küçük sayının indexini alır
'''