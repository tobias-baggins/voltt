import sys
from PyQt6 import QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("app/ui/numpad.ui")
window.show()
app.exec()