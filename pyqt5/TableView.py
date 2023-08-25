from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from tableviewform import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.pushButton.clicked.connect(self.saveProduct)
        self.ui.tableproducts.doubleClicked.connect(self.doubleClick)
    def doubleClick(self):
        for item in self.ui.tableproducts.selectedItems():
            print(item.row(), item.column(), item.text())

    def saveProduct(self):
        name = self.ui.nameline.text()
        price = self.ui.priceline.text()

        if name and price is not None:
            rowC = self.ui.tableproducts.rowCount()
            self.ui.tableproducts.insertRow(rowC)
            self.ui.tableproducts.setItem(rowC, 0, QTableWidgetItem(name))
            self.ui.tableproducts.setItem(rowC, 1, QTableWidgetItem(price))

    def loadProducts(self):
        products = [
            {'name': 'Samsung S5', 'price': '2000'},
            {'name': 'Samsung S6', 'price': '3000'},
            {'name': 'Samsung S7', 'price': '4000'},
            {'name': 'Samsung S8', 'price': '5000'}
        ]

        self.ui.tableproducts.setRowCount(len(products))
        self.ui.tableproducts.setColumnCount(2)
        self.ui.tableproducts.setHorizontalHeaderLabels(('Name', 'Price'))
        self.ui.tableproducts.setColumnWidth(0, 100)
        self.ui.tableproducts.setColumnWidth(1, 40)

        rowIndex = 0
        for product in products:
            self.ui.tableproducts.setItem(rowIndex, 0, QTableWidgetItem(product['name']))
            self.ui.tableproducts.setItem(rowIndex, 1, QTableWidgetItem(str(product['price'])))
            rowIndex += 1



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()