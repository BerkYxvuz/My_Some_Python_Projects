from tkinter import *
window = Tk()
window.title('ATM')
window.attributes("-fullscreen", True)
class Kullanicilar():
    def __init__(self, kulnosu, kulsifre):
        self.kulno = kulnosu
        self.sifre = kulsifre
berkyavuz = Kullanicilar("1234 5678 1234 5678","1234")

#Ana Sayfa
KartNo = Label(window, text="Kart Numaranızı Giriniz")
KartNo.pack()

Numara = Text(window, width="18", height=1, font=("Helvetica", 32))
Numara.pack()

SifreNo = Label(window, text="Şifrenizi Giriniz")
SifreNo.pack()

Sifre = Entry(window, show="*", width=3, font=("Helvetica", 32))
Sifre.pack(pady=10)

def girisfonk():
    pass

Giris = Button(window, text="Giriş", height="1", width="4", background="grey", font=("Helvetica", 16), command=girisfonk)
Giris.pack()



window.mainloop()