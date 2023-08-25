import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9] # normal python listesi

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9]) # numpy ile oluşturulmuş liste

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]] # burada 3 e ayrılmış bilgiler mevcut
np_multi = np_array.reshape(3,3) #burada 3 satır ve 3 kolon oluşturuluyor

print(py_multi)
print(np_multi)

print(np_array.ndim) # dizi elamanı kaç boyutlu ona bakıyor
print(np_multi.ndim)

print(np_array.shape) # shape ini kontrol ediyoruz.
print(np_multi.shape)