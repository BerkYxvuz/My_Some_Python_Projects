from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import *
import time

class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    def NextPage(self):
        submit = self.browser.find_element(By.XPATH, '//*[@id="user-profile-frame"]/div/div[51]/div/a')
        submit.send_keys(Keys.ENTER)
        return submit.text
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        findusernamelement = self.browser.find_element(By.ID, 'login_field')
        findusernamelement.send_keys(f'{self.username}')

        findpasselement = self.browser.find_element(By.ID, 'password')
        findpasselement.send_keys(f'{self.password}')

        submitelement = self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]')
        submitelement.send_keys(Keys.ENTER)
    def GetFollowers(self):
        self.browser.get(f"https://github.com/sadikturan?tab=followers")

        items = self.browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed')
        for i in items:
            follower = i.find_element(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade").text
            if follower == '':
                pass
            elif follower != '':
                self.followers.append(follower)


github = GitHub(username,password)
github.signIn()
github.GetFollowers()
print(github.followers)