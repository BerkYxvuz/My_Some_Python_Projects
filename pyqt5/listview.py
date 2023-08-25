from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
from listviewform import Ui_MainWindow
from PyQt5.QtWidgets import QLineEdit, QMessageBox
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load students
        self.LoadStudents()
        # add New Student
        self.ui.Add.clicked.connect(self.addStudent)
        # edit student
        self.ui.Edit.clicked.connect(self.editStudent)
        # delete student
        self.ui.Remove.clicked.connect(self.removeStudent)
        # up student
        self.ui.Up.clicked.connect(self.upStudent)
        # down student
        self.ui.Down.clicked.connect(self.downStudent)
        # sort
        self.ui.sort.clicked.connect(self.sortStudents)
        # exit
        self.ui.exit.clicked.connect(self.close)
    def LoadStudents(self):
        self.ui.listitem.addItems(['Ahmet', 'Ali', 'Çınar'])
        self.ui.listitem.setCurrentRow(0)

    def addStudent(self):
        text, ok = QInputDialog.getText(self, 'New Student', 'Student Name')
        if ok and text is not None:
            self.ui.listitem.insertItem(0, text)
    def editStudent(self):
        index = self.ui.listitem.currentRow()
        item = self.ui.listitem.item(index)
        if item is not None:
            text, ok = QInputDialog.getText(self, 'Edit Student', 'Student Name', QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
    def removeStudent(self):
        index = self.ui.listitem.currentRow()
        item = self.ui.listitem.item(index)
        if item is None:
            return
        q = QMessageBox.question(self, "Remove Student", "Do you want to remove student ? " + str(item.text()), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listitem.takeItem(index)
            del item
    def upStudent(self):
        index = self.ui.listitem.currentRow()
        item = self.ui.listitem.item(index)
        if index >= 1:
            item = self.ui.listitem.takeItem(index)
            self.ui.listitem.insertItem(index-1, item)
            self.ui.listitem.setCurrentItem(item)
    def downStudent(self):
        index = self.ui.listitem.currentRow()
        item = self.ui.listitem.item(index)
        if index >= 0:
            item = self.ui.listitem.takeItem(index)
            self.ui.listitem.insertItem(index+1, item)
            self.ui.listitem.setCurrentItem(item)
    def sortStudents(self):
        self.ui.listitem.sortItems()
    def close(self):
        quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()