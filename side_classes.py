import sys
from PySide6 import QtCore, QtWidgets, QtGui

## ----------------------SUB CLASSES------------------- ##
# grid for positioning items
class Grid(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setStyleSheet("background: transparent;")

        # Set up layout with no margins
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.QColor(180, 180, 180, 120))  # light gray, semi-transparent
        pen.setWidth(1)
        painter.setPen(pen)
        w, h = self.width(), self.height()
        step = 50
        
        x = 0
        while x < w:
            painter.drawLine(x, 0, x, h)
            x += step
        
        y = 0
        while y < h:
            painter.drawLine(0, y, w, y)
            y += step
        painter.end()
