from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://web.telegram.org/k/"

driver.get(url)

time.sleep(2)

driver.maximize_window() # siteyi tam ekran yapar
driver.save_screenshot("screenshot") # screenshot alır "isim" olarak belirtilir
# driver.back() bulunduğu sayfanın bir gerisini gider.
# driver.forward() bulunduğu sayfanın bir ilerisine gider.
print(driver.title)
time.sleep(2)
driver.close()