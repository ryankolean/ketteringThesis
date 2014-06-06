#!/usr/bin/python2

from PyQt4 import QtGui, QtCore
import sys

from awesimEmergencyControl import EmergencyControl

class Confirm(QtGui.QDialog):
    def __init__(self, array):
        super(Confirm, self).__init__()
        self.initUI(array)

    # closeClicked - called to close the panel on button click
    def closeClicked(self):
        self.close()

    def slotEmergencyControl(self, arrayName):
        self.arrayControl = EmergencyControl(arrayName)
        self.arrayControl.exec_()

    def initUI(self, array):
        
        # Set up the Layouts
        self.layout = QtGui.QVBoxLayout()

        message = QtGui.QTextEdit()
        message.setText('<center>By clicking ACCEPT to this message, the user is confirming that they are full aware of any repercussions that might occur when performing a start, stop, and/or restart on the <B>%s</B> array.</center>\n<center>This utility is only meant to start, stop, or restart the <B>%s</B> when there is no other option. Please exhaust all other options before executing any actions in the following control panel.</center>' % (array, array))
        message.setReadOnly(True)
        self.layout.addWidget(message)

        # Make Buttons
        buttonLayout = QtGui.QHBoxLayout()
        
        cancelButton = QtGui.QPushButton('Cancel')
        acceptButton = QtGui.QPushButton('Accept')

        cancelButton.clicked.connect(self.closeClicked)
        # accept button needs to close the window and launch the next window
        acceptButton.clicked.connect(self.closeClicked)
        acceptButton.clicked.connect(lambda: self.slotEmergencyControl(array))

        buttonLayout.addWidget(cancelButton)
        buttonLayout.addWidget(acceptButton)
 
        self.layout.addLayout(buttonLayout)

        self.setLayout(self.layout)
        self.setWindowTitle('%s ARRAY WARNING' % (array))
        # Give the Window dimensions
        self.setGeometry(50, 50, 255, 285)
        # Draw the window
        #self.setModal(True)
        self.show()


# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Confirm()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
