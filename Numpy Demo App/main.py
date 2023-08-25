import numpy as np

result = np.array([10, 15, 30, 45, 60])

result = np.arange(5, 15)

result = np.arange(50, 100, 5)

result = np.zeros(10)

result = np.ones(10)

result = np.linspace(0, 100, 5)# 0-100 arasında eşit aralıklı 5 sayı oluşturdu

result = np.random.randint(10, 30, 5)

result = np.random.randn(10)

result = np.random.randint(10, 50, 15)
result = result.reshape(3, 5)

sutun = result.sum(axis=1)
satir = result.sum(axis=0)

enk = result.max()
enb = result.min()
ort = result.mean()

enbinx = result.argmax()

result = np.flip(result)

resulttt = result[:, 0] #her satırın ilk sayısı

resultkare = np.sqrt(result)

resultcift = result[result % 2 == 0]
resultcift = resultcift > 5

print(resultcift)