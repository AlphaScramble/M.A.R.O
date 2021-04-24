from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from girişarayüzü import Ui_MainWindow
import sys
from second_window import window2
from pygame import mixer
import yts


class window1(QMainWindow):

    def __init__(self):
        super(window1,self).__init__()
        #defult password and username
        self.username="börü"
        self.password="maro"
        #main window function and method
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("fusion")
        #password and username screan's connects 
        self.ui.kullanci_button.clicked.connect(self.click)
        #İkinci ekranın yapısal kodları
        self.ikinci_ekran=window2()

    def click(self):

        yts.take_photos()


        
        if self.username==self.ui.Kullanici_adi.text() and self.password==self.ui.Sifre.text():
            self.ikinci_ekran.show()
            self.close()
            mixer.init()
            mixer.music.load("audio.mp3")
            mixer.music.play()

        if self.username != self.ui.Kullanici_adi.text() or self.password!=self.ui.Sifre.text():
            pass

            