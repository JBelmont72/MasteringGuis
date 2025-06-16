### understanding Custom Widgets and using QTextEdit
* Mastering Gui programming
* working with custom widgets

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class CustomTextEdit(qtw.QTextEdit):
    """A custom QTextEdit that clears its contents when focused."""
    def focusInEvent(self, event):
        self.clear()  # Clear text when focus is gained
        super().focusInEvent(event)  # Call the base method to retain default behavior

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chapter 3 - My Project')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(qtg.QIcon('/Users/judsonbelmont/Downloads/MasteringGuis/Chapter06/logo.png'))

        # Main layout
        self.layout = qtw.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Header label
        self.label = qtw.QLabel('Welcome to Chapter 3 of My Project!', self)
        self.label.setAlignment(qtc.Qt.AlignCenter)
        self.label.setFont(qtg.QFont('Arial', 16))
        self.layout.addWidget(self.label)

        # Grid layout section
        self.grid_layout = qtw.QGridLayout()
        self.grid_layout.setSpacing(10)
        self.layout.addLayout(self.grid_layout)

        # Button
        self.button = qtw.QPushButton('Click Me', self)
        self.grid_layout.addWidget(self.button, 0, 0)
        self.button.clicked.connect(self.on_button_click)

        # Custom text edit widget
        self.text_edit = CustomTextEdit(self)
        self.text_edit.setPlaceholderText('Type something here...')
        self.text_edit.setFont(qtg.QFont('Arial', 12))
        self.text_edit.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        self.text_edit.setFixedHeight(100)
        self.text_edit.setFixedWidth(300)
        self.text_edit.setLineWrapMode(qtw.QTextEdit.WidgetWidth)
        self.text_edit.setTextInteractionFlags(qtc.Qt.TextEditorInteraction)
        self.text_edit.setAcceptRichText(True)
        self.text_edit.setUndoRedoEnabled(True)
        self.text_edit.setText('This is a text edit widget. You can type here.')

        self.grid_layout.addWidget(self.text_edit, 0, 1, 1, 2)

        self.show()

    def on_button_click(self):
        """Read text from the editor and show it in a message box."""
        text = self.text_edit.toPlainText().strip()
        if text:
            qtw.QMessageBox.information(self, 'Button Clicked', f'You typed: {text}')
        else:
            qtw.QMessageBox.warning(self, 'Button Clicked', 'Please type something before clicking the button.')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    mw = MainWindow()
    sys.exit(app.exec())

### tutorial
✅ 2. Why Use a Custom Widget?

➤ Qt's Signal/Slot System Is Powerful — But Not Always Enough
Qt gives us signals like .textChanged, .editingFinished, etc. However:

You don’t get a signal for focus events by default.
You may want to change the widget’s core behavior (like clearing on focus).
Built-in signals don't let you intercept or override system events like mouse clicks, key presses, or focus.
That’s where CustomTextEdit comes in.
✅ Common Use Cases for Custom Widgets:
Scenario	Why Built-in Signals Fail	Solution
Clear text on focus	No .focusIn signal	Override focusInEvent()
Intercept Return key	.returnPressed is only for QLineEdit	Override keyPressEvent()
Validate input while typing	.textChanged doesn't block bad input	Override inputMethodEvent() or use validators
Add animation or effects	Built-in methods are static	Override paintEvent() or resizeEvent()
✅ 3. Anatomy of a Custom Widget

Here's the anatomy of what we did:

class CustomTextEdit(qtw.QTextEdit):
    def focusInEvent(self, event):
        self.clear()  # Custom behavior: clear on focus
        super().focusInEvent(event)  # Retain default behavior
🔍 Key Points:
focusInEvent(self, event) is a special Qt event handler.
By overriding it, we inject our behavior.
We call the base class afterward to avoid breaking default behavior.
🧠 Final Takeaway

Custom widgets are useful when:

You want different behavior than what’s offered by signals/slots.
You want to respond to low-level events (keyboard, mouse, focus).
You need a component with specific visual or interactive behavior that Qt doesn’t offer out of the box.
Would you like a second example showing:

➤ A custom QPushButton that changes its color when clicked or hovered?
Or maybe something like:

➤ A QTextEdit that only allows numeric input?
Let me know what direction you'd like to explore next!


Yes — if you want a QPushButton to respond directly to keyboard input in a custom way (like changing colors when specific keys are pressed) — then a custom widget is typically the cleanest and most reliable solution.

Let me explain with clarity:

✅ When You Need a Custom QPushButton

You need a custom subclass of QPushButton if:

You want the button to change color based on keyboard keys (e.g., pressing "R" makes it red).
You want to intercept key presses only when the button has focus or always, regardless of focus.
The behavior is not tied to button clicks, but instead to key events.
🔥 Example: Custom Button That Changes Color Based on Keyboard
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
🤔 Why Not Just Use a Signal?

Because QPushButton doesn't emit signals on arbitrary keypresses — only on clicked() or certain shortcuts. Overriding keyPressEvent() gives you:

Full control over keyboard interaction
Custom logic per key
The ability to build visual feedback like color changes
🧠 Summary

You want to…	Need a custom widget?	Why?
Change color on click	❌ No	Use .clicked.connect(...)
Change color on keyboard press	✅ Yes	Requires keyPressEvent() override
Change color on hover	✅ Yes or use enterEvent()	Hovering needs event handlers or CSS
React to key even when widget doesn't have focus	✅ Yes + event filter	Needs extra event management
Would you like a version where keyboard events are captured globally, even if the button doesn’t have focus? That’s a great next step if you’re exploring advanced interaction.
