from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://web.telegram.org/z/#-1283943060"

driver.get(url)
time.sleep(15)
SearchElement = driver.find_element(By.ID, "editable-message-text")
SearchElement.send_keys("python")
SearchElement.send_keys(Keys.ENTER)