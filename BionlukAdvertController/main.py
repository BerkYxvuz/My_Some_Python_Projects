from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import telebot
import asyncio
import time


# Kullanı

bot_token = "Your-Bot-Token"

bot = telebot.TeleBot(token=bot_token)

user_id = "yourtelegramuserid"

message = "Bionlukta Yeni İlan Var!"

is_function_called = False

# Mesaj gönderme işlemi
def send_message():
    bot.send_message(chat_id=user_id, text=message)

class Fonksiyon():
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--headless")  # Başsız mod
        self.driver = webdriver.Chrome(options=options)
    def Login(self):
        self.driver.get("https://bionluk.com/login")

        time.sleep(5)

        inputs = self.driver.find_elements(By.TAG_NAME, "input")

        button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div[8]/form/button')

        inputs[0].send_keys("E-POSTA")
        inputs[1].send_keys("ŞİFRE/PASSWORD")

        button.click()

        time.sleep(5)

    def GetAdverts(self):
        self.driver.get("https://bionluk.com/panel/alici-istekleri")
        
        time.sleep(5)
        
        mainbox = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div/div[2]')
        request_boxes = mainbox.find_elements(By.CLASS_NAME, "request-box")
        adverts = {}
        for x in request_boxes:
            item1 = x.find_element(By.CLASS_NAME, "body-title").text
            item2 = x.find_element(By.CLASS_NAME, "body-text").text

            adverts[item1] = item2
        return adverts

Program = Fonksiyon()
Program.Login()
kontrol = 0
deger1 = None
deger2 = None
while True:
    if kontrol == 0:
        deger1 = Program.GetAdverts()
        kontrol+=1
    elif kontrol == 1:
        deger2 = Program.GetAdverts()
        kontrol-=1

    if deger1 != deger2:
        send_message()
    else:
        pass

    time.sleep(1800)