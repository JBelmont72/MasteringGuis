
First has demonstration of the signals that various widgets utilize
#  /Users/judsonbelmont/Downloads/MasteringGuis/WidgetSignalConnections.py
Second program is great illustration of using  QAction object

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QCheckBox, QRadioButton, QLineEdit, QSlider,
    QComboBox, QLabel, QTabWidget, QMainWindow
)
from PyQt5.QtCore import Qt

class DemoSignals(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal Showcase")
        layout = QVBoxLayout()

        # QPushButton
        self.button = QPushButton("Push Me")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        # QCheckBox
        self.checkbox = QCheckBox("Check Me")
        self.checkbox.stateChanged.connect(self.on_checkbox_state_changed)
        layout.addWidget(self.checkbox)

        # QRadioButton
        self.radio = QRadioButton("Select Me")
        self.radio.toggled.connect(self.on_radio_toggled)
        layout.addWidget(self.radio)

        # QLineEdit
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Type and press Enter")
        self.lineedit.returnPressed.connect(self.on_return_pressed)
        layout.addWidget(self.lineedit)

        # QSlider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.valueChanged.connect(self.on_slider_changed)
        layout.addWidget(self.slider)

        # QComboBox
        self.combo = QComboBox()
        self.combo.addItems(["Apple", "Banana", "Cherry"])
        self.combo.currentTextChanged.connect(self.on_combo_changed)
        layout.addWidget(self.combo)

        # QTabWidget
        self.tabs = QTabWidget()
        self.tabs.addTab(QLabel("Tab 1 Content"), "Tab 1")
        self.tabs.addTab(QLabel("Tab 2 Content"), "Tab 2")
        self.tabs.currentChanged.connect(self.on_tab_changed)
        layout.addWidget(self.tabs)

        # Status Label
        self.status = QLabel("Output will appear here...")
        layout.addWidget(self.status)

        self.setLayout(layout)

    def on_button_clicked(self):
        self.status.setText("Button clicked!")

    def on_checkbox_state_changed(self, state):
        self.status.setText(f"Checkbox: {'Checked' if state else 'Unchecked'}")

    def on_radio_toggled(self, checked):
        self.status.setText(f"Radio toggled: {'On' if checked else 'Off'}")

    def on_return_pressed(self):
        self.status.setText(f"LineEdit: {self.lineedit.text()}")

    def on_slider_changed(self, value):
        self.status.setText(f"Slider value: {value}")

    def on_combo_changed(self, text):
        self.status.setText(f"ComboBox selected: {text}")

    def on_tab_changed(self, index):
        self.status.setText(f"Tab changed to: {index + 1}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DemoSignals()
    demo.show()
    sys.exit(app.exec_())

'''

QAction Sync Example 
https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
No, PyQt5 QAction is not only for toolbars. 
Purpose of QAction:
QAction represents an abstract user command that can be invoked via various user interface components, such as menus, toolbar buttons, and keyboard shortcuts.
It serves to ensure that the same command is performed consistently regardless of how the user triggers it. 
Where QActions are used:
Menus: QAction objects can be added to menus to create menu items.
Toolbars: They can be added to toolbars to represent actions that are easily accessible through toolbar buttons.
Keyboard Shortcuts: You can associate keyboard shortcuts with QAction objects, allowing users to trigger commands using keyboard combinations. 
Benefits of using QAction:
Centralized Command Handling: QAction allows you to define a single action and then add it to multiple UI elements, ensuring consistency.
Automatic UI Synchronization: When a QAction is triggered (e.g., from a toolbar button), the corresponding UI element (e.g., a menu item) will automatically update its state (e.g., checked or unchecked). 
In summary: While QAction is commonly used in toolbars, it provides a broader abstraction for user commands that can be utilized in various UI contexts, including menus and keyboard shortcuts. 
'''

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QLabel, QVBoxLayout,
    QWidget, QPushButton, QCheckBox, QToolBar
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QAction Sync Example")
        self.setGeometry(100, 100, 400, 300)

        # === CENTRAL WIDGET SETUP ===
        self.label = QLabel("Toggle something!", self)
        self.label.setAlignment(Qt.AlignCenter)
        ## create the QAction Object
        self.toggle_action = QAction("Toggle Message", self)
        self.toggle_action.setCheckable(True)
        self.toggle_action.setChecked(False)
        self.toggle_action.triggered.connect(self.toggle_label)

        # Widgets that use the same QAction- both the toolbar_checkbox and the QPushbutton  self.central_button
        self.toolbar_checkbox = QCheckBox("Toggle via CheckBox (Shared QAction)")
        self.toolbar_checkbox.stateChanged.connect(
            lambda state: self.toggle_action.setChecked(state == Qt.Checked)
        )

        self.central_button = QPushButton("Toggle via Button (Shared QAction)")
        self.central_button.clicked.connect(self.toggle_action.trigger)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.toolbar_checkbox)
        layout.addWidget(self.central_button)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        # === TOOLBAR SETUP ===
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        toolbar.addAction(self.toggle_action)

    def toggle_label(self, checked):
        if checked:
            self.label.setText("Toggled ON!")
        else:
            self.label.setText("Toggled OFF!")
        self.toolbar_checkbox.setChecked(checked)  # Keep checkbox synced

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
