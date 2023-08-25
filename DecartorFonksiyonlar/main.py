import math,time

def Sure_Hesapla(func):
    def inner(*args):
        started = time.time()
        time.sleep(1)
        finished = time.time()
        print(f'Toplam: {func(*args)}, İşlem {started-finished} saniye sürdü.')
    return inner

@Sure_Hesapla
def Toplama(a, b):
    return a + b
Toplama(1, 2)