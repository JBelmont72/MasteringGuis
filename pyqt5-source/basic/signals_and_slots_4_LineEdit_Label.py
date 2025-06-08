# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QLabel,
#     QLineEdit,
#     QVBoxLayout,
#     QWidget,
# )

# import sys


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         self.label = QLabel()

#         self.input = QLineEdit()
#         self.input.textChanged.connect(self.label.setText)  # <1>

#         layout = QVBoxLayout()  # <2>
#         layout.addWidget(self.input)
#         layout.addWidget(self.label)

#         container = QWidget()
#         container.setLayout(layout)

#         # Set the central widget of the Window.
#         self.setCentralWidget(container)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()
######~~~~ my version

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import sys

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('my Label/LineEdit')
        self.setGeometry(50,50,400,600)
        ## create layout
        layout = qtw.QVBoxLayout()
        
        ## create lineEdit and Qlabel
        self.myLabel = qtw.QLabel('my new label')
        self.myLineEdit = qtw.QLineEdit()
        ## define the input for the lineEdit
        self.myLineEdit.textChanged.connect(self.myLabel.setText)
        self.myLineEdit.textChanged.connect(self.change)
        
        # add to layout
        layout.addWidget(self.myLabel)
        layout.addWidget(self.myLineEdit)
        
        ## create  central_window
        central_window = qtw.QWidget()
        central_window.setLayout(layout)
        self.setCentralWidget(central_window)
        layout.addStretch()
        
        
    def change(self):
        print('change now.')   
        
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
