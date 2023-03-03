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


class Window2(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ro'yxatdan o'tish ")

        self.mes_box=QMessageBox()
        self.mes_box.setGeometry(100, 100, 250, 250)

        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.h1_box=QHBoxLayout()
        self.h2_box=QHBoxLayout()
        self.h3_box=QHBoxLayout()
        self.h4_box=QHBoxLayout()


        #Button
        self.btn_saqlash=QPushButton('SAQLASH')
        self.btn_saqlash.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : blue;"
                             "}")
        self.btn_saqlash.clicked.connect(self.file_open)



        # Ism qatori
        self.fname_label=QLabel('Ismingiz')
        self.fname_line=QLineEdit()

        #Familiya qatori
        self.lname_label=QLabel('Familiyangiz')
        self.lname_line=QLineEdit()

        #Login
        self.login_label1=QLabel('Login')
        self.login_line1=QLineEdit()

        #parol
        self.parol_label1=QLabel('Parol')
        self.parol_line1=QLineEdit()

        #Gorizontal Ism Qator
        self.h_box.addWidget(self.fname_label)
        self.h_box.addWidget(self.fname_line)

        #Gorizontal FAmiliya Qator
        self.h1_box.addWidget(self.lname_label)
        self.h1_box.addWidget(self.lname_line)

        #Gorizontal Login qayor
        self.h2_box.addWidget(self.login_label1)
        self.h2_box.addWidget(self.login_line1)

        #Gorizontal PArol qator
        self.h3_box.addWidget(self.parol_label1)
        self.h3_box.addWidget(self.parol_line1)

        
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h1_box)
        self.v_box.addLayout(self.h2_box)
        self.v_box.addLayout(self.h3_box)
        self.v_box.addWidget(self.btn_saqlash)

        
        self.setLayout(self.v_box)


    def file_open(self):
        cor= Core()
        
        
        if not cor.getuser(self.login_line1.text()):
            self.mes_box.setWindowTitle('Error')
            self.mes_box.setText("Bu login egallangan")
            self.mes_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel )
        
            returnValue = self.mes_box.exec()
            self.login_line1.setText('')
            self.parol_line1.setText('')
            
            
        elif len(self.parol_line1.text())<8:
            self.mes_box.setWindowTitle('Error')
            self.mes_box.setText("Parol 8 ta xonadan iborat qo'lishi kerak")
            self.mes_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel )
            
            returnValue = self.mes_box.exec()
            self.parol_line1.setText('')
            
        else:
            cor.createuser(self.fname_line.text(), self.lname_line.text(),self.login_line1.text(), self.parol_line1.text())
            self.close()
