'''I converted the stacked layout of page 94 of matin Fitz[atrick 'clinical gui applications eiyh python and PyQt5'''
# /Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/layout_8.py
# import sys

# from PyQt5.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QMainWindow,
#     QPushButton,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
# )

# from layout_colorwidget import Color


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         pagelayout = QVBoxLayout()
#         button_layout = QHBoxLayout()
#         self.stacklayout = QStackedLayout()

#         pagelayout.addLayout(button_layout)
#         pagelayout.addLayout(self.stacklayout)

#         btn = QPushButton("red")
#         btn.pressed.connect(self.activate_tab_1)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("red"))

#         btn = QPushButton("green")
#         btn.pressed.connect(self.activate_tab_2)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("green"))

#         btn = QPushButton("yellow")
#         btn.pressed.connect(self.activate_tab_3)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("yellow"))
#         colors=['yellow','red','magenta','blue']
#         for color in colors:
#             self.stacklayout.addWidget(Color(color))
#         for color in colors:
#             btn=QPushButton(color)
#         widget = QWidget()
#         widget.setLayout(pagelayout)
#         self.setCentralWidget(widget)

#     def activate_tab_1(self):
#         self.stacklayout.setCurrentIndex(0)

#     def activate_tab_2(self):
#         self.stacklayout.setCurrentIndex(1)

#     def activate_tab_3(self):
#         self.stacklayout.setCurrentIndex(2)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        colors=['yellow','red','magenta','blue']
        # Activate =['self.activate_tab_1','self.activate_tab2','self.activate_tab_3','self.activate_tab4']
        Activate =[self.activate_tab_1,self.activate_tab_2,self.activate_tab_3,self.activate_tab_4]
        for color, active in zip(colors,Activate):
            self.stacklayout.addWidget(Color(color))
            btn=QPushButton(color)
            btn.pressed.connect(active)
            button_layout.addWidget(btn)
        
        # for color in colors:
        #     self.stacklayout.addWidget(Color(color))
        #     btn=QPushButton(color)
        #     button_layout.addWidget(btn)
        # btn = QPushButton("red")
        # btn.pressed.connect(self.activate_tab_1)
        # button_layout.addWidget(btn)
        # self.stacklayout.addWidget(Color("red"))

        # btn = QPushButton("green")
        # btn.pressed.connect(self.activate_tab_2)
        # button_layout.addWidget(btn)
        # self.stacklayout.addWidget(Color("green"))

        # btn = QPushButton("yellow")
        # btn.pressed.connect(self.activate_tab_3)
        # button_layout.addWidget(btn)
        # self.stacklayout.addWidget(Color("yellow"))
        

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)
    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
