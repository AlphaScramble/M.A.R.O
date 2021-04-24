from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from içerikarayüzü2 import Ui_ikinci_pencere_sinifi
import sys
import webbrowser
import speech_recognition as sr
import webbrowser
import mymodüles




class window2(QMainWindow):

    def __init__(self):

        super().__init__()

        #doğal değişken ve sınıftan tanımlama objeler
        """self.speak=sr.Recognizer() #sesin yazıya dönüştürülmesi için kullanılan obje
        self.mic=sr.Microphone() #mikrofonun açılması için kullanılan obje"""
        


        #ekran öğreleri ile ilgili işlemler
        self.ua=Ui_ikinci_pencere_sinifi()#ekran öğrelerinin bulunduğu widget sınıfı objeleri
        self.ua.setupUi(self)#ekran objelerinin çalışması.Self parametresi verildi çünkü mainwindow sınıfı üzerinde çalışması gerekiyor(Mainwindow objesi miraz olasak window2 sınıfına aktarıldı)

        #ikinci ekrana ait fonksiyonlar
        self.setWindowTitle("ana ekran 2")
        self.setWindowIcon(QIcon("resim.jpg"))
        #buttton connects 
        self.ua.maro.clicked.connect(self.ear)
    def ear(self):
        
        translation=mymodüles.speak()

        

        

        
        if "arama yap" in translation:
            print("şarta girdi")
            print("aramanızı yapabilirsiniz")
            arama=mymodüles.speak()


            
            url="https://google.com/search?q="+arama
            webbrowser.get().open(url)

        

            
            
            
            
            

        

    



    
    

            

            



        

        






    

    


        


    




        

        





        




