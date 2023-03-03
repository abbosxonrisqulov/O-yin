import sys 

from kirish import Window1
from royxatdan_otish import Window2
from dboyin import Core

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Xush kelibsiz')
        self.setGeometry(100,100, 250, 250)

        self.m_box=QMessageBox()

        #label
        self.login_label=QLabel("Login")
        self.parol_label=QLabel('Parol')
        self.error=QLabel("Parol 8 ta belgidan\n iborat bo'lishi kerak")


        #line edit
        self.login_line=QLineEdit()
        self.parol_line=QLineEdit()

        #Button Kirish
        self.btn_kirish=QPushButton("KIRISH")
        self.btn_kirish.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : blue;"
                             "}")
        self.btn_kirish.clicked.connect(self.clickbutton)


        #Button Ro'yxatdan o'tish
        self.btn_royxatdan_otish=QPushButton("Ro'yxatdan o'tish")
        self.btn_royxatdan_otish.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : red;"
                             "}")
        self.btn_royxatdan_otish.clicked.connect(self.royxat)



        self.v_box=QVBoxLayout()
        self.g_box=QHBoxLayout()
        self.g1_box=QHBoxLayout()

        #login qatori
        self.g_box.addWidget(self.login_label)
        self.g_box.addWidget(self.login_line)

        #parol qatori
        self.g1_box.addWidget(self.parol_label)
        self.g1_box.addWidget(self.parol_line)


        self.v_box.addLayout(self.g_box)
        self.v_box.addLayout(self.g1_box)
        self.v_box.addWidget(self.btn_kirish)
        self.v_box.addWidget(self.btn_royxatdan_otish)


        self.setLayout(self.v_box)

        
    def clickbutton(self,checked):
        cor=Core()
        self.w1=Window1()
        
        
        if cor.getUserloginandparol(self.login_line.text(),self.parol_line.text()):
            self.w1.show()
            self.hide()
                
                
        else :
            self.m_box.setWindowTitle('Error')
            self.m_box.setText("Parol yoki Login xato")
            self.m_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel )
            returnValue = self.m_box.exec()
            self.login_line.setText('')
            self.parol_line.setText('')


    def royxat(self):
        self.win2=Window2()
        self.win2.show()
        self.hide()
        
        
app = QApplication([])
win = Window()
win.show()
sys.exit(app.exec_())



