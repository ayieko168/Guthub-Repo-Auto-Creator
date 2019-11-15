# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Guthub-Repo-Auto-Creator/cridentialsDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(346, 154)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.doneButton = QtGui.QPushButton(Dialog)
        self.doneButton.setGeometry(QtCore.QRect(230, 110, 75, 23))
        self.doneButton.setObjectName(_fromUtf8("doneButton"))
        self.showButton = QtGui.QPushButton(Dialog)
        self.showButton.setGeometry(QtCore.QRect(130, 110, 75, 23))
        self.showButton.setObjectName(_fromUtf8("showButton"))
        self.userNameEntry = QtGui.QLineEdit(Dialog)
        self.userNameEntry.setGeometry(QtCore.QRect(80, 20, 241, 20))
        self.userNameEntry.setObjectName(_fromUtf8("userNameEntry"))
        self.passwordEntry = QtGui.QLineEdit(Dialog)
        self.passwordEntry.setGeometry(QtCore.QRect(80, 60, 241, 20))
        self.passwordEntry.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEntry.setObjectName(_fromUtf8("passwordEntry"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Credentials Dialog", None))
        self.label.setText(_translate("Dialog", "User Name: ", None))
        self.doneButton.setText(_translate("Dialog", "Done", None))
        self.showButton.setText(_translate("Dialog", "show", None))
        self.label_2.setText(_translate("Dialog", "Password: ", None))

