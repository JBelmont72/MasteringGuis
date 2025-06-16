from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")

        # The `Qt` namespace has a lot of attributes to customize
        # widgets. See: https://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        label.setStyleSheet("font-size: 50px; color: red;")
        # The label will expand to take up all the space in the window
        # by default, so we don't need to set a layout or anything.
        # If you want to set a fixed size, you can use:
        # label.setFixedSize(300, 200)
        label.setToolTip("This is a label widget.")
        # list of signals for QLabel:
        # https://doc.qt.io/qt-5/qwidget.html#signals
        # list of slots for QLabel:
        # https://doc.qt.io/qt-5/qwidget.html#slots
        # list of events for QLabel:
        # https://doc.qt.io/qt-5/qwidget.html#events
        # list of properties for QLabel:
        # https://doc.qt.io/qt-5/qwidget.html#properties
        # list of methods for QLabel:
        # https://doc.qt.io/qt-5/qwidget.html#public-functions
        # list of styles for QLabel:
        # https://doc.qt.io/qt-5/stylesheet-syntax.html
        # list of styles for QLabel:
        # https://doc.qt.io/qt-5/stylesheet-examples.html
        label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        # The label will expand to take up all the space in the window
        label.setSizePolicy(
            # The horizontal policy is set to expand, which means the label will
            # take up all the available space in the window.
            # The vertical policy is set to fixed, which means the label will
            # not change its height.
            # QSizePolicy.Expanding, QSizePolicy.Fixed
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )   
        self.setCentralWidget(label)



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()


# Your application won't reach here until you exit and the event
# loop has stopped.
