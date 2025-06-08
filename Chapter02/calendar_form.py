'''
this is aclaendoar using the widgets and layouts covered in Chapter 2 of Mastering Gui Widgets with Python by Alan D Moore

/Users/judsonbelmont/Downloads/MasteringGuis/Chapter02/calendar_form.py
for PyQt5 docs  https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtextedit.html#qtextedit'''


# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self):
#         """MainWindow constructor."""
#         super().__init__()

#         # Configure the window
#         self.setWindowTitle("My Calendar App")
#         self.resize(800, 600)

#         # Create our widgets
#         self.calendar = qtw.QCalendarWidget()
#         self.event_list = qtw.QListWidget()
#         self.event_title = qtw.QLineEdit()
#         self.event_category = qtw.QComboBox()
#         self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
#         self.allday_check = qtw.QCheckBox('All Day')
#         self.event_detail = qtw.QTextEdit(self)
#         ## working with the QTextEdit
        
#         self.event_detail=qtw.QTextEdit(self,acceptRichText=False,lineWrapMode=qtw.QTextEdit.FixedColumnWidth,placeholderText="Enter your data here",lineWrapColumnOrWidth=25,readOnly=False,cursorWidth=20)
#         self.event_detail.setOverwriteMode(True) ## if true overwrites. if false, just adds or pushes the old entry to the right
#         self.event_detail.setFontPointSize(30)
#         # Example of usage:
#         cursor_rect = self.event_detail.cursorRect() ## this gives the cursor size
#         print(f"Cursor Rect: x={cursor_rect.x()}, y={cursor_rect.y()}, width={cursor_rect.width()}, height={cursor_rect.height()}")

#         ## this creates a bullet list if i start typing with *
#         self.event_detail.setAutoFormatting(qtw.QTextEdit.AutoBulletList) # Corrected to use valid AutoFormatting flags

#         self.add_button = qtw.QPushButton('Add/Update')
#         self.del_button = qtw.QPushButton('Delete')

#         # Configure some widgets

#         # Add event categories this is QComboBox
#         self.event_category.addItems(
#             ['Select category…', 'New…', 'Work',
#              'Meeting', 'Doctor', 'Family']
#             )
#         # disable the first category item of the QComboBox
#         self.event_category.model().item(0).setEnabled(False)

#         # Arrange the widgets
#         main_layout = qtw.QHBoxLayout()
#         self.setLayout(main_layout)
#         main_layout.addWidget(self.calendar)    ## here added a widget to occupay the left side of 'main_layout'
#         # Calendar expands to fill the window
#         self.calendar.setSizePolicy(
#             qtw.QSizePolicy.Expanding,
#             qtw.QSizePolicy.Expanding
#         )
#         right_layout = qtw.QVBoxLayout()
#         main_layout.addLayout(right_layout)
#         right_layout.addWidget(qtw.QLabel('Events on Date'))## in the right layout have 1_QLabel, 2_'event_list',3_ event_form_layout'
#         right_layout.addWidget(self.event_list)
#         # Event list expands to fill the right area
#         self.event_list.setSizePolicy(
#             qtw.QSizePolicy.Expanding,
#             qtw.QSizePolicy.Expanding
#         )

#         # Create a sub-layout for the event view/add form
#         event_form = qtw.QGroupBox('Event')
#         right_layout.addWidget(event_form)
#         event_form_layout = qtw.QGridLayout()   ## this is the right sided Layout
#         event_form.setLayout(event_form_layout)

#         event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
#         event_form_layout.addWidget(self.event_category, 2, 1)
#         event_form_layout.addWidget(self.event_time, 2, 2,)
#         event_form_layout.addWidget(self.allday_check, 2, 3)
#         event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
#         event_form_layout.addWidget(self.add_button, 4, 2)
#         event_form_layout.addWidget(self.del_button, 4, 3)

#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())


'''
The cursorRect() method in PyQt5, specifically within the QTextEdit class, is used to obtain the bounding rectangle of the text cursor. This method returns a QRect object that represents the cursor's position and size within the QTextEdit widget's viewport coordinates.
Key aspects:
Purpose:
It provides the geometrical information of the cursor, which is essential for tasks like displaying custom tooltips, context menus, or other UI elements relative to the cursor's location.
Return Value:
The method returns a QRect, which contains the x and y coordinates of the top-left corner of the cursor rectangle, as well as the width and height of the cursor.
Coordinate System:
The coordinates returned are in the QTextEdit's viewport coordinate system, not the global screen coordinates.
Usage:
It's typically called when you need to position elements in relation to the cursor, such as when implementing autocompletion or other interactive features.
No Arguments:
When called without arguments, it returns the rectangle of the current cursor.




/Users/judsonbelmont/Downloads/MasteringGuis/Chapter02/calendar_form.py


setTextBackgroundColor(Union[QColor, GlobalColor, QGradient])
'''

from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QColor, QTextCharFormat, QTextCursor

app = QApplication([])
text_edit = QTextEdit()
text_edit.setStyleSheet("background-color: lightgreen")
# Create a QTextCharFormat object
char_format = QTextCharFormat()

# Set the background color to yellow
char_format.setBackground(QColor("magenta"))

# Select some text
cursor = text_edit.textCursor()
cursor.select(QTextCursor.WordUnderCursor) # Example: Select the word under the cursor

# Apply the format to the selected text
cursor.mergeCharFormat(char_format)

text_edit.show()
app.exec_()
'''
In PyQt5, you can use the setTextBackgroundColor() function to set the background color of text within a text-based widget like QTextEdit or QPlainTextEdit. This function belongs to the QTextCharFormat class, which is used to apply formatting information to characters within a QTextDocument. 
How to use setTextBackgroundColor():
Create a QTextCharFormat object: This object will hold the formatting you want to apply.
Set the background color: Use setBackground() on the QTextCharFormat object, passing a QColor or QBrush. You can specify the color using RGB values, hex codes (e.g., "#RRGGBB"), or predefined color names.
Apply the format to the desired text:
For selected text: Use a QTextCursor to define the selected range and then use mergeCharFormat() to apply the QTextCharFormat to that range.
For all text in the widget: You might need to iterate through the text document or use a QSyntaxHighlighter to apply the formatting to specific sections of text. 
Note: While you can directly set the background color of a QLabel using stylesheets (e.g., label.setStyleSheet("background-color: lightgreen")), this is generally for setting the overall background of the widget, not for individual characters or selected text. 
For more complex scenarios, like applying syntax highlighting, consider using QSyntaxHighlighter in conjunction with QTextCharFormat. 
'''