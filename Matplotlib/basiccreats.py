import matplotlib.pyplot as plt
import numpy as np
'''

x = [1,2,3,4]
y = [1,4,9,16]

# color="" çizginin rengini belirler
# linewidth="" çizginin kalınlığını belirler
# matplotlib style google'da aratınca style ayarları çıkıyor.

plt.plot(x, y, "--r") # kullanılacak değeri verdik
plt.axis([0, 6, 0, 20]) # solda ki 2 değer x'e sağda ki 2 değer y'ye ait (tablonun genişliğini ayarlar)
plt.title("Grafik")
plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.show() # ve göster dedik
'''
'''
x = np.linspace(0, 2, 100)

plt.plot(x, x, label="linear", color="black")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.legend()
plt.show()
'''

'''
axs[0].plot(x, x, color="black") # birden fazla grafik tablosu oluşturduk.
axs[1].plot(x, x**2, color="red")
axs[2].plot(x, x**3, color="blue")
plt.tight_layout() # başlıkları karıştırmamak için
plt.show()
'''
'''
x = np.linspace(0, 2, 100)
fig,axs = plt.subplots(2, 2) #virgülden sonra koyunca yana geliyor

axs[0, 0].plot(x, x, color="black") # birden fazla grafik tablosu oluşturduk.
axs[0, 1].plot(x, x**2, color="red")
axs[1, 0].plot(x, x**3, color="pink")
axs[1, 1].plot(x, x**4, color="yellow")

plt.show()
'''

import pandas as pd

df = pd.read_csv("all_seasons.csv")

df = df.groupby("age").mean()

df.plot(subplots=True)
plt.legend()

plt.show()