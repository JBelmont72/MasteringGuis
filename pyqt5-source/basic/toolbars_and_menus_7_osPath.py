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

# basedir = os.path.dirname(__file__)
basedir = os.path.dirname('/Users/judsonbelmont/Downloads/MasteringGuis/Images/alarm-clock-blue.png')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basedir, "smiley-fat.png")),
            "&Your button",
            self,
        )
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(
            QIcon(os.path.join(basedir, "star.png")),
            "Your &button2",
            self,
        )
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()



# # Python program to explain os.path.dirname() method 
#   # example path  /Users/judsonbelmont/Downloads/MasteringGuis/Images/alarm-clock-blue.png
# # importing os.path module 
# import os.path

# # Path
# # path = '/home/User/Documents'
# path = '/Users/judsonbelmont/Downloads/MasteringGuis/Images/'
# # Get the directory name  
# # from the specified path
# dirname = os.path.dirname(path)

# # Print the directory name  
# print(dirname)


# # Path
# path = '/Users/judsonbelmont/Downloads/MasteringGuis/Images/animal.png'

# # Get the directory name  
# # from the specified path
# dirname = os.path.dirname(path)

# # Print the directory name  
# print(dirname)


# # Path
# path = 'animal.png'

# # Get the directory name  
# # from the specified path
# dirname = os.path.dirname(path)

# # Print the directory name  
# print(dirname)

# # In the above specified path 
# # does not contains any
# # directory so, 
# # It will print Nothing