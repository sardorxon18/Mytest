from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 350)

        self.v_main_lay = QVBoxLayout()
        self.h_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.grid_lay = QGridLayout()

        self.navbat = 1

        self.msg = QMessageBox()

        self.btn1 = QPushButton()
        self.btn1.clicked.connect(lambda: self.clicker(self.btn1))

        self.btn2 = QPushButton()
        self.btn2.clicked.connect(lambda: self.clicker(self.btn2))
        
        self.btn3 = QPushButton()
        self.btn3.clicked.connect(lambda: self.clicker(self.btn3))
        
        self.btn4 = QPushButton()
        self.btn4.clicked.connect(lambda: self.clicker(self.btn4))
        
        self.btn5 = QPushButton()
        self.btn5.clicked.connect(lambda: self.clicker(self.btn5))
        
        self.btn6 = QPushButton()
        self.btn6.clicked.connect(lambda: self.clicker(self.btn6))
        
        self.btn7 = QPushButton()
        self.btn7.clicked.connect(lambda: self.clicker(self.btn7))
        
        self.btn8 = QPushButton()
        self.btn8.clicked.connect(lambda: self.clicker(self.btn8))
        
        self.btn9 = QPushButton()
        self.btn9.clicked.connect(lambda: self.clicker(self.btn9))
        
        self.btns_list = [self.btn1, self.btn2,self.btn3, self.btn4,self.btn5, self.btn6,self.btn7, self.btn8, self.btn9]

        self.lbl = QLabel(">>>X<<<")
        self.lbl.setStyleSheet("font-weight:bold; font-size: 20px")

        self.reset_btn = QPushButton("RESET")
        self.reset_btn.clicked.connect(self.reset)

        self.exit_btn = QPushButton("EXIT")
        self.exit_btn.clicked.connect(exit)

        self.str_style = """QPushButton{
            color:red;
            background:silver;
            border: 1px solid black;
            border-radius: 50%;
            font: bold 12pt;
        }"""

        index=0
        for i in range(3):
            for j in range(3):
                self.btns_list[index].setStyleSheet(self.str_style)
                self.btns_list[index].setFixedSize(96,90)
                self.grid_lay.addWidget(self.btns_list[index],i,j)
                index+=1

        self.h_lay.addStretch()
        self.h_lay.addWidget(self.lbl)
        self.h_lay.addStretch()

        self.h_btn_lay.addWidget(self.reset_btn)
        self.h_btn_lay.addWidget(self.exit_btn)

        self.v_main_lay.addLayout(self.grid_lay)
        self.v_main_lay.addLayout(self.h_lay)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def disable(self, natija: bool):
        for i in self.btns_list:
            i.setDisabled(natija)

    def win(self, a:QPushButton, b, c):
        str_style = """QPushButton{
            color:floralwhite;
            background:darkgreen;
            border: 1px solid black;
            border-radius: 50%;
            font: bold 12pt;
        }"""
        a.setStyleSheet(str_style)
        b.setStyleSheet(str_style)
        c.setStyleSheet(str_style)

        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setText(f"{a.text()} IS WINNER")
        self.msg.buttonClicked.connect(self.reset)
        self.msg.exec_()

        self.disable(True)


    def checkWin(self):
        # horizontal
        if(self.btn1.text()!="" and self.btn1.text() == self.btn2.text() and self.btn1.text() == self.btn3.text()):
            self.win(self.btn1, self.btn2, self.btn3)
        elif(self.btn4.text()!="" and self.btn4.text() == self.btn5.text() and self.btn4.text() == self.btn6.text()):
            self.win(self.btn4, self.btn5, self.btn6)
        elif(self.btn7.text()!="" and self.btn7.text() == self.btn8.text() and self.btn8.text() == self.btn9.text()):
            self.win(self.btn7, self.btn8, self.btn9)
        # vertical
        elif(self.btn1.text()!="" and self.btn1.text() == self.btn4.text() and self.btn4.text() == self.btn7.text()):
            self.win(self.btn1, self.btn4, self.btn7)
        elif(self.btn5.text()!="" and self.btn2.text() == self.btn5.text() and self.btn8.text() == self.btn5.text()):
            self.win(self.btn5, self.btn2, self.btn8)
        elif(self.btn3.text()!="" and self.btn3.text() == self.btn6.text() and self.btn6.text() == self.btn9.text()):
            self.win(self.btn3, self.btn6, self.btn9)
        # diogonal
        elif(self.btn1.text()!="" and self.btn1.text() == self.btn5.text() and self.btn5.text() == self.btn9.text()):
            self.win(self.btn1, self.btn5, self.btn9)
        elif(self.btn7.text()!="" and self.btn3.text() == self.btn5.text() and self.btn5.text() == self.btn7.text()):
            self.win(self.btn7, self.btn5, self.btn3)
        elif(self.navbat == 10):
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("DRAW")
            self.msg.buttonClicked.connect(self.reset)
            self.msg.exec_()

    def reset(self):
        self.disable(False)
        for i in self.btns_list:
            i.setStyleSheet(self.str_style)
            i.setText("")
        self.navbat = 1
        self.lbl.setText(">>>X<<<")

    def clicker(self, btn:QPushButton):
        if self.navbat % 2:
            btn.setText("X")
            self.lbl.setText(">>>O<<<")
        else:
            btn.setText("O")
            self.lbl.setText(">>>X<<<")

        self.navbat += 1
        btn.setEnabled(False)

        self.checkWin()

app = QApplication([])
win = Window()
win.show()
app.exec_()