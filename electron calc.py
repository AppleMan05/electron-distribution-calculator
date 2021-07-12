
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mendeleev import *

global x 
x = "Test"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(242, 80, 121, 36))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 341, 41))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(33, 90, 191, 20))
        self.label_2.setObjectName("label_2")
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(290, 220, 111, 23))
        self.checkBox.setObjectName("checkBox")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 91, 36))
        self.pushButton.setObjectName("pushButton")
        text1 = self.lineEdit.text()
        

        self.pushButton.clicked.connect(lambda: self.calculation(text1))
        print(text1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Electron Distribution Calculator"))
        self.label.setText(_translate("MainWindow", "Electron Distribution Calculator"))
        self.label_2.setText(_translate("MainWindow", "Enter symbol/name of element:"))
        self.checkBox.setText(_translate("MainWindow", "Toggle music"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
    
    def clicked(self, input):
        self.label_2.setText("Test")
        self.update()



    def calculation(self, text):
        while True:
            text1 = self.lineEdit.text()
            user_input = element(text1)

            atomic_no_of_input = user_input.atomic_number
            output_var = user_input.ec.conf
            break
        l=[]
        for x, c in output_var.items():
            inner_tuple = x
            second_value = c
            t = f"{str(inner_tuple[0]) + inner_tuple[1]}^{second_value}"
            l.append(t)
        
        msg = QMessageBox()
        msg.setWindowTitle(user_input.name)
        #test3 = calculation(text1)
        msg.setText(" ".join(l))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("This is the basic output you needed.")
        msg.setDetailedText(user_input.description)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
