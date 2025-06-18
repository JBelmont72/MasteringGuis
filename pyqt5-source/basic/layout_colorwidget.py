from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget,QApplication
import sys

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Color('red')
    w.show()
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
