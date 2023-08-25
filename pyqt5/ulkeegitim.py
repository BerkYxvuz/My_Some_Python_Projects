from PyQt5 import QtWidgets
import sys
from ulkeegitimform import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioturk.setChecked(True)
        self.ui.radiolise.setChecked(True)

        self.ui.radioturk.toggled.connect(self.onClickedUlke)
        self.ui.radioazer.toggled.connect(self.onClickedUlke)
        self.ui.radioyunan.toggled.connect(self.onClickedUlke)
        self.ui.radioalman.toggled.connect(self.onClickedUlke)

        self.ui.radiolise.toggled.connect(self.onClickedEgitim)
        self.ui.radiouni.toggled.connect(self.onClickedEgitim)
        self.ui.radioyukseklis.toggled.connect(self.onClickedUlke)
        self.ui.radioilkok.toggled.connect(self.onClickedUlke)

        self.ui.ulkebutn.clicked.connect(self.getSelectedUlke)
        self.ui.egitimbuton.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print(f'Seçilen Ülke: {rb.text()}')

    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print(f'Seçilen Eğitim: {rb.text()}')

    def getSelectedUlke(self):
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)
        for x in items:
            if x.isChecked():
                self.ui.labelulke.setText('Seçilen Ülke: ' + x.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBox_2.findChildren(QtWidgets.QRadioButton)
        for x in items:
            if x.isChecked():
                self.ui.labelegitim.setText('Seçilen Ülke: ' + x.text())


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())