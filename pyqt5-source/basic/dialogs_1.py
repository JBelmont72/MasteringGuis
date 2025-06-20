# import sys

# from PyQt5.QtWidgets import (
#     QApplication,
#     QDialog,
#     QMainWindow,
#     QPushButton,
# )


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)

#     def button_clicked(self, is_checked):
#         print("click", is_checked)

#         dlg = QDialog(self)
#         dlg.setWindowTitle("?")
#         dlg.exec_()


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
class MainWindow(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('my first dialog')
        self.setGeometry(10,10,300,400)
        ## set Action
        self.toggle_action=qtw.QAction('Toggle Message to Us',self)
        self.toggle_action.setChecked(False)
        self.toggle_action.setCheckable(True)
        self.toggle_action.triggered.connect(self.toggled)
        
        ## toolbar
        self.toolbar=qtw.QToolBar('my own toolbar')
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.toggle_action)
        
        
        
        
        layout = qtw.QVBoxLayout()
        
        self.label=qtw.QLabel('my Label',self)
        self.label.setAlignment(qtc.Qt.AlignCenter)
        layout.addWidget(self.label)
        central_widget=qtw.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def toggled(self,checked):
        print(checked)
        if checked == True:
            self.label.setText('you have checked YES') 
        else:
            self.label.setText('you have checked NO')
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    
# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QAction, QLabel, QVBoxLayout,
#     QWidget, QPushButton, QCheckBox, QToolBar
# )
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("QAction Sync Example")
#         self.setGeometry(100, 100, 400, 300)

#         # === CENTRAL WIDGET SETUP ===
#         self.label = QLabel("Toggle something!", self)
#         self.label.setAlignment(Qt.AlignCenter)

#         self.toggle_action = QAction("Toggle Message", self)
#         self.toggle_action.setCheckable(True)
#         self.toggle_action.setChecked(False)
#         self.toggle_action.triggered.connect(self.toggle_label)

#         # Widgets that use the same QAction
#         self.toolbar_checkbox = QCheckBox("Toggle via CheckBox (Shared QAction)")
#         self.toolbar_checkbox.stateChanged.connect(
#             lambda state: self.toggle_action.setChecked(state == Qt.Checked)
#         )

#         self.central_button = QPushButton("Toggle via Button (Shared QAction)")
#         self.central_button.clicked.connect(self.toggle_action.trigger)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.toolbar_checkbox)
#         layout.addWidget(self.central_button)

#         central = QWidget()
#         central.setLayout(layout)
#         self.setCentralWidget(central)

#         # === TOOLBAR SETUP ===
#         toolbar = QToolBar("Main Toolbar")
#         self.addToolBar(toolbar)

#         toolbar.addAction(self.toggle_action)

#     def toggle_label(self, checked):
#         if checked:
#             self.label.setText("Toggled ON!")
#         else:
#             self.label.setText("Toggled OFF!")
#         self.toolbar_checkbox.setChecked(checked)  # Keep checkbox synced

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec_())
