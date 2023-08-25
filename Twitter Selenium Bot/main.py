import requests, time, pyautogui
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import undetected_chromedriver as uc

class TWBOT:
    def __init__(self):
        self.mainurl = "https://twitter.com/"
        self.URL = "https://twitter.com/login"
        self.driver = uc.Chrome()
    def Login(self):
        self.driver.get(self.URL)
        time.sleep(2)
        inpt = self.driver.find_element(By.NAME, "text")
        inpt.send_keys("username")
        time.sleep(1)
        butondiv = self.driver.find_elements(By.TAG_NAME, "div")
        time.sleep(1)
        try:
            for x in butondiv:
                if x.text == "İleri":
                    x.click()
        except:
            pass
        time.sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("yourpassword")

        submit = self.driver.find_elements(By.TAG_NAME, 'div')
        try:
            for x in submit:
                if x.text == "Giriş yap":
                    x.click()
        except:
            pass
        time.sleep(2)

    def GetFollws(self):
        global getbuttons
        self.driver.get("https://twitter.com/D88655/followers")
        time.sleep(6)
        while True:
            getbuttons = self.driver.find_elements(By.TAG_NAME, "div")
            for x in getbuttons:
                try:
                    if x.get_attribute('role') == 'button' and 'Takip et' in x.get_attribute('aria-label'):
                        x.click()
                        time.sleep(6)
                    else:
                        pass
                except Exception as ex:
                    getbuttons = self.driver.find_elements(By.TAG_NAME, "div")
                    pass
                finally:
                    pass

    def Findunf(self):
        pass


twbot = TWBOT()
twbot.Login()
time.sleep(5)
twbot.Findunf()