import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "CharacterBuilder.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    proficiency = 2

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.athletics_radioButton.clicked.connect(self.calculate_skill)
        self.acrobatics_radioButton.clicked.connect(self.calculate_skill)
        self.animal_handling_radioButton.clicked.connect(self.calculate_skill)
        self.arcana_radioButton.clicked.connect(self.calculate_skill)
        self.deception_radioButton.clicked.connect(self.calculate_skill)

    def calculate_skill(self):
        if self.athletics_radioButton.isChecked():
            self.athletics_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.athletics_lineEdit.setText("+{}".format(0))
        # end-if
        if self.acrobatics_radioButton.isChecked():
            self.acrobatics_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.acrobatics_lineEdit.setText("+{}".format(0))
        # end-if
        if self.animal_handling_radioButton.isChecked():
            self.animal_handling_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.animal_handling_lineEdit.setText("+{}".format(0))
        # end-if
        if self.arcaba_radioButton.isChecked():
            self.arcana_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.arcana_lineEdit.setText("+{}".format(0))
        # end-if

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
