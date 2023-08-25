import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time, random



class DRIVER():
    def __init__(self):

        self.driver = uc.Chrome()
        self.actions = ActionChains(self.driver)
        self.driver2 = uc.Chrome()
        self.isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli", "Hüseyin", "Zeynep", "Cem", "Ebru", "Can", "Gülay", "Emre", "İpek", "Selim", "Burcu", "Deniz", "Aylin", "Cihan", "Nazlı"]
        self.aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


    def Register(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(15)
        kaydol_btn = self.driver.find_elements(By.TAG_NAME, 'span')
        for x in kaydol_btn:
            if x.get_attribute('role'):
                if x.text == 'Kaydol':
                    x.click()
                    break
        time.sleep(3)

        divs = self.driver.find_elements(By.TAG_NAME, 'div')

        for x in divs:
            if x.get_attribute('role') == 'button':
                if x.text == 'Hesap oluştur':
                    x.click()
                    break

        time.sleep(3)

        name_inpt = self.driver.find_element(By.NAME, 'name')
        name_inpt.send_keys(random.choice(self.isimler))

        time.sleep(2)

        epostakullan = self.driver.find_elements(By.TAG_NAME, 'div')

        for x in epostakullan:
            if x.get_attribute('role') == 'button':
                if x.find_element(By.TAG_NAME, 'span').text == 'E-posta kullan':
                    x.click()

        time.sleep(3)

        self.driver2.get("https://temp-mail.org/en/")

        time.sleep(30)

        buts = self.driver2.find_elements(By.TAG_NAME, 'button')

        for x in buts:
            if x.text == 'Copy':
                x.click()
        
        eposta_inpt = self.driver.find_element(By.NAME, "email")

        eposta_inpt.send_keys(Keys.CONTROL, 'v')

        selectors = self.driver.find_elements(By.TAG_NAME, 'select')

        time.sleep(3)
        # MONTH SELECTOR
        selectormont = selectors[0]

        selectormonth = Select(selectormont)

        selectormonth.select_by_value('4')
        # DAY SELECTOR
        selectorday = selectors[1]

        selectordays = Select(selectorday)

        selectordays.select_by_value(str(random.randint(1, 30)))
        # YEAR SELECTOR
        selectoryears = selectors[2]

        selectoryear = Select(selectoryears)

        selectoryear.select_by_value('2000')

        ileri = self.driver.find_elements(By.TAG_NAME, 'div')

        for x in ileri:
            if x.text == 'İleri':
                x.click()
                break

        time.sleep(5)

        ileri = self.driver.find_elements(By.TAG_NAME, 'div')

        for x in ileri:
            if x.text == 'İleri':
                x.click()
                break

        time.sleep(5)

        ileri = self.driver.find_elements(By.TAG_NAME, 'div')

        for x in ileri:
            if x.text == 'Kaydol':
                x.click()
                break


bot = DRIVER()
bot.Register()