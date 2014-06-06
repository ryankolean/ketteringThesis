#!/usr/bin/python2

from PyQt4 import QtGui, QtCore
import sys

class ClusterMediaTray(QtGui.QDialog):
    def __init__(self, bladeAssign):
        super(ClusterMediaTray, self).__init__()
        self.initUI(bladeAssign)

    # closeClicked - called to close the panel on button click
    def closeClicked(self):
        self.close()

    def initUI(self, bladeAssign):
        # Set up the Layouts
        self.layout = QtGui.QVBoxLayout()
        message = QtGui.QTextEdit()
        message.setText('<center> This media tray is currently assigned to Blade %s' % (bladeAssign))
        self.layout.addWidget(message)
        # Make Buttons
        buttonLayout = QtGui.QHBoxLayout()
        okButton = QtGui.QPushButton('OK')
        okButton.clicked.connect(self.closeClicked)
        # EXECUTE THE COMMAND HERE - CONNECT THE ACCEPT BUTTON CLICK TO THE ACTIONS SLOT AS WELL
        buttonLayout.addWidget(okButton)
        self.layout.addLayout(buttonLayout)
        self.setLayout(self.layout)
        self.setWindowTitle('MEDIA TRAY ASSIGNMENT')
        # Give the Window dimensions
        self.setGeometry(50, 50, 225, 50)
        # Draw the window
        #self.setModal(True)
        self.show()


# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = ClusterMediaTray()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

