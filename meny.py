# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meny.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 794)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(10, 92, 143);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 240, 421, 71))
        self.label.setStyleSheet("font: 85 italic 30pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.user = QtWidgets.QPushButton(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(350, 340, 291, 91))
        self.user.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Times New Roman\";")
        self.user.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "     Личный кабинет"))
        self.user.setText(_translate("MainWindow", "Пользователь"))