from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout
)
import random

class Window1(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(500,300,400,450)
        self.setWindowTitle("O'yin")
        self.setStyleSheet("background-color:orange")

        self.start=QPushButton("START")
        self.close_btn=QPushButton("CLOSE")
        self.reset=QPushButton("RESTART")

        self.grid= QGridLayout()
        self.h_lay= QHBoxLayout()
        self.v_lay= QVBoxLayout()


        self.btn1=QPushButton("1")
        self.btn2=QPushButton("2")
        self.btn3=QPushButton("3")
        self.btn4=QPushButton("4")
        self.btn5=QPushButton("5")
        self.btn6=QPushButton("6")
        self.btn7=QPushButton("7")
        self.btn8=QPushButton("8")
        self.btn9=QPushButton("9")
        self.btn10=QPushButton("10")
        self.btn11=QPushButton("11")
        self.btn12=QPushButton("12")
        self.btn13=QPushButton("13")
        self.btn14=QPushButton("14")
        self.btn15=QPushButton("15")
        self.btn16=QPushButton("")

        self.btn1.clicked.connect(self.alsh1)
        self.btn2.clicked.connect(self.alsh2)
        self.btn3.clicked.connect(self.alsh3)
        self.btn4.clicked.connect(self.alsh4)
        self.btn5.clicked.connect(self.alsh5)
        self.btn6.clicked.connect(self.alsh6)
        self.btn7.clicked.connect(self.alsh7)
        self.btn8.clicked.connect(self.alsh8)
        self.btn9.clicked.connect(self.alsh9)
        self.btn10.clicked.connect(self.alsh10)
        self.btn11.clicked.connect(self.alsh11)
        self.btn12.clicked.connect(self.alsh12)
        self.btn13.clicked.connect(self.alsh13)
        self.btn14.clicked.connect(self.alsh14)
        self.btn15.clicked.connect(self.alsh15)
        self.btn16.clicked.connect(self.alsh16)


        self.str_style = """QPushButton {
            color:black;
            background-color:white;
            font: bold 12pt}"""

        self.start.setFixedSize(140,50)
        self.start.setStyleSheet(self.str_style)
        self.start.clicked.connect(self.star)

        self.reset.setFixedSize(140,50)
        self.reset.setStyleSheet(self.str_style)
        self.reset.clicked.connect(self.res)

        self.close_btn.setFixedSize(140,50)
        self.close_btn.setStyleSheet(self.str_style)
        self.close_btn.clicked.connect(self.chiqish)
            

        self.lst=[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]
        self.ash=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]
        self.a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]

        index=0
        for i in range(4):
            for j in range(4):
                self.grid.addWidget(self.lst[index],i,j)
                self.lst[index].setFixedSize(100,100)
                self.lst[index].setStyleSheet(self.str_style)
                index+=1
       
       
        self.h_lay.addWidget(self.close_btn)
        self.h_lay.addWidget(self.reset)
        self.h_lay.addWidget(self.start)

        self.v_lay.addLayout(self.grid)
        self.v_lay.addLayout(self.h_lay)

        self.setLayout(self.v_lay)
        self.show()

    def res(self):
        for i in range(len(self.lst)):
            self.lst[i].setText(f'{self.a[i]}')


    def star(self):
        random.shuffle(self.ash)
        for i in range(len(self.lst)):
            self.lst[i].setText(f'{self.ash[i]}')

    def chiqish(self):
        self.close()

    def alsh1(self):
        k=self.btn1.text()
        if self.btn2.text()==" ":
            self.btn1.setText(" ")
            self.btn2.setText(k)
        elif self.btn5.text()==" ":
            self.btn1.setText(" ")
            self.btn5.setText(k)

    def alsh2(self):
        k=self.btn2.text()
        if self.btn1.text()==" ":
            self.btn2.setText(" ")
            self.btn1.setText(k)
        elif self.btn3.text()==" ":
            self.btn2.setText(" ")
            self.btn3.setText(k)
        elif self.btn6.text()==" ":
            self.btn2.setText(" ")
            self.btn6.setText(k)

    def alsh3(self):
        k=self.btn3.text()
        if self.btn2.text()==" ":
            self.btn2.setText(k)
            self.btn3.setText(" ")
        elif self.btn4.text()==" ":
            self.btn4.setText(k)
            self.btn3.setText(" ")
        elif self.btn7.text()==" ":
            self.btn7.setText(k)
            self.btn3.setText(" ")

    def alsh4(self):
        k=self.btn4.text()
        if self.btn3.text()==" ":
            self.btn3.setText(k)
            self.btn4.setText(" ")
        elif self.btn8.text()==" ":
            self.btn8.setText(k)
            self.btn4.setText(" ")
        
    def alsh5(self):
        k=self.btn5.text()
        if self.btn1.text()==" ":
            self.btn1.setText(k)
            self.btn5.setText( " ")
        elif self.btn6.text()==" ":
            self.btn6.setText(k)
            self.btn5.setText(" ")
        elif self.btn9.text()==" ":
            self.btn9.setText(k)
            self.btn5.setText(" ")

    def alsh6(self):
        k=self.btn6.text()
        if self.btn2.text()==" ":
            self.btn2.setText(k)
            self.btn6.setText( " ")
        elif self.btn5.text()==" ":
            self.btn5.setText(k)
            self.btn6.setText(" ")
        elif self.btn7.text()==" ":
            self.btn7.setText(k)
            self.btn6.setText(" ")
        elif self.btn10.text()==" ":
            self.btn10.setText(k)
            self.btn6.setText(" ")

    def alsh7(self):
        k=self.btn7.text()
        if self.btn3.text()==" ":
            self.btn3.setText(k)
            self.btn7.setText( " ")
        elif self.btn6.text()==" ":
            self.btn6.setText(k)
            self.btn7.setText(" ")
        elif self.btn8.text()==" ":
            self.btn8.setText(k)
            self.btn7.setText(" ")
        elif self.btn11.text()==" ":
            self.btn11.setText(k)
            self.btn7.setText(" ")

    def alsh8(self):
        k=self.btn8.text()
        if self.btn4.text()==" ":
            self.btn4.setText(k)
            self.btn8.setText( " ")
        elif self.btn7.text()==" ":
            self.btn7.setText(k)
            self.btn8.setText(" ")
        elif self.btn12.text()==" ":
            self.btn12.setText(k)
            self.btn8.setText(" ")

    def alsh9(self):
        k=self.btn9.text()
        if self.btn5.text()==" ":
            self.btn5.setText(k)
            self.btn9.setText( " ")
        elif self.btn10.text()==" ":
            self.btn10.setText(k)
            self.btn9.setText(" ")
        elif self.btn13.text()==" ":
            self.btn13.setText(k)
            self.btn9.setText(" ")
            
    def alsh10(self):
        k=self.btn10.text()
        if self.btn9.text()==" ":
            self.btn9.setText(k)
            self.btn10.setText( " ")
        elif self.btn6.text()==" ":
            self.btn6.setText(k)
            self.btn10.setText(" ")
        elif self.btn14.text()==" ":
            self.btn14.setText(k)
            self.btn10.setText(" ")
        elif self.btn11.text()==" ":
            self.btn11.setText(k)
            self.btn10.setText(" ")

    def alsh11(self):
        k=self.btn11.text()
        if self.btn7.text()==" ":
            self.btn7.setText(k)
            self.btn11.setText( " ")
        elif self.btn10.text()==" ":
            self.btn10.setText(k)
            self.btn11.setText(" ")
        elif self.btn12.text()==" ":
            self.btn12.setText(k)
            self.btn11.setText(" ")
        elif self.btn15.text()==" ":
            self.btn15.setText(k)
            self.btn11.setText(" ")

    def alsh12(self):
        k=self.btn12.text()
        if self.btn8.text()==" ":
            self.btn8.setText(k)
            self.btn12.setText( " ")
        elif self.btn11.text()==" ":
            self.btn11.setText(k)
            self.btn12.setText(" ")
        elif self.btn16.text()==" ":
            self.btn16.setText(k)
            self.btn12.setText(" ")

    def alsh14(self):
        k=self.btn14.text()
        if self.btn15.text()==" ":
            self.btn15.setText(k)
            self.btn14.setText( " ")
        elif self.btn10.text()==" ":
            self.btn10.setText(k)
            self.btn14.setText(" ")
        elif self.btn13.text()==" ":
            self.btn13.setText(k)
            self.btn14.setText(" ")

    def alsh15(self):
        k=self.btn15.text()
        if self.btn11.text()==" ":
            self.btn11.setText(k)
            self.btn15.setText( " ")
        elif self.btn14.text()==" ":
            self.btn14.setText(k)
            self.btn15.setText(" ")
        elif self.btn16.text()==" ":
            self.btn16.setText(k)
            self.btn15.setText(" ")

    def alsh16(self):
        k=self.btn16.text()
        if self.btn12.text()==" ":
            self.btn12.setText(k)
            self.btn16.setText( " ")
        elif self.btn15.text()==" ":
            self.btn15.setText(k)
            self.btn16.setText(" ")

    def alsh13(self):
        k=self.btn13.text()
        if self.btn14.text()==" ":
            self.btn14.setText(k)
            self.btn13.setText( " ")
        elif self.btn9.text()==" ":
            self.btn9.setText(k)
            self.btn13.setText(" ")

        
