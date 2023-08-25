import checkboxform
import sys
from PyQt5 import QtWidgets
from checkboxform import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbsinema.stateChanged.connect(self.show_state)
        self.ui.cbkitapokuma.stateChanged.connect(self.show_state)
        self.ui.cbspor.stateChanged.connect(self.show_state)
        self.ui.pushButton.clicked.connect(self.getAllChecked)

        self.ui.cbsinema_2.stateChanged.connect(self.show_state)
        self.ui.cbkitapokuma_2.stateChanged.connect(self.show_state)
        self.ui.cbspor_2.stateChanged.connect(self.show_state)
        self.ui.pushButton_2.clicked.connect(self.getAllChecked_2)


    def getAllChecked(self):
        result = ''
        items = self.ui.groupBox.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        self.ui.label.setText(result)

    def getAllChecked_2(self):
        result = ''
        items = self.ui.groupBox_2.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        self.ui.label_2.setText(result)

    def show_state(self, value):
        pass

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()