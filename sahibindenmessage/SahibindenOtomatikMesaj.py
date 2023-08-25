from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, instaloader, urllib.request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import undetected_chromedriver as uc
import pandas as pd
import tkinter as tk

datafr = pd.read_csv('linkler.csv')
df2 = pd.read_csv('mesajgidenler.csv')

zatenvarolanlinklerpd = datafr['linkler']
zatenvarolanlinkler = list(zatenvarolanlinklerpd)

loginurl = "https://secure.sahibinden.com/giris"

driver = uc.Chrome()
driver.get(loginurl)
driver.set_window_size(800, 600)

anliktrler = []
yenieklenentrler = []
acilcikis = 0

hide = False

def hide_show_driver():
    global driver, hide
    hide = not hide
    if hide is False:
        driver.set_window_position(0, 0)
        driver.screen_width = 1024
        driver.screen_height = 768
    else:
        driver.set_window_position(-3000, 0)
        driver.screen_width = 0
        driver.screen_height = 0

def Login(epos, sif):
    epostdiv = driver.find_element(By.ID, 'loginSelectionPageEmail')
    epostdiv.send_keys(epos)

    submitbut = driver.find_element(By.ID, 'signInWithEmail')
    submitbut.send_keys(Keys.ENTER)

    time.sleep(5)

    password = driver.find_element(By.ID, 'password')
    password.send_keys(sif)

    logbut = driver.find_element(By.ID, 'userLoginSubmitButton')
    logbut.send_keys(Keys.ENTER)

def SayfayaGit(link, kactane):
    global anliktrler, zatenvarolanlinkler, df, href, linkler, trler, yenieklenentrler, acilcikis
    try:

        driver.get(link)
        time.sleep(6)

        while True:
            tbody = driver.find_element(By.CSS_SELECTOR, '.searchResultsRowClass')
            trler = tbody.find_elements(By.TAG_NAME, 'tr')
            linkler = tbody.find_elements(By.CSS_SELECTOR, '.classifiedTitle')
            print("Veriler Alındı")

            if int(len(yenieklenentrler)) == int(kactane) or int(len(yenieklenentrler)) > int(kactane):
                print(f'{kactane} Adet İlan Alındı')
                yenieklenentrler = []
                yenieklenentrler.clear()
                break

            elif acilcikis == int(kactane):
                print('BİTTİ')
                yenieklenentrler = []
                yenieklenentrler.clear()
                break

            for x in linkler:
                if len(yenieklenentrler) > int(kactane):
                    break
                print("Yeni Linke Geçildi")
                href = x.get_attribute('href')
                if href not in zatenvarolanlinkler:
                    print('Kayıt Ediliyor')
                    href = href.replace('"', '')
                    yeni_link = {
                        'linkler': [href]
                    }
                    df = pd.read_csv('linkler.csv')
                    df = pd.concat([df, pd.DataFrame(yeni_link)])
                    df.to_csv('linkler.csv', index=False)
                    zatenvarolanlinklerpd = df['linkler']
                    zatenvarolanlinkler = list(zatenvarolanlinklerpd)
                    anliktrler.append(href)
                    yenieklenentrler.append(href)
                    print('Kayıt Edildi')
                    time.sleep(0.5)
                elif href in zatenvarolanlinkler:
                    print('Zaten Var Olan Link')
                    if len(trler) < kactane:
                        kactane = len(trler)
                        acilcikis = kactane
                        break
                    if len(anliktrler) == len(trler):
                        try:
                            global nxtbuton2
                            print("Sayfa Değişme Kısmında")
                            nxtbuton = driver.find_elements(By.CSS_SELECTOR, '.prevNextBut')

                            for y in nxtbuton:
                                print("Buton arıyor")
                                if y.get_attribute('title') == 'Sonraki':

                                    x = ""
                                    nxtbuton2 = y.get_attribute('href')
                                    break

                                if nxtbuton[0].get_attribute('title') != 'Sonraki' and nxtbuton[1].get_attribute('title') != 'Sonraki':
                                    if nxtbuton[0].get_attribute('title') == 'Önceki':
                                        acilcikis = kactane
                                        break
                            print('Sayfa Değişiyor...')
                            driver.get(nxtbuton2)
                            anliktrler.clear()
                            time.sleep(5)
                            break
                        except:
                            anliktrler.append(" ")
                            pass
                    else:
                        anliktrler.append(" ")
                        pass
                    pass
                else:

                    pass
    except Exception as ex:
        if ex == StaleElementReferenceException:
            print("Hata oluştu, element yeniden bulunuyor...")
            tbody = driver.find_element(By.CSS_SELECTOR, '.searchResultsRowClass')
            trler = tbody.find_elements(By.TAG_NAME, 'tr')
            linkler = tbody.find_elements(By.CSS_SELECTOR, '.classifiedTitle')
            print("Veriler Yeniden Alındı")
            pass

def MesajGonder(message):
    global df2, lng
    say = 0
    dataframemesajgidenler = pd.read_csv('mesajgidenler.csv')
    mesajgidenlerz = dataframemesajgidenler['mesajgidenler']
    mesajgidenler = list(mesajgidenlerz)
    try:
        for x in zatenvarolanlinkler:
            lng = x
            if x not in mesajgidenler:
                driver.get(x)
                time.sleep(8)

                saticibilgileri = driver.find_element(By.ID, 'askQuestionLink')
                saticimsglink = saticibilgileri.get_attribute('href')
                driver.get(saticimsglink)

                time.sleep(2)

                messagebox = driver.find_element(By.ID, 'messageContent')
                messagebox.send_keys(message)

                time.sleep(30)

                gonderbuton = driver.find_elements(By.TAG_NAME, 'button')
                for y in gonderbuton:
                    if y.get_attribute('ng-disabled') == '!sendMessageForm.$valid':
                        y.click()
                        say += 1

                        yeni_giden = {
                            'mesajgidenler': [x]
                        }
                        df2 = pd.concat([df2, pd.DataFrame(yeni_giden)])
                        df2.to_csv('mesajgidenler.csv', index=False)

                        time.sleep(5)
            elif x in mesajgidenler:
                pass
            elif len(zatenvarolanlinkler) == say:
                break
    except:
        yeni_giden = {
            'mesajgidenler': [lng]
        }
        df2 = pd.concat([df2, pd.DataFrame(yeni_giden)])
        df2.to_csv('mesajgidenler.csv', index=False)
        time.sleep(1)
        pass

win = tk.Tk()
win.configure(bg="#191919")
win.title('Sahibinden Mesaj Gönderme Uygulaması')
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win.geometry("500x600+800+0")
# değişkenler
loggined = False

# fonksiyonlar
def girisislemi():
    global loggined
    epos = epostatextbox.get("1.0", "end-1c")
    sif = sifretextbox.get("1.0", "end-1c")
    Login(epos, sif)
    gidecekmesajlab.configure(fg="green")
    olaylab.configure(fg="green")
    win.update()

# Giriş Bilgileri
kuladilabel = tk.Label(win, text="E-Posta", bg="#191919", fg="white")
kuladilabel.place(x=75, y=0)

epostatextbox = tk.Text(win, width=20, height=1)
epostatextbox.place(x=20, y=20)

passlabel = tk.Label(win, text="Şifre", bg="#191919", fg="white")
passlabel.place(x=255, y=0)

sifretextbox = tk.Text(win, width=20, height=1)
sifretextbox.place(x=190, y=20)

Girisbuton = tk.Button(win, text="Giriş Yap", bg="gray", fg="white", command=girisislemi)
Girisbuton.place(x=380, y=17)

ilansayisi = tk.Label(win, text=f'Mevcut İlan Sayısı: {len(datafr["linkler"])}', bg="#191919", fg="white", font=("Arial", 16))
ilansayisi.place(x=20, y=60)

# Linkleri Alma Kısmı
olaylab = tk.Label(win, text="İlanları Bul", bg="#191919", fg="red", font=("Arial", 24))
olaylab.place(x=25, y=130)

urlgirislab = tk.Label(win, text="URL", bg="#191919", fg="white")
urlgirislab.place(x=85, y=180)

urlgiris = tk.Text(win, width=20, height=1)
urlgiris.place(x=20, y=200)

kaclinklab = tk.Label(win, text="Kaç Tane İlan Alınacak", bg="#191919", fg="white")
kaclinklab.place(x=35, y=230)

kaclink = tk.Text(win, width=10, height=1)
kaclink.place(x=55, y=260)

def SayfayaGitIslemi():
    urllingi = urlgiris.get("1.0", "end-1c")
    tane = kaclink.get("1.0", "end-1c")
    tanesi = int(tane)
    SayfayaGit(link=urllingi, kactane=tanesi)
    datafr = pd.read_csv('linkler.csv')
    ilansayisi.configure(text=f'Mevcut İlan Sayısı: {len(datafr["linkler"])}')
    win.update()

ilanal = tk.Button(win,text="İlanları Al", width=10, height=1, command=SayfayaGitIslemi)
ilanal.place(x=57, y=290)

# Mesaj gönderme kısmı
gidecekmesajlab = tk.Label(win, text='İlanlara Mesaj \nGönderme', bg="#191919", fg="red", font=("Arial", 16))
gidecekmesajlab.place(x=260, y=130)

gidecekmesaj = tk.Text(win, width=20, height=8)
gidecekmesaj.place(x=250, y=190)

hidebuton = tk.Button(win, text="Google'ı Gizle/Göster", command=hide_show_driver)
hidebuton.place(x=20, y=100)

def mesajgidiyor():
    try:
        message = gidecekmesaj.get("1.0", "end-1c")
        MesajGonder(message=message)
    except:
        pass
gondermesaj = tk.Button(win, text='Gönder', command=mesajgidiyor)
gondermesaj.place(x=310, y=340)

win.mainloop()