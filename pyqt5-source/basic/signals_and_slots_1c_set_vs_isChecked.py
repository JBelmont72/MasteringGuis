''' one option when the widget being used does not provide a signal.  use .setChecked(the self.default value as below)
page 29-30 of 'create guis...'

'''

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True  # <1>

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)  # <2> the default value in <1> is set as the initial value of the widget

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_toggled(self, is_checked):
        self.button_is_checked = is_checked  # <3> When the button is clicked, the value of self.button_is_checked is reset.

        print(self.button_is_checked)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
