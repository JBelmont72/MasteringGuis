## /Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/toolbars_and_menus_1.py
## first from the tutorial. second is my version

# import sys

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
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
#         # Optional: to prevent this toolbar being removed.
#         # toolbar.toggleViewAction().setEnabled(False)
#         self.addToolBar(toolbar)

#     def onMyToolBarButtonClick(self, is_checked):
#         print("click", is_checked)



# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()


## /Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/toolbars_and_menus_1.py
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QToolBar,QVBoxLayout,QWidget,QTabWidget)
from PyQt5 import QtCore as qtc
class MainWindow(QMainWindow):
    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)
        self.setWindowTitle('my Qaction')
        layout=QVBoxLayout()
        # self.setLayout(layout)
        toolbar =QToolBar(self)
        tabs=QTabWidget(self)
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        # tabs.setTabText()
        layout.addWidget(tabs)
        label=QLabel('my label',self)
        label.setAlignment(qtc.Qt.AlignCenter)
        
        
        
        layout.addWidget(toolbar)
        layout.addWidget(label)
        
        central_widget =QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        


if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())