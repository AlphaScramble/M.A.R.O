# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Giriş_arayüzü.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Kullanici_adi = QtWidgets.QLineEdit(self.centralwidget)
        self.Kullanici_adi.setGeometry(QtCore.QRect(220, 50, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Kullanici_adi.setFont(font)
        self.Kullanici_adi.setObjectName("Kullanici_adi")
        self.Sifre = QtWidgets.QLineEdit(self.centralwidget)
        self.Sifre.setGeometry(QtCore.QRect(220, 90, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sifre.setFont(font)
        self.Sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Sifre.setObjectName("Sifre")
        self.kullanci_button = QtWidgets.QPushButton(self.centralwidget)
        self.kullanci_button.setGeometry(QtCore.QRect(220, 130, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kullanci_button.setFont(font)
        self.kullanci_button.setObjectName("kullanci_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 20, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 90, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Ziyaretci_girisi = QtWidgets.QLineEdit(self.centralwidget)
        self.Ziyaretci_girisi.setGeometry(QtCore.QRect(570, 90, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ziyaretci_girisi.setFont(font)
        self.Ziyaretci_girisi.setObjectName("Ziyaretci_girisi")
        self.ziyaretci_button = QtWidgets.QPushButton(self.centralwidget)
        self.ziyaretci_button.setGeometry(QtCore.QRect(570, 130, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ziyaretci_button.setFont(font)
        self.ziyaretci_button.setObjectName("ziyaretci_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M.A.R.O"))
        self.label.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.kullanci_button.setText(_translate("MainWindow", "GİRİŞ"))
        self.label_3.setText(_translate("MainWindow", "Ziyaretçi Girişi"))
        self.label_4.setText(_translate("MainWindow", "Ziyaretçi Adı:"))
        self.ziyaretci_button.setText(_translate("MainWindow", "GÖNDER"))
