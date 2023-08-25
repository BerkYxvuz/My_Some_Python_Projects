import pandas as pd
import numpy as np

# data
numbers = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']
scaler = 5
dict = {'a':10, 'b':20, 'c':30, 'd':40}
random_numbers = np.random.randint(10, 100, 6)

# pandas_series = pd.Series(scaler, [0, 1, 2, 3]) # verdiğimiz index kadar 5 yazar.
# pandas_series = pd.Series(numbers, ["a", "b", "c", "d"]) # numaraların indexleri a b c d oldu.
# pandas_series = pd.Series(dict) # dict de zaten indexi belirlenmiş şekilde veriler gelir.
# pandas_series = pd.Series(random_numbers) # dict de zaten indexi belirlenmiş şekilde veriler gelir.
pandas_series = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"]) # numaraların indexleri a b c d oldu.

# result = pandas_series[0]
# result = pandas_series[-1] # son eleman
# result = pandas_series[:2] # ilk iki eleman
# result = pandas_series[-2:] # son iki eleman
# result = pandas_series['a'] # a indexi gelir
# # result = pandas_series[['a', 'c']] # a ve c indexi gelir
# result = pandas_series[['a', 'c', 'e']] # a ve c indexi gelir e NaN yani hiç anlamı gelir.
# result = pandas_series.ndim # kaç boyutlu olduğunu kontrol eder
# result = pandas_series.dtype # data tipini kontrol eder
# result = pandas_series.shape # kaç x kaç olduğunu söyler
# result = pandas_series.sum() # elemanların toplamı.
# result = pandas_series.max() # en büyük değer gelir
# result = pandas_series.min() # en küçük değer gelir
# result = pandas_series + pandas_series # matematiksel işlemler de yapılır numpy da olduğu gibi
# result = np.sqrt(pandas_series)
# result = pandas_series >= 50


# print(pandas_series)
# print(result)

opel2018 = pd.Series([20, 30, 40, 10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["astra", "corsa", "grandland", "insignia"])

total = opel2018 + opel2019

# print(total["astra"]) # tek model çekilebilir
# print(total) #Burada NaN bilgi döner çünkü mokka ve grandland aynı olmayan değerlerdir