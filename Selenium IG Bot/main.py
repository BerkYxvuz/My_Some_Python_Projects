import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, instaloader, urllib.request
from tkinter import *


def renkdegis():
    takipetmeyenler.config(bg="red")
    window.update()

def renkdegisYESIL():
    takipetmeyenler.config(bg="green")
    window.update()

class IGBOT:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.IGURL = "https://www.instagram.com"
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.list = []
        self.bot = instaloader.Instaloader()
        self.followingers = 0
        self.loggined = False
    def Login(self):
        if self.loggined is False:
            self.loggined = True
            self.driver.get(self.IGURL)
            time.sleep(2)

            findusernamebox = self.driver.find_elements(By.TAG_NAME, 'input')
            submit = self.driver.find_element(By.TAG_NAME, 'button')

            findusernamebox[0].send_keys(f'{self.username}')
            findusernamebox[1].send_keys(f'{self.password}')
            submit.click()
            time.sleep(12)
        else:
            pass
    def GetFollowers(self):
        profile = instaloader.Profile.from_username(self.bot.context, f'{self.username}')
        followercount = int(profile.followers)
        self.driver.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(4)
        getdiv = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        action = webdriver.ActionChains(self.driver)
        dialog = self.driver.find_element(By.CSS_SELECTOR, '.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe')
        time.sleep(2)
        dialog.click()
        while followercount != len(self.followers):
            getspan = getdiv.find_elements(By.CSS_SELECTOR, '._aacl._aaco._aacw._aacx._aad7._aade')
            if followercount != len(getspan):
                action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
            else:
                getspan = getdiv.find_elements(By.CSS_SELECTOR, '._aacl._aaco._aacw._aacx._aad7._aade')
                for x in getspan:
                    self.followers.append(x.text)
        with open("followers.txt", "w", encoding='utf-8') as f:
            for item in self.followers:
                f.write(item + "\n")
    def FollowAuto(self):
        user = input('Takip Edilecek Kullanıcı Adı: ')
        self.driver.get(f"https://www.instagram.com/{user}/")
        time.sleep(4)
        getfollowerbutonz = self.driver.find_element(By.CSS_SELECTOR, '.x1qjc9v5.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x5n08af.x78zum5.xdt5ytf.xs83m0k.xeuugli.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xk390pu.x11njtxf.x139hhg0.x1qgnrqa.xg1prrt.x1quol0o')
        getfollowerbuton = getfollowerbutonz.find_element(By.TAG_NAME, 'button')
        if getfollowerbuton.text == 'Takip Et':
            getfollowerbuton.click()
            time.sleep(3)
        else:
            print('Zaten takip ediliyor.')
    def UnFollow(self, nick):
        user = nick
        self.driver.get(f'https://www.instagram.com/{user}/')
        time.sleep(2)
        getfollowerbutonz = self.driver.find_element(By.CSS_SELECTOR, '.x1qjc9v5.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x5n08af.x78zum5.xdt5ytf.xs83m0k.xeuugli.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xk390pu.x11njtxf.x139hhg0.x1qgnrqa.xg1prrt.x1quol0o')
        getfollowerbuton = getfollowerbutonz.find_element(By.TAG_NAME, 'button')
        if getfollowerbuton.text == 'İstek Gönderildi' or getfollowerbuton.text == 'Takiptesin':
            getfollowerbuton.click()
            time.sleep(2)
            getnewdiv = self.driver.find_element(By.CSS_SELECTOR, '.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe')
            getunfbut = getnewdiv.find_elements(By.TAG_NAME, 'div')
            for x in getunfbut:
                if x.text == 'Takibi Bırak':
                    x.click()
                    time.sleep(1)
                    takipetmeyenlerlistbox.delete(nick)
                    break
                else:
                    pass
        else:
            print('Zaten takip ediliyor.')
    def GetFollowing(self):
        profile = instaloader.Profile.from_username(self.bot.context, f'{self.username}')
        self.driver.get(f'https://www.instagram.com/{self.username}/following/')
        time.sleep(4)
        followingcount = int(profile.followees)
        time.sleep(1)
        getacc = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        action = webdriver.ActionChains(self.driver)
        dialog = self.driver.find_element(By.CSS_SELECTOR, '.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe')
        time.sleep(1)
        dialog.click()

        while followingcount != len(self.following):
            getfollow = getacc.find_elements(By.CSS_SELECTOR, '._aacl._aaco._aacw._aacx._aad7._aade')
            self.followingers = int(len(getfollow))
            if followingcount != len(getfollow):
                action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
            else:
                for x in getfollow:
                    self.following.append(x.text)
        with open("following.txt", "w", encoding='utf-8') as f:
            for item in self.following:
                f.write(item + "\n")
    def UnfDoesntFollowers(self):

        renkdegis()
        self.Login()
        self.GetFollowers()
        time.sleep(1)
        self.GetFollowing()
        time.sleep(1)
        self.list = []
        for x in self.following:
            y = x
            if y in self.followers:
                pass
            else:
                self.list.append(x)
                takipetmeyenlerlistbox.insert(tkinter.END, x)
        renkdegisYESIL()
popup = Tk()
popup.title("Giriş Ekranı")
popup.overrideredirect(True)
popup.geometry("160x200")

screen_width = popup.winfo_screenwidth()
screen_height = popup.winfo_screenheight()
window_width = popup.winfo_reqwidth()
window_height = popup.winfo_reqheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
popup.geometry("+{}+{}".format(x, y))

Label1 = Label(text="Kullanıcı Adı")
Label1.place(x=40, y=0)

usernam = tkinter.Entry(popup,)
usernam.place(x=20, y=40)

Label2 = Label(text="Şifre")
Label2.place(x=65, y=70)

password = tkinter.Entry(popup, show="*")
password.place(x=20, y=120)

def logginer():
    submit.config(bg="red")
    global igbot
    igbot = IGBOT(username=usernam.get(), password=password.get())
    igbot.Login()
    if igbot.loggined is True:
        submit.config(bg="green")
        popup.update()
        time.sleep(2)
        popup.destroy()
    popup.mainloop()

submit = Button(popup, text="Giriş Yap", command=logginer)
submit.place(x=55, y=160)

popup.mainloop()

bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, igbot.username)

window = Tk()
window.title("Instagram Bot")
window.geometry("428x340")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry("+{}+{}".format(x, y))

username = Label(window, text=f'Kullanıcı Adı: {profile.username}')
username.place(x=10, y=80)

followers = Label(window, text=f'Takipçi: {profile.followers}')
followers.place(x=180, y=80)

following = Label(window, text=f'Takip Edilenler: {profile.followees}')
following.place(x=260, y=80)

def yenile():
    global profile
    profile = instaloader.Profile.from_username(bot.context, igbot.username)

reload = Button(window, text="Yenile", command=yenile)
reload.place(x=380, y=80)

uyari = Label(window, text="Bastığınız Buton Yeşil Olana Kadar Uygulamaya Tıklamayınız\nBunun Anlamı İşlem Devam Ediyor Demektir.")
uyari.place(x=10, y=10)

takipetmeyenler = Button(window, text="Takip Etmeyenleri Bul", command=igbot.UnfDoesntFollowers)
takipetmeyenler.place(x=10, y=110)
nick = ""
def takiptencik():
    nick = takipetmeyenlerlistbox.get(takipetmeyenlerlistbox.curselection())
    igbot.UnFollow(nick)

takipetmeyenlerlistbox = Listbox(window, selectmode=tkinter.SINGLE)
takipetmeyenlerlistbox.place(x=10, y=150)

takiptencikar = Button(window, text=f"Takipten Çıkar", command=takiptencik)
takiptencikar.place(x=135, y=150)

window.mainloop()