# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyGame.ui'
#
# Created: Wed Nov  9 08:17:43 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(700, 400)
        Window.setMinimumSize(QtCore.QSize(700, 400))
        Window.setMaximumSize(QtCore.QSize(700, 400))
        Window.setBaseSize(QtCore.QSize(700, 400))
        Window.setAutoFillBackground(False)
        Window.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.KopfLabel = QtWidgets.QLabel(Window)
        self.KopfLabel.setGeometry(QtCore.QRect(20, 20, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.KopfLabel.setFont(font)
        self.KopfLabel.setObjectName("KopfLabel")
        self.B01 = QtWidgets.QPushButton(Window)
        self.B01.setGeometry(QtCore.QRect(100, 100, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B01.setFont(font)
        self.B01.setStyleSheet("color: rgb(182, 113, 33);")
        self.B01.setObjectName("B01")
        self.B02 = QtWidgets.QPushButton(Window)
        self.B02.setGeometry(QtCore.QRect(200, 100, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B02.setFont(font)
        self.B02.setStyleSheet("color: rgb(182, 113, 33);")
        self.B02.setObjectName("B02")
        self.B04 = QtWidgets.QPushButton(Window)
        self.B04.setGeometry(QtCore.QRect(400, 100, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B04.setFont(font)
        self.B04.setStyleSheet("color: rgb(182, 113, 33);")
        self.B04.setObjectName("B04")
        self.B03 = QtWidgets.QPushButton(Window)
        self.B03.setGeometry(QtCore.QRect(300, 100, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B03.setFont(font)
        self.B03.setStyleSheet("color: rgb(182, 113, 33);")
        self.B03.setObjectName("B03")
        self.B05 = QtWidgets.QPushButton(Window)
        self.B05.setGeometry(QtCore.QRect(500, 100, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B05.setFont(font)
        self.B05.setStyleSheet("color: rgb(182, 113, 33);")
        self.B05.setObjectName("B05")
        self.B06 = QtWidgets.QPushButton(Window)
        self.B06.setGeometry(QtCore.QRect(200, 140, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B06.setFont(font)
        self.B06.setStyleSheet("color: rgb(182, 113, 33);")
        self.B06.setObjectName("B06")
        self.B09 = QtWidgets.QPushButton(Window)
        self.B09.setGeometry(QtCore.QRect(400, 140, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B09.setFont(font)
        self.B09.setStyleSheet("color: rgb(182, 113, 33);")
        self.B09.setObjectName("B09")
        self.B07 = QtWidgets.QPushButton(Window)
        self.B07.setGeometry(QtCore.QRect(100, 140, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B07.setFont(font)
        self.B07.setStyleSheet("color: rgb(182, 113, 33);")
        self.B07.setObjectName("B07")
        self.B08 = QtWidgets.QPushButton(Window)
        self.B08.setGeometry(QtCore.QRect(300, 140, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B08.setFont(font)
        self.B08.setStyleSheet("color: rgb(182, 113, 33);")
        self.B08.setObjectName("B08")
        self.B10 = QtWidgets.QPushButton(Window)
        self.B10.setGeometry(QtCore.QRect(500, 140, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B10.setFont(font)
        self.B10.setStyleSheet("color: rgb(182, 113, 33);")
        self.B10.setObjectName("B10")
        self.B12 = QtWidgets.QPushButton(Window)
        self.B12.setGeometry(QtCore.QRect(200, 180, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B12.setFont(font)
        self.B12.setStyleSheet("color: rgb(182, 113, 33);")
        self.B12.setObjectName("B12")
        self.B14 = QtWidgets.QPushButton(Window)
        self.B14.setGeometry(QtCore.QRect(400, 180, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B14.setFont(font)
        self.B14.setStyleSheet("color: rgb(182, 113, 33);")
        self.B14.setObjectName("B14")
        self.B11 = QtWidgets.QPushButton(Window)
        self.B11.setGeometry(QtCore.QRect(100, 180, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B11.setFont(font)
        self.B11.setStyleSheet("color: rgb(182, 113, 33);")
        self.B11.setObjectName("B11")
        self.B13 = QtWidgets.QPushButton(Window)
        self.B13.setGeometry(QtCore.QRect(300, 180, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B13.setFont(font)
        self.B13.setStyleSheet("color: rgb(182, 113, 33);")
        self.B13.setObjectName("B13")
        self.B15 = QtWidgets.QPushButton(Window)
        self.B15.setGeometry(QtCore.QRect(500, 180, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B15.setFont(font)
        self.B15.setStyleSheet("color: rgb(182, 113, 33);")
        self.B15.setObjectName("B15")
        self.EndeButton = QtWidgets.QPushButton(Window)
        self.EndeButton.setGeometry(QtCore.QRect(400, 260, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.EndeButton.setFont(font)
        self.EndeButton.setStyleSheet("background-color: rgb(255, 26, 26);\n"
"color: rgb(207, 207, 207);")
        self.EndeButton.setObjectName("EndeButton")
        self.NeuButton = QtWidgets.QPushButton(Window)
        self.NeuButton.setGeometry(QtCore.QRect(200, 260, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.NeuButton.setFont(font)
        self.NeuButton.setStyleSheet("background-color: rgb(0, 162, 10);\n"
"color: rgb(207, 207, 207);")
        self.NeuButton.setObjectName("NeuButton")
        self.OffenLabel = QtWidgets.QLabel(Window)
        self.OffenLabel.setGeometry(QtCore.QRect(100, 320, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.OffenLabel.setFont(font)
        self.OffenLabel.setObjectName("OffenLabel")
        self.KorrektLabel = QtWidgets.QLabel(Window)
        self.KorrektLabel.setGeometry(QtCore.QRect(100, 360, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.KorrektLabel.setFont(font)
        self.KorrektLabel.setObjectName("KorrektLabel")
        self.FalschLabel = QtWidgets.QLabel(Window)
        self.FalschLabel.setGeometry(QtCore.QRect(290, 340, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.FalschLabel.setFont(font)
        self.FalschLabel.setObjectName("FalschLabel")
        self.GeamtLabel = QtWidgets.QLabel(Window)
        self.GeamtLabel.setGeometry(QtCore.QRect(510, 360, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.GeamtLabel.setFont(font)
        self.GeamtLabel.setObjectName("GeamtLabel")
        self.SpielLabel = QtWidgets.QLabel(Window)
        self.SpielLabel.setGeometry(QtCore.QRect(510, 320, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SpielLabel.setFont(font)
        self.SpielLabel.setObjectName("SpielLabel")
        self.OLabel = QtWidgets.QLabel(Window)
        self.OLabel.setGeometry(QtCore.QRect(160, 320, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.OLabel.setFont(font)
        self.OLabel.setStyleSheet("color: rgb(0, 158, 153);")
        self.OLabel.setObjectName("OLabel")
        self.KLabel = QtWidgets.QLabel(Window)
        self.KLabel.setGeometry(QtCore.QRect(170, 360, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.KLabel.setFont(font)
        self.KLabel.setStyleSheet("color: rgb(0, 158, 153);")
        self.KLabel.setObjectName("KLabel")
        self.FLabel = QtWidgets.QLabel(Window)
        self.FLabel.setGeometry(QtCore.QRect(350, 340, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FLabel.setFont(font)
        self.FLabel.setStyleSheet("color: rgb(0, 158, 153);")
        self.FLabel.setObjectName("FLabel")
        self.SLabel = QtWidgets.QLabel(Window)
        self.SLabel.setGeometry(QtCore.QRect(570, 320, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SLabel.setFont(font)
        self.SLabel.setStyleSheet("color: rgb(0, 158, 153);")
        self.SLabel.setObjectName("SLabel")
        self.GLabel = QtWidgets.QLabel(Window)
        self.GLabel.setGeometry(QtCore.QRect(570, 360, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cousine")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.GLabel.setFont(font)
        self.GLabel.setStyleSheet("color: rgb(0, 158, 153);")
        self.GLabel.setObjectName("GLabel")
        self.line = QtWidgets.QFrame(Window)
        self.line.setGeometry(QtCore.QRect(100, 230, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Window)
        self.line_2.setGeometry(QtCore.QRect(100, 70, 481, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Window)
        self.line_3.setGeometry(QtCore.QRect(100, 300, 481, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Window)
        self.EndeButton.clicked.connect(Window.close)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MyGame"))
        self.KopfLabel.setText(_translate("Window", "Drücken Sie die Knöpfe in aufsteigender Reihnfolge!"))
        self.B01.setText(_translate("Window", "1"))
        self.B02.setText(_translate("Window", "2"))
        self.B04.setText(_translate("Window", "4"))
        self.B03.setText(_translate("Window", "3"))
        self.B05.setText(_translate("Window", "5"))
        self.B06.setText(_translate("Window", "7"))
        self.B09.setText(_translate("Window", "9"))
        self.B07.setText(_translate("Window", "6"))
        self.B08.setText(_translate("Window", "8"))
        self.B10.setText(_translate("Window", "10"))
        self.B12.setText(_translate("Window", "12"))
        self.B14.setText(_translate("Window", "14"))
        self.B11.setText(_translate("Window", "11"))
        self.B13.setText(_translate("Window", "13"))
        self.B15.setText(_translate("Window", "15"))
        self.EndeButton.setText(_translate("Window", "Ende"))
        self.NeuButton.setText(_translate("Window", "Neu"))
        self.OffenLabel.setText(_translate("Window", "Offen:"))
        self.KorrektLabel.setText(_translate("Window", "Korrect:"))
        self.FalschLabel.setText(_translate("Window", "Falsch:"))
        self.GeamtLabel.setText(_translate("Window", "Gesamt:"))
        self.SpielLabel.setText(_translate("Window", "Spiele:"))
        self.OLabel.setText(_translate("Window", "0"))
        self.KLabel.setText(_translate("Window", "0"))
        self.FLabel.setText(_translate("Window", "0"))
        self.SLabel.setText(_translate("Window", "0"))
        self.GLabel.setText(_translate("Window", "0"))
