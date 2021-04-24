from PyQt5.QtWidgets import QApplication
import sys
from main_window import window1





app=QApplication(sys.argv)
win=window1()
win.show()
exit(app.exec_())
