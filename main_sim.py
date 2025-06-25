from PySide6 import QtCore, QtWidgets, QtGui
from styles import Buttons
import sys

from side_classes import Grid

## ---------------Abbreviations----------------- ##
fixed_size = QtWidgets.QSizePolicy.Policy.Fixed
align_left = QtCore.Qt.AlignmentFlag.AlignLeft

## ---------------Repetitive elements----------- ##
def page_title(title:str, location:tuple, size:tuple, parent=None):
    screen_title = QtWidgets.QLabel(title, parent)
    screen_title.setFixedSize(*size)
    screen_title.move(*location)
    return screen_title

def button_and_label(b_size:tuple, l_size:tuple, location: tuple, parent=None):
    button1 = QtWidgets.QPushButton("MODE", parent)
    button1.setStyleSheet(Buttons.button_style_1)
    button1.setFixedSize(50, 30)
    label1 = QtWidgets.QLabel("Mode Label", parent)
    label1.setFixedSize(100, 30)
    button1.move(20, 20)
    label1.move(90, 20)
    return button1, label1


## ---------------PAGE FUNCTIONS---------------- ##
def config_pg():
    widget = QtWidgets.QWidget()

    def render_buttons():
        buttons = []
        labels = []

        # MODE
        button1 = QtWidgets.QPushButton("MODE", widget)
        button1.setStyleSheet(Buttons.button_style_1)
        button1.setFixedSize(50, 30)
        label1 = QtWidgets.QLabel("Mode Label", widget)
        label1.setFixedSize(100, 30)
        button1.move(20, 20)
        label1.move(90, 20)
        buttons.append(button1)
        labels.append(label1)

        # SYRINGE
        button2 = QtWidgets.QPushButton("SYRINGE", widget)
        button2.setStyleSheet(Buttons.button_style_1)
        button2.setFixedSize(50, 30)
        label2 = QtWidgets.QLabel("Syringe Label", widget)
        label2.setFixedSize(100, 30)
        button2.move(20, 70)
        label2.move(90, 70)
        buttons.append(button2)
        labels.append(label2)

        # RATES
        button3 = QtWidgets.QPushButton("RATES", widget)
        button3.setStyleSheet(Buttons.button_style_1)
        button3.setFixedSize(50, 30)
        label3 = QtWidgets.QLabel("Rates Label", widget)
        label3.setFixedSize(100, 30)
        button3.move(20, 120)
        label3.move(90, 120)
        buttons.append(button3)
        labels.append(label3)

        # TARGET
        button4 = QtWidgets.QPushButton("TARGET", widget)
        button4.setStyleSheet(Buttons.button_style_1)
        button4.setFixedSize(50, 30)
        label4 = QtWidgets.QLabel("Target Label", widget)
        label4.setFixedSize(100, 30)
        button4.move(20, 170)
        label4.move(90, 170)
        buttons.append(button4)
        labels.append(label4)

    page_title("Configuration",(100,90), widget)
    render_buttons()

    # --- Add grid overlay ---
    grid = Grid(widget)
    grid.resize(widget.size())
    grid.raise_()  # move grid to top of stack

    def on_resize(event):
        grid.resize(widget.size())
        return QtWidgets.QWidget.resizeEvent(widget, event)
    widget.resizeEvent = on_resize

    return widget

def setup_pg():
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)

    label = QtWidgets.QLabel("Info Page", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

    layout.addWidget(label)
    return widget

def run_pg(): 
    widget = QtWidgets.QWidget()
    return widget

# what returns everyhting
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create page title and define the "stacked" widget
        self.setWindowTitle("KDS Legato 110 Serial Control Simulator")
        self.stack = QtWidgets.QStackedWidget()

        # define size of window
        self.setFixedSize(500, 300)
        self.setContentsMargins(0,0,0,0)

        # add pages/screens to the stack
        self.stack.addWidget(config_pg())
        self.stack.addWidget(setup_pg())
        self.stack.addWidget(run_pg())

        # main page layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.stack)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
