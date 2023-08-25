import matplotlib.pyplot as plt
import datetime

berkkosular = \
{
    "kosu1": {"tarih": datetime.date(2023, 4, 1), "sure": 13.03},
    "kosu3": {"tarih": datetime.date(2022, 4, 23), "sure": 12.21}
}

tarihler = [berkkosular[k]["tarih"] for k in berkkosular]
saniyeler = [berkkosular[k]["sure"] for k in berkkosular]

plt.plot(tarihler, saniyeler)
plt.xlabel("Tarih")
plt.ylabel("Süre (saniye)")
plt.title("Atletizm Koşu Grafiği")
plt.show()