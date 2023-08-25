import pyqrcode,sys,png
from pyqrcode import QRCode
from output import Ui_MainWindow
from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.setWindowTitle("QRCODE Maker")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Create)

    def Create(self):
        if self.ui.textEdit.toPlainText() == None:
            pass
        else:
            string = str(self.ui.textEdit.toPlainText())
            qrname = str(self.ui.textEdit_2.toPlainText())

            qrcode = pyqrcode.create(string)

            qrcode.png(f"C:/Users/berk.BERK-PC/Documents/TheAll/Python/Projects/QrCodeMaker/qrcodes/{qrname}.png", scale = 8)
            

app = QtWidgets.QApplication(sys.argv)
win = MyApp()
win.show()
sys.exit(app.exec_())