import mysql.connector
from output import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem

from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QApplication, QDialog
from popup import Ui_PopupWindow

class MyApp(QtWidgets.QMainWindow):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.uii = Ui_PopupWindow()
        self.uii.setupUi(self.window)
        self.window.show()
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle("E School")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # DATA BASE PART
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="berk1907",
        database="eschool"
        )
        self.mycursor = self.mydb.cursor()
        self.mydb.close()
        # DATA BASE PART FINISHED

        self.combobox_add_class()
        self.load_students()

        self.ui.comboBox.currentIndexChanged.connect(self.load_students)
        self.ui.pushButton_2.clicked.connect(self.openWindow)


    def combobox_add_class(self):
        items = ["A","B","C","D"]
        self.ui.comboBox.addItems(items)
        pass

    def load_students(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost",user="root",password="berk1907",database="eschool")
            self.mycursor = self.mydb.cursor()
            value = self.ui.comboBox.currentText()
            sql = "SELECT Isim, Soyisim, No, Sinif FROM Students WHERE Sinif=%s"
            self.mycursor.execute(sql,list(value))
            result = self.mycursor.fetchall()

            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(4)

            for row in range(len(result)):
                for column in range(4):
                    item = QTableWidgetItem(str(result[row][column]))
                    self.ui.tableWidget.setItem(row, column, item)

            
            pass
        except Exception as ex:
            print(ex)
        finally:
            self.mydb.close()
            pass
    


class ExamplePopup(QDialog):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.label = QLabel(self.name, self)
app = QtWidgets.QApplication(sys.argv)
win = MyApp()
win.show()
sys.exit(app.exec_())