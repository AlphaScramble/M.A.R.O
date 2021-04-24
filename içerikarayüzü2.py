# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'içerik_arayüzü.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ikinci_pencere_sinifi(object):
    def setupUi(self, ikinci_pencere_sinifi):
        ikinci_pencere_sinifi.setObjectName("ikinci_pencere_sinifi")
        ikinci_pencere_sinifi.resize(931, 845)
        self.centralwidget = QtWidgets.QWidget(ikinci_pencere_sinifi)
        self.centralwidget.setObjectName("centralwidget")
        self.maro = QtWidgets.QPushButton(self.centralwidget)
        self.maro.setGeometry(QtCore.QRect(10, 10, 111, 51))
        self.maro.setObjectName("maro")
        self.maro_2 = QtWidgets.QLabel(self.centralwidget)
        self.maro_2.setGeometry(QtCore.QRect(30, 40, 121, 51))
        self.maro_2.setText("")
        self.maro_2.setObjectName("maro_2")
        self.Kelime_kutusu = QtWidgets.QLineEdit(self.centralwidget)
        self.Kelime_kutusu.setGeometry(QtCore.QRect(730, 100, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Kelime_kutusu.setFont(font)
        self.Kelime_kutusu.setObjectName("Kelime_kutusu")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 80, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.kelime = QtWidgets.QLabel(self.centralwidget)
        self.kelime.setGeometry(QtCore.QRect(640, 100, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kelime.setFont(font)
        self.kelime.setObjectName("kelime")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 20, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.anlam_2 = QtWidgets.QLabel(self.centralwidget)
        self.anlam_2.setGeometry(QtCore.QRect(640, 150, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.anlam_2.setFont(font)
        self.anlam_2.setObjectName("anlam_2")
        self.anlam_kutusu = QtWidgets.QLineEdit(self.centralwidget)
        self.anlam_kutusu.setGeometry(QtCore.QRect(730, 150, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.anlam_kutusu.setFont(font)
        self.anlam_kutusu.setObjectName("anlam_kutusu")
        self.kelime_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.kelime_kaydet.setGeometry(QtCore.QRect(760, 200, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kelime_kaydet.setFont(font)
        self.kelime_kaydet.setObjectName("kelime_kaydet")
        self.yuz_tanima = QtWidgets.QPushButton(self.centralwidget)
        self.yuz_tanima.setGeometry(QtCore.QRect(130, 10, 121, 51))
        self.yuz_tanima.setObjectName("yuz_tanima")
        ikinci_pencere_sinifi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ikinci_pencere_sinifi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 26))
        self.menubar.setObjectName("menubar")
        ikinci_pencere_sinifi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ikinci_pencere_sinifi)
        self.statusbar.setObjectName("statusbar")
        ikinci_pencere_sinifi.setStatusBar(self.statusbar)

        self.retranslateUi(ikinci_pencere_sinifi)
        QtCore.QMetaObject.connectSlotsByName(ikinci_pencere_sinifi)

    def retranslateUi(self, ikinci_pencere_sinifi):
        _translate = QtCore.QCoreApplication.translate
        ikinci_pencere_sinifi.setWindowTitle(_translate("ikinci_pencere_sinifi", "MainWindow"))
        self.maro.setText(_translate("ikinci_pencere_sinifi", "M.A.R.O"))
        self.kelime.setText(_translate("ikinci_pencere_sinifi", "Kelime:"))
        self.label_4.setText(_translate("ikinci_pencere_sinifi", "İngilizce"))
        self.anlam_2.setText(_translate("ikinci_pencere_sinifi", "Anlamı:"))
        self.kelime_kaydet.setText(_translate("ikinci_pencere_sinifi", "KAYDET"))
        self.yuz_tanima.setText(_translate("ikinci_pencere_sinifi", "Yüz tanıma"))
