import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[5]
result = numbers[-1]# en sonuncuyu alır.
result = numbers[0:3]# 0 ile 3 arasındakini alır.

numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])
result = numbers2
result = numbers2[0, 2]
result = numbers2[:, 0]
result = numbers2[:, 0:2]#bütün satırlardan 0 dan 1 e kadar yazdırır.
result = numbers2[-1, :]#son satırın hepsini yazdırır
result = numbers2[:3, :3]#3 satırdan 3 değeride alır.
# print(result)
arr1 = np.arange(0, 10)
arr2 = arr1.copy()

print(arr1)
print(arr2)