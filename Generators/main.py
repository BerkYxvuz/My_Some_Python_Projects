# def cube():
#     result = []
#     for i in range(5):
#         result.append(i ** 3)
#     return result
# print(cube())
'''
Bu yöntem range de kullanılan sayı büyük olduğunda fazlaca yer kaplıyor
Bu yüzden aşağıdaki yöntem büyük işlemlerde yer tutmaması için çok işlevli oluyor
'''
#def cube():
    #for i in range(5):
        #yield i ** 3 # Yield değer üretiyor gönderiyor ve bellekte tutulmuyor bu yüzden 2.kez çağıramayacağımız bir değer
#print(cube())
# Kodlar bu şekilde generator'ın bellekteki yerini gönderiyor ama aşağıda

# def cube():
#     for i in range(5):
#         yield i ** 3
#
# for i in cube():
#     print(i)

#Fonksiyon harici örnekler

generator = (i**3 for i in range(5))

for i in generator:
    print(i)