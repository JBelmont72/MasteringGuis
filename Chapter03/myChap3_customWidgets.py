'''
This is a placeholder for Chapter 3 of my project.
It includes a custom widget that changes color based on keyboard input.
This code is a simple PyQt5 application that demonstrates how to create a custom button widget
that changes its background color when the user presses the 'R', 'G', or 'B' keys.
This is a simple PyQt5 application that demonstrates how to create a custom button widget
that changes its background color when the user presses the 'R', 'G', or 'B' keys.
/Users/judsonbelmont/Downloads/MasteringGuis/Chapter03/textEdit_CustomWidget_button.md

Chapter03/myChap3_customWidgets.py
chat with Custom Widgets  https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
'''     
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QWidget):

#     def __init__(self):
  
#         super().__init__()
#         # Main UI code goes here
#         self.setWindowTitle('Chapter 3 - My Project')
#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowIcon(qtg.QIcon('/Users/judsonbelmont/Downloads/MasteringGuis/Chapter06/logo.png'))
#         self.layout = qtw.QVBoxLayout(self)
#         self.setLayout(self.layout)
#         self.label = qtw.QLabel('Welcome to Chapter 3 of My Project!', self)
#         self.label.setAlignment(qtc.Qt.AlignCenter)
#         self.label.setFont(qtg.QFont('Arial', 16))
#         self.layout.addWidget(self.label)
#         ##page 38 QGridlayout
#         self.grid_layout = qtw.QGridLayout()
#         self.grid_layout.setSpacing(10)
        
#         self.layout.addLayout(self.grid_layout)

#         self.button = qtw.QPushButton('Click Me', self)
#         self.grid_layout.addWidget(self.button, 0, 0)
#         self.button.clicked.connect(self.on_button_click)
#         self.text_edit = qtw.QTextEdit(self)
#         self.text_edit.setPlaceholderText('Type something here...')
#         self.grid_layout.addWidget(self.text_edit, 0, 1, 1, 2)
#         self.text_edit.setFont(qtg.QFont('Arial', 12))
#         self.text_edit.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
#         self.text_edit.setFixedHeight(100)
#         self.text_edit.setFixedWidth(300)
#         self.text_edit.setAlignment(qtc.Qt.AlignLeft)
#         self.text_edit.setReadOnly(False)
#         self.text_edit.setTabChangesFocus(True)
#         self.text_edit.setLineWrapMode(qtw.QTextEdit.WidgetWidth)
#         self.text_edit.setTextInteractionFlags(qtc.Qt.TextEditorInteraction)
#         self.text_edit.setAcceptRichText(True)
#         self.text_edit.setUndoRedoEnabled(True)
#         # self.text_edit.setWordWrapMode(qtc.QTextOption.WrapAnywhere)
#         self.text_edit.setText('This is a text edit widget. You can type here.')
#         self.clear_placeholder_on_focus()
#         self.setup_text_edit_behavior()
#         self.show()       
#     def on_button_click(self):
#         # This method will be called when the button is clicked
#         text = self.text_edit.toPlainText().strip()  # Strip leading/trailing whitespace
#         if text:  # Check if text is not empty after stripping
#             qtw.QMessageBox.information(self, 'Button Clicked', f'You typed: {text}')
#         else:
#             qtw.QMessageBox.warning(self, 'Button Clicked', 'Please type something before clicking the button.')

#     def clear_placeholder_on_focus(self):
#         # Clear placeholder text when the widget gains focus
#         self.text_edit.clear()

#     def setup_text_edit_behavior(self):
#         # Connect focus event to clear placeholder
#         class CustomTextEdit(qtw.QTextEdit):
#             def focusInEvent(self, event):
#                 self.clear()
#                 super().focusInEvent(event)

#         self.text_edit = CustomTextEdit(self)

#     # Call this method in the constructor after initializing text_edit
#     # self.setup_text_edit_behavior()
#         # Add more UI elements and functionality as needed
#         # This is the end of the main UI code
#         # End main UI code
        


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     app.setStyle('Fusion')  # Set the application style to Fusion
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())

# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class CustomTextEdit(qtw.QTextEdit):
#     """A custom QTextEdit that clears its contents when focused."""
#     def focusInEvent(self, event):
#         self.clear()  # Clear text when focus is gained
#         super().focusInEvent(event)  # Call the base method to retain default behavior

# class MainWindow(qtw.QWidget):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Chapter 3 - My Project')
#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowIcon(qtg.QIcon('/Users/judsonbelmont/Downloads/MasteringGuis/Chapter06/logo.png'))

#         # Main layout
#         self.layout = qtw.QVBoxLayout(self)
#         self.setLayout(self.layout)

#         # Header label
#         self.label = qtw.QLabel('Welcome to Chapter 3 of My Project!', self)
#         self.label.setAlignment(qtc.Qt.AlignCenter)
#         self.label.setFont(qtg.QFont('Arial', 16))
#         self.layout.addWidget(self.label)

#         # Grid layout section
#         self.grid_layout = qtw.QGridLayout()
#         self.grid_layout.setSpacing(10)
#         self.layout.addLayout(self.grid_layout)

#         # Button
#         self.button = qtw.QPushButton('Click Me', self)
#         self.grid_layout.addWidget(self.button, 0, 0)
#         self.button.clicked.connect(self.on_button_click)

#         # Custom text edit widget
#         self.text_edit = CustomTextEdit(self)
#         self.text_edit.setPlaceholderText('Type something here...')
#         self.text_edit.setFont(qtg.QFont('Arial', 12))
#         self.text_edit.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
#         self.text_edit.setFixedHeight(100)
#         self.text_edit.setFixedWidth(300)
#         self.text_edit.setLineWrapMode(qtw.QTextEdit.WidgetWidth)
#         self.text_edit.setTextInteractionFlags(qtc.Qt.TextEditorInteraction)
#         self.text_edit.setAcceptRichText(True)
#         self.text_edit.setUndoRedoEnabled(True)
#         self.text_edit.setText('This is a text edit widget. You can type here.')

#         self.grid_layout.addWidget(self.text_edit, 0, 1, 1, 2)

#         self.show()

#     def on_button_click(self):
#         """Read text from the editor and show it in a message box."""
#         text = self.text_edit.toPlainText().strip()
#         if text:
#             qtw.QMessageBox.information(self, 'Button Clicked', f'You typed: {text}')
#         else:
#             qtw.QMessageBox.warning(self, 'Button Clicked', 'Please type something before clicking the button.')

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     app.setStyle('Fusion')
#     mw = MainWindow()
#     sys.exit(app.exec())




import sys
from PyQt5 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

class ColorChangingButton(qtw.QPushButton):
    def __init__(self, label='Press R, G, or B', parent=None):
        super().__init__(label, parent)
        self.setFocusPolicy(qtc.Qt.StrongFocus)  # Allow it to receive key events

    def keyPressEvent(self, event):
        key = event.key()
        if key == qtc.Qt.Key_R:
            self.setStyleSheet("background-color: red; color: white;")
        elif key == qtc.Qt.Key_G:
            self.setStyleSheet("background-color: green; color: white;")
        elif key == qtc.Qt.Key_B:
            self.setStyleSheet("background-color: blue; color: white;")
        else:
            super().keyPressEvent(event)  # Preserve default behavior

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Button Keyboard Example")
        layout = qtw.QVBoxLayout()

        self.button = ColorChangingButton()
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.resize(300, 150)
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())
