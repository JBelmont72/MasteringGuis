##/Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/toolbars_and_menus_2.py
'''page 103 'Creating Gui Applications...' Martin Fitzpatrick]
1,create a function that will accept the signal for QAction

2,define QAction
    When creating the 'instance' we can pass a label for the action or /and an icon
must also pass in any QObject to act as the parent for the action( here we use 'self') whic is a reference to the MainWIndow
THis parent element is passed in as the final parameter
3, set up status tip
4,conect the .triggered signal to the custom function



'''
# import sys    ## #1  toolbar clicked calls the function. not a class

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QAction,
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QToolBar,
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         label = QLabel("Hello!")
#         label.setAlignment(Qt.AlignCenter)

#         self.setCentralWidget(label)

#         toolbar = QToolBar("My main toolbar")
#         self.addToolBar(toolbar)

#         button_action = QAction("Your button", self)
#         button_action.setStatusTip("This is your button")
#         button_action.triggered.connect(self.onMyToolBarButtonClick)
#         toolbar.addAction(button_action)

#     def onMyToolBarButtonClick(self, is_checked):
#         print("click", is_checked)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()

# /Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/toolbars_and_menus_2.py
# import sys  ## #2 this is the class form of adding toobar with the toolbar having an action QAction

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QAction,
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QToolBar,QVBoxLayout,QMainWindow,QWidget
# )


# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QAction
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('my QAction')
#         self.setGeometry(10,10,300,400)
#         layout=QVBoxLayout() # create layout
#         toolbar =QToolBar('my Toolbar')
#         label=QLabel('my label',self)
#         label.setAlignment(Qt.AlignCenter)
#         # label.setAlignment(Qt.AlignRight|Qt.AlignBottom)
#         # layout.addWidget(toolbar)
#         layout.addWidget(label)
#         layout.addStretch()
        
#         button_action =QAction('My Button',self)
#         button_action.setStatusTip('this is my own button')
#         button_action.triggered.connect(self.onMyToolBar)
#         toolbar.addAction(button_action)
        
#         # from PyQt5.QtGui import QIcon
#         # from PyQt5.QtWidgets import QAction

#         # Inside your __init__ method after creating the toolbar:
#         action = QAction(QIcon(), "Greet", self)
#         action.setStatusTip("Print a greeting")
#         action.triggered.connect(lambda: self.label.setText(' '),print("Hello from the toolbar!"))
#         toolbar.addAction(action)

        
        
        
        
#         self.addToolBar(toolbar)   
#         central_widget=QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#     def onMyToolBar(self,s):
#         print('click',s)
#         self.label.setText('') 
#         self.label.setText('hello again')   
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window=MainWindow()
#     window.show()
#     sys.exit(app.exec_())
    
    
# /Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/toolbars_and_menus_2.py



# import sys    ## #2  basic open a toolbar ,no function
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication, QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My QAction Test")
#         self.setGeometry(100, 100, 300, 200)

#         # Label
#         label = QLabel("My Label", self)
#         label.setAlignment(Qt.AlignCenter)

#         # Layout and central widget
#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         layout.addStretch()

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Toolbar
#         toolbar = QToolBar("My Toolbar")
#         self.addToolBar(toolbar)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

## #4 adds a button to toolbar
# import sys        ## #4 adds a button to toolbar, No QAction
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QToolBar,
#     QVBoxLayout,
#     QWidget,
#     QPushButton
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Toolbar Without QAction')
#         self.setGeometry(10, 10, 300, 200)

#         # Label in central widget
#         self.label = QLabel('Press the toolbar button', self)
#         self.label.setAlignment(Qt.AlignCenter)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create toolbar
#         toolbar = QToolBar("Main Toolbar")
#         self.addToolBar(toolbar)

#         # Add QPushButton to toolbar
#         button = QPushButton("Click Me")
#         button.clicked.connect(self.say_hello)
#         toolbar.addWidget(button)

#     def say_hello(self):
#         self.label.setText("Hello from the toolbar!")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

##  number 5 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QToolBar,
    QAction,
    QVBoxLayout,
    QWidget
)
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Toolbar Action with Lambda')
        self.setGeometry(100, 100, 400, 300)

        # Create central widget and layout
        layout = QVBoxLayout()
        self.label = QLabel('This label will be cleared', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create toolbar and add it
        toolbar = QToolBar('My Toolbar')
        self.addToolBar(toolbar)

        action = QAction(QIcon(), "Greet", self) # added
        action.setStatusTip("Print a greeting")
        action.triggered.connect(lambda checked: self.enter_label(checked))
        action.triggered.connect(self.enter_label)
        toolbar.addAction(action)

  
        
        # Create action and connect using lambda
        clear_action = QAction('Clear Label', self)
        clear_action.triggered.connect(lambda: self.clear_label())
        toolbar.addAction(clear_action)

    def clear_label(self):
        self.label.setText("")
        print("Label cleared from toolbar action.")



    def enter_label(self,checked):    ## added
        print('click',checked)
        self.label.setText('') 
        self.label.setText('hello again') 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QToolBar,
#     QAction,
#     QVBoxLayout,
#     QWidget
# )
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Toolbar Action with Lambda')
#         self.setGeometry(100, 100, 400, 300)

#         # Create central widget and layout
#         layout = QVBoxLayout()
#         self.label = QLabel('This label will be cleared', self)
#         self.label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(self.label)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create toolbar and add it
#         toolbar = QToolBar('My Toolbar')
#         self.addToolBar(toolbar)

#         # Enter label action
#         action = QAction(QIcon(), "Greet", self)
#         action.setStatusTip("Print a greeting")
#         action.triggered.connect(self.enter_label)  # ✅ No lambda or extra args needed
#         toolbar.addAction(action)

#         # Clear label action
#         clear_action = QAction('Clear Label', self)
#         clear_action.triggered.connect(self.clear_label)  # ✅ Properly connected
#         toolbar.addAction(clear_action)

#     def clear_label(self):
#         self.label.setText("")
#         print("Label cleared from toolbar action.")

#     def enter_label(self):
#         print('Toolbar action: enter_label triggered')
#         self.label.setText('Hello again!')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

