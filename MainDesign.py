# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Guthub-Repo-Auto-Creator/MainDesign.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(630, 392)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.searchDirectoryButton = QtGui.QPushButton(self.centralwidget)
        self.searchDirectoryButton.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.searchDirectoryButton.setDefault(True)
        self.searchDirectoryButton.setObjectName(_fromUtf8("searchDirectoryButton"))
        self.searchDirectoryEntry = QtGui.QLineEdit(self.centralwidget)
        self.searchDirectoryEntry.setGeometry(QtCore.QRect(50, 20, 571, 31))
        self.searchDirectoryEntry.setObjectName(_fromUtf8("searchDirectoryEntry"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 611, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.commitMessageText = QtGui.QPlainTextEdit(self.groupBox)
        self.commitMessageText.setGeometry(QtCore.QRect(10, 20, 591, 61))
        self.commitMessageText.setObjectName(_fromUtf8("commitMessageText"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 611, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.readmeText = QtGui.QPlainTextEdit(self.groupBox_2)
        self.readmeText.setGeometry(QtCore.QRect(10, 20, 591, 131))
        self.readmeText.setObjectName(_fromUtf8("readmeText"))
        self.createButton = QtGui.QPushButton(self.centralwidget)
        self.createButton.setEnabled(True)
        self.createButton.setGeometry(QtCore.QRect(490, 330, 121, 31))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 340, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.repoNameEntry = QtGui.QLineEdit(self.centralwidget)
        self.repoNameEntry.setGeometry(QtCore.QRect(120, 340, 241, 20))
        self.repoNameEntry.setObjectName(_fromUtf8("repoNameEntry"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchDirectoryButton.setText(_translate("MainWindow", "*", None))
        self.searchDirectoryEntry.setToolTip(_translate("MainWindow", "Enter the path to the Directory you want to create a Repository for", None))
        self.searchDirectoryEntry.setPlaceholderText(_translate("MainWindow", "  DIR", None))
        self.groupBox.setTitle(_translate("MainWindow", "Commit Message ", None))
        self.commitMessageText.setPlainText(_translate("MainWindow", "First Commit.", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "README contents (./README.md) ", None))
        self.createButton.setText(_translate("MainWindow", "CREATE", None))
        self.label.setText(_translate("MainWindow", "Repository Name: ", None))
        self.repoNameEntry.setPlaceholderText(_translate("MainWindow", "  NAME", None))

