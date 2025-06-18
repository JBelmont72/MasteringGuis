# Mastering Guis   stacked layout of page 94 of matin Fitz[atrick 'clinical gui applications eiyh python and PyQt5'
# /Users/judsonbelmont/Downloads/MasteringGuis/pyqt5-source/basic/layout_9_Stacked_Tabs_Buttons.py
#  stacked Layout,  ended up using stacked Widget 
# [Chat](https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb)
# import sys

# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QTabWidget,
# )

# from layout_colorwidget import Color


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         tabs = QTabWidget()
#         tabs.setTabPosition(QTabWidget.West)
#         tabs.setMovable(True)

#         for color in ["red", "green", "blue", "yellow"]:
#             tabs.addTab(Color(color), color)

#         self.setCentralWidget(tabs)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTabWidget, QStackedWidget, QLabel
)
from PyQt5.QtCore import Qt


# Dummy color widget for demonstration
class Color(QWidget):
    def __init__(self, color_name):
        super().__init__()
        self.setStyleSheet(f"background-color: {color_name};")
        layout = QVBoxLayout()
        label = QLabel(color_name)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabs and Buttons - Synced View")
        self.colors = ["yellow", "red", "magenta", "blue"]

        # Main layout
        layout = QVBoxLayout()

        # Create the shared stacked widget
        self.stack = QStackedWidget()
        for color in self.colors:
            self.stack.addWidget(Color(color))
        layout.addWidget(self.stack)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.setMovable(True)
        for i, color in enumerate(self.colors):
            self.tabs.addTab(QWidget(), color)  # Dummy tabs just for labels
        self.tabs.currentChanged.connect(self.stack.setCurrentIndex)
        layout.addWidget(self.tabs)

        # Buttons
        button_layout = QHBoxLayout()
        for i, color in enumerate(self.colors):
            btn = QPushButton(color)
            btn.clicked.connect(lambda _, index=i: self.stack.setCurrentIndex(index))
            button_layout.addWidget(btn)
        layout.addLayout(button_layout)

        # Central widget setup
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
'''
✅ What This Fixes:
One set of colored pages inside a single QStackedWidget.
Both the QTabWidget and the QPushButtons now change the same stack view.
Minimal, readable layout logic.
Thanks for your patience. Here's a corrected explanation and working structure that ensures both the buttons and the tabs control the same view using a shared QStackedWidget.

Problem in Your Code
You created two parallel sets of widgets: one for the tabs (tabs.addTab(Color(color))) and one for the buttons (self.stacklayout.addWidget(Color(color))).
But they are not synced: the tabs and buttons are connected to different widgets, so they don't update the same display.
✅ Working Approach
You only need one QStackedWidget that both the tabs and buttons can control.

| What Was Changed                                  | Why                                                     |
| ------------------------------------------------- | ------------------------------------------------------- |
| Switched from `QStackedLayout` → `QStackedWidget` | `QStackedWidget` is a visible widget, not just a layout |
| `stacked_widget` is directly displayed            | Ensures you *see* color changes                         |
| Tabs use empty `QWidget()`s, only for control     | So you can select without replacing the display         |
| Buttons connect via `lambda` with correct scope   | Ensures buttons trigger correct index                   |





'''
