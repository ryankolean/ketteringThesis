#!/usr/bin/python2

from PyQt4 import QtGui, QtCore
import sys

class ClusterWarning(QtGui.QDialog):
    def __init__(self, action):
        super(ClusterWarning, self).__init__()
        self.initUI(action)

    # closeClicked - called to close the panel on button click
    def closeClicked(self):
        self.close()

    def initUI(self, action):
        # Set up the Layouts
        self.layout = QtGui.QVBoxLayout()

        message = QtGui.QTextEdit()
        # SWITCH THE MESSAGE DEPENDING ON ACTION VALUE:
        # 0 = POWER OFF
        if ( action == 0 ):
            actionName = 'POWER OFF'
            message.setText('<center> A <b>%s</b>  operation on the Cluster Management Node will cause all connected machines to also perform a <b>%s</b>.\nDo you wish to proceed?</center>' % (actionName, actionName))
        # 1 = POWER ON
        elif ( action == 1 ):
            actionName = 'POWER ON'
            message.setText('<center> A <b>%s</b> operation on the Cluster Management Node will cause all connected machines to also perform a <b>%s</b>.\nDo you wish to proceed?</center>' % (actionName, actionName))
        # 2 = REBOOT 
        elif ( action == 2 ):
            actionName = 'REBOOT'
            message.setText('<center> A <b>%s</b>  operation on the Cluster Management Node will cause all connected machines to also perform a <b>%s</b>.\nDo you wish to proceed?</center>' % (actionName, actionName))
        self.layout.addWidget(message)

        # Make Buttons
        buttonLayout = QtGui.QHBoxLayout()

        cancelButton = QtGui.QPushButton('Cancel')
        acceptButton = QtGui.QPushButton('Accept')
        cancelButton.clicked.connect(self.closeClicked)
        acceptButton.clicked.connect(self.closeClicked)
        # EXECUTE THE COMMAND HERE - CONNECT THE ACCEPT BUTTON CLICK TO THE ACTIONS SLOT AS WELL
        buttonLayout.addWidget(cancelButton)
        buttonLayout.addWidget(acceptButton)

        self.layout.addLayout(buttonLayout)

        self.setLayout(self.layout)
        self.setWindowTitle('WARNING')
        # Give the Window dimensions
        self.setGeometry(50, 50, 255, 285)
        # Draw the window
        #self.setModal(True)
        self.show()


# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = ClusterWarning()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

