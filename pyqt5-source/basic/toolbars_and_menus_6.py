'''
/Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/toolbars_and_menus_6.py
i made rooky mistke of not making the label global with self.label
'''

import os
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
## /Users/judsonbelmont/Downloads/MasteringGuis/Images/rocket-fly.png
basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel("Hello!",self)
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            # QIcon(os.path.join(basedir, "bug.png")),
            # QIcon(os.path.join(basedir, "/Users/judsonbelmont/Downloads/MasteringGuis/Images/rocket-fly.png")),
            QIcon(os.path.join(basedir, "/Users/judsonbelmont/Downloads//MasteringGuis/Images/rocket-fly.png")),
            "Your button",
            self,
        )
        
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "Your button2",
            self,
        )
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        self.checkBox1=QCheckBox('my CheckBox')
        
        self.checkBox1.setStatusTip('This is my own checkbox1')
        # self.checkBox1.clicked.connect(self.winter)
        self.checkBox1.clicked.connect(lambda checkstate  :self.winter(checkstate))
        self.checkBox1.stateChanged.connect(self.method)
        
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        toolbar.addWidget(self.checkBox1)
        
        
        
        

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)

    def winter(self,checkstate):
        print('CheckState  ',checkstate)
        if checkstate== True:
            self.label.setText('')
            self.label.setText('my CheckBox checked')
        else: 
            self.label.setText('i am back')

    def method(self):
        print(self.checkBox1.isChecked())
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
