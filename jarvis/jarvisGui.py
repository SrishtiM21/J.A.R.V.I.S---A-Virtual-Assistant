from jarvisui import Ui_jarvisUI
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import Main
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        Main.wishMe()
        Main.taskexe()
        

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.gui = Ui_jarvisUI()
        self.gui.setupUi(self)

        self.gui.push_start.clicked.connect(self.startTask)
        self.gui.push_exit.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("..//..//G.U.I Material-20221121T175203Z-001//G.U.I Material//ExtraGui//live.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()


        self.gui.label2 = QtGui.QMovie("..//..//G.U.I Material-20221121T175203Z-001//G.U.I Material//ExtraGui//Code_Template.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()


        self.gui.label3 = QtGui.QMovie("..//..//G.U.I Material-20221121T175203Z-001//G.U.I Material//B.G//Iron_Template_1.gif")
        self.gui.gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time :" + time
        label_date = "Date :" + date

        self.gui.text_time.setText(label_time)
        self.gui.text_date.setText(label_date)


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())
