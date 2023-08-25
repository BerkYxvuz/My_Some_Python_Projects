import matplotlib.pyplot as plt
import numpy as np

'''
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [4,6,15,23,3]
oyuncu3 = [53,25,13,12,22]

# StackPlot

plt.plot([],[],color='y',label="Oyuncu1")
plt.plot([],[],color='r',label="Oyuncu2")
plt.plot([],[],color='b',label="Oyuncu3")

plt.stackplot(yil, oyuncu1, oyuncu2, oyuncu3, colors=["y", "r", "b"])

plt.show()
'''
# PİE GRAFİĞİ
'''
goaltypes = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'

goals = [12, 20, 7]
colors = ['y', 'r', 'b']

plt.pie(goals,labels=goaltypes,colors=(colors),shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()
'''

# BAR GRAFİĞİ

'''
plt.bar([0.25,1.25,2.25,3.25,4.25], [50,40,70,80,20], label="BMW", width=.5)
plt.bar([0.25,9.25,7.25,3.25,6.25], [88,46,12,55,23], label="SUPRA", width=.5)

plt.xlabel("Gün")
plt.ylabel("Mesafe/KM")
plt.title("Araç Bilgileri")

plt.show()
'''

yaslar = np.random.randint(0, 100, 20)
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar, yas_gruplari, histtype="bar", rwidth=0.8)
plt.xlabel("Yaş Grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram")

plt.show()