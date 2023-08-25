from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from gui_py import Ui_MainWindow
from PyQt5 import QtWidgets
import time, sys, csv



class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.csv_file_path = "domains.csv"

        self.ui.pushButton.clicked.connect(self.Test)
        
    def Test(self):
        

        # Selenium
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yoncu.com")
        time.sleep(3)
        getbox = self.driver.find_element(By.ID, "YncDomSorguTxt")
        getbox.send_keys(self.ui.textEdit.toPlainText())

        for_domain_text = self.ui.textEdit.toPlainText()
        domains = for_domain_text.split(",")

        time.sleep(0.5)

        getbutton = self.driver.find_element(By.XPATH, "//*[@id='DSAltOrtaOrtaUst']/div/button")

        getbutton.click()

        time.sleep(15)
        domains_div = self.driver.find_element(By.ID, "DomSorguNanlar")
        for domain in domains:
            by_domain_element = domains_div.find_element(By.ID, domain)
            b_element = by_domain_element.find_element(By.TAG_NAME, "b")
            b_text = b_element.text

            domain_a = by_domain_element.find_elements(By.TAG_NAME, "a")
            onclick_t = domain_a[1].get_attribute("onclick")
            onclick_t2 = onclick_t.split("Bu alan adını ")[1]
            onclick_t3 = onclick_t2.split(" tarihinden")[0]

            the_text = f"Durum:{b_text} Backorder Zamanı: {onclick_t3}"

            print(the_text)

            with open(self.csv_file_path, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                # Verileri ayrı sütunlara yazdır
                writer.writerow([domain,b_text, onclick_t3])


        time.sleep(5)

app = QtWidgets.QApplication(sys.argv)
win = MyApp()
win.show()
sys.exit(app.exec_())