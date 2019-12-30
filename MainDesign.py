# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Guthub-Repo-Auto-Creator/MainDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchDirectoryButton.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.searchDirectoryButton.setDefault(True)
        self.searchDirectoryButton.setObjectName("searchDirectoryButton")
        self.searchDirectoryEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.searchDirectoryEntry.setGeometry(QtCore.QRect(50, 20, 571, 31))
        self.searchDirectoryEntry.setObjectName("searchDirectoryEntry")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 611, 91))
        self.groupBox.setObjectName("groupBox")
        self.commitMessageText = QtWidgets.QPlainTextEdit(self.groupBox)
        self.commitMessageText.setGeometry(QtCore.QRect(10, 20, 591, 61))
        self.commitMessageText.setObjectName("commitMessageText")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 611, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.readmeText = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.readmeText.setGeometry(QtCore.QRect(10, 20, 591, 131))
        self.readmeText.setObjectName("readmeText")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setEnabled(True)
        self.createButton.setGeometry(QtCore.QRect(490, 330, 121, 31))
        self.createButton.setObjectName("createButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 340, 91, 16))
        self.label.setObjectName("label")
        self.repoNameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.repoNameEntry.setGeometry(QtCore.QRect(120, 340, 241, 20))
        self.repoNameEntry.setObjectName("repoNameEntry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchDirectoryButton.setText(_translate("MainWindow", "*"))
        self.searchDirectoryEntry.setToolTip(_translate("MainWindow", "Enter the path to the Directory you want to create a Repository for"))
        self.searchDirectoryEntry.setPlaceholderText(_translate("MainWindow", "  DIR"))
        self.groupBox.setTitle(_translate("MainWindow", "Commit Message "))
        self.commitMessageText.setPlainText(_translate("MainWindow", "First Commit."))
        self.groupBox_2.setTitle(_translate("MainWindow", "README contents (./README.md) "))
        self.createButton.setText(_translate("MainWindow", "CREATE"))
        self.label.setText(_translate("MainWindow", "Repository Name: "))
        self.repoNameEntry.setPlaceholderText(_translate("MainWindow", "  NAME"))
