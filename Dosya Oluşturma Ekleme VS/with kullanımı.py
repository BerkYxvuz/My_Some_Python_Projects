# with open("newfile. txt", "r", encoding="utf-8")as file:
#     content = file.read
#     print(content)
#With komutunu bu şekilde kullandığımızda artık file.close() komutuna gerek kalmıyor kodlar bitince otomatik kapanıyor
#file.seek(sayı) sayı yerine girilen değer okunanın dosyada metnin sonunda yanıp sönen düz çizgiyi yazdığınız sayıya atar
#Mesela "12345" metnini içeren bir txt dosyasında read dedikten sonra 5 ten sonra düz çizgi yanıp sönecek yani okuma yeri
#Ama ben file.seek(0) yaparsam okuma başa dönecektir.
#file.tell() bana okuma çizgisinin yerini verir.
# with open("newfile. txt", "r", encoding="utf-8") as file:
#     list = file.readlines() Bütün satırları list'e aktarıyor.
#     list.insert(index, Değer) satırları listeye çevirdikten sonra index ve değer belirterek istediğimiz
# indexten sonra değer ekleyebiliriz.
#     print(content)