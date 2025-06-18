'''   
'''
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import sys

class Color(qtw.QMainWindow):
    def __init__(self, color):
        super().__init__()
        self.setWindowTitle("Color Widget")
        layout = qtw.QVBoxLayout()        
        # Set the background color
        self.setStyleSheet(f"background-color: {color};")        
        # Set the size of the window
        self.resize(400, 300)
        central_widget = qtw.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    w = Color("lightblue")  # Change the color as needed
    # main_window.setWindowTitle("My App")

    # widget = qtw.QWidget()
    # layout = qtw.QVBoxLayout(widget)
    
    # label = qtw.QLabel("Hello, PyQt5!")
    # label.setAlignment(qtc.Qt.AlignCenter)
    
    # button = qtw.QPushButton("Click Me")
    
    # layout.addWidget(label)
    # layout.addWidget(button)

    # main_window.setCentralWidget(widget)
    w.show()
    sys.exit(app.exec_())

# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc
# import sys

# class Color(qtw.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle("Color Widget")
#         self.setAutoFillBackground(True)  # Enable auto-fill background
#         pallette = self.palette()
#         pallette.setColor(qtg.QPalette.Window, qtg.QColor("lightblue"))
#         self.setPalette(pallette)
#         self.resize(400, 300)
#         central_widget = qtw.QWidget()
#         layout = qtw.QVBoxLayout(central_widget)
#         self.setCentralWidget(central_widget)
#         self.show()


# if __name__ == "__main__":
#     app = qtw.QApplication(sys.argv)

#     w = Color()
#     w.setStyleSheet("background-color: lightblue;")  # Set the background color
#     w.resize(400, 300)  # Set the size of the window
#     w.show()

#     sys.exit(app.exec_())
    
    
    
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QPalette, QColor

# app = QApplication([])
# widget = QWidget()

# palette = widget.palette()
# palette.setColor(QPalette.Window, QColor("red"))
# widget.setPalette(palette)
# widget.setAutoFillBackground(True)

# widget.show()
# app.exec_()
