# Data frame birden fazla serinin birleşmiş hali yani tablo gibidir.
# Json'u frame'e çevirip işlem yapabiliyoruz ve başka çeşitli dosyalar içinde geçerli.
import pandas as pd

data = [["Ahmet", 50],
        ["Ali", 60],
        ["Yağmur", 70],
        ["Çınar", 70]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
dict_list = [{"Name":"Ahmet","Grade":59},
             {"Name":"Ali","Grade":75},
             {"Name":"Yağmur","Grade":85},
             {"Name":"Berk","Grade":71}
             ]
# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(data, columns=['İsim', 'Not'], index=[1,2,3,4], dtype=float)
                                                                    # bu şekilde kolonları isimlendirebiliriz.
                                                                    # İndexleri ayarlayabiliriz.
                                                                    #dtype= ile değerlerin türünü belirleriz
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index=[212,213,214,215])
df = pd.DataFrame(dict_list)

print(df)



# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2]) # Seriler oluşturduk
#
# data = dict(apples = s1, oranges = s2) # bunları dict'e çevirdik
#
# df = pd.DataFrame(data) # burada DataFrame'e çevirdik
#
# print(df) # ve yazdırdık.