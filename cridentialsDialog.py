# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Guthub-Repo-Auto-Creator/cridentialsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 154)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.doneButton = QtWidgets.QPushButton(Dialog)
        self.doneButton.setGeometry(QtCore.QRect(230, 110, 75, 23))
        self.doneButton.setObjectName("doneButton")
        self.showButton = QtWidgets.QPushButton(Dialog)
        self.showButton.setGeometry(QtCore.QRect(130, 110, 75, 23))
        self.showButton.setObjectName("showButton")
        self.userNameEntry = QtWidgets.QLineEdit(Dialog)
        self.userNameEntry.setGeometry(QtCore.QRect(80, 20, 241, 20))
        self.userNameEntry.setObjectName("userNameEntry")
        self.passwordEntry = QtWidgets.QLineEdit(Dialog)
        self.passwordEntry.setGeometry(QtCore.QRect(80, 60, 241, 20))
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setObjectName("passwordEntry")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Credentials Dialog"))
        self.label.setText(_translate("Dialog", "User Name: "))
        self.doneButton.setText(_translate("Dialog", "Done"))
        self.showButton.setText(_translate("Dialog", "show"))
        self.label_2.setText(_translate("Dialog", "Password: "))
