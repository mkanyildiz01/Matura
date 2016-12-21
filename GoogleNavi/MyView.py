# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoogleNavigation.ui'
#
# Created: Tue Nov 22 11:10:22 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoogleNavigation(object):
    def setupUi(self, GoogleNavigation):
        GoogleNavigation.setObjectName("GoogleNavigation")
        GoogleNavigation.resize(887, 467)
        self.l1 = QtWidgets.QLabel(GoogleNavigation)
        self.l1.setGeometry(QtCore.QRect(30, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(GoogleNavigation)
        self.l2.setGeometry(QtCore.QRect(30, 70, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(GoogleNavigation)
        self.l3.setGeometry(QtCore.QRect(30, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.tstart = QtWidgets.QLineEdit(GoogleNavigation)
        self.tstart.setGeometry(QtCore.QRect(90, 70, 761, 31))
        self.tstart.setObjectName("tstart")
        self.tziel = QtWidgets.QLineEdit(GoogleNavigation)
        self.tziel.setGeometry(QtCore.QRect(90, 110, 761, 31))
        self.tziel.setObjectName("tziel")
        self.bsubmit = QtWidgets.QPushButton(GoogleNavigation)
        self.bsubmit.setGeometry(QtCore.QRect(30, 420, 401, 27))
        self.bsubmit.setObjectName("bsubmit")
        self.breset = QtWidgets.QPushButton(GoogleNavigation)
        self.breset.setGeometry(QtCore.QRect(440, 420, 201, 27))
        self.breset.setObjectName("breset")
        self.bclose = QtWidgets.QPushButton(GoogleNavigation)
        self.bclose.setGeometry(QtCore.QRect(650, 420, 201, 27))
        self.bclose.setObjectName("bclose")
        self.tergebnis = QtWidgets.QTextEdit(GoogleNavigation)
        self.tergebnis.setGeometry(QtCore.QRect(30, 150, 821, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tergebnis.setFont(font)
        self.tergebnis.setObjectName("tergebnis")


        self.retranslateUi(GoogleNavigation)
        self.bclose.clicked.connect(GoogleNavigation.close)
        self.breset.clicked.connect(self.tstart.clear)
        self.breset.clicked.connect(self.tziel.clear)
        self.breset.clicked.connect(self.tergebnis.clear)
        QtCore.QMetaObject.connectSlotsByName(GoogleNavigation)

    def retranslateUi(self, GoogleNavigation):
        _translate = QtCore.QCoreApplication.translate
        GoogleNavigation.setWindowTitle(_translate("GoogleNavigation", "Google Navigation"))
        self.l1.setText(_translate("GoogleNavi", "Google Navi"))
        self.l2.setText(_translate("GoogleNavigation", "Start:"))
        self.l3.setText(_translate("GoogleNavigation", "Ziel:"))
        self.bsubmit.setText(_translate("GoogleNavigation", "submit"))
        self.breset.setText(_translate("GoogleNavigation", "reset"))
        self.bclose.setText(_translate("GoogleNavigation", "close"))
        self.tergebnis.setHtml(_translate("GoogleNavigation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))