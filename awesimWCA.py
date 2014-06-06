#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

class WCA(QtGui.QDialog):

    def __init__(self, wcaData):
        super(WCA, self).__init__()

        self.initUI(wcaData)

    def closeClicked(self):
        self.close()

    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        button.setFont(self.font)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        color.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))        
        button.setPalette(color)
        return button

    def makeWCALine(self, wcaType, wcaMessage, placeCounter):
        typeLabel = QtGui.QLabel(wcaType)
        messageLabel = QtGui.QLabel(wcaMessage)
        typeLabel.setFont(self.font)
        messageLabel.setFont(self.font)
        typePalette = typeLabel.palette()
        if 'W' in wcaType:
            typePalette.setColor(typeLabel.foregroundRole(), QtGui.QColor(221,0,0))
        elif 'C' in wcaType:
            typePalette.setColor(typeLabel.foregroundRole(), QtGui.QColor(193,96,0))
        typeLabel.setPalette(typePalette)
        messageLabel.setPalette(typePalette)
        self.wcaGrid.addWidget(typeLabel, placeCounter, 0)
        self.wcaGrid.addWidget(messageLabel, placeCounter, 1)
            

    def initUI(self, wcaData):

        self.font = QtGui.QFont()
        self.font.setBold(True)

        # This will be used to to set the window's layout
        self.layout = QtGui.QVBoxLayout()

        # Layout Boxes to Store things
        dataLayout = QtGui.QHBoxLayout()
        buttonsLayout = QtGui.QHBoxLayout()

        # Layout Boxes to hold each element of data
	wcaLayout = QtGui.QVBoxLayout()


        # Make grid for the arrays that are being passed in
        self.wcaGrid = QtGui.QGridLayout()
        j = 0 
        #dataList = [['W', 'Incomplete data'], 
        #            ['C', 'Unable to connect to server'], 
        #            ['A', 'Restart Server'], 
        dataList = wcaData
        for i in dataList:
            self.makeWCALine(i[0], i[1], j)
            j = j + 1

        ## Put grid into connectionLayout
        wcaLayout.addLayout(self.wcaGrid)

        # Make close button
        closeButton = self.makeActionButton('CLOSE', '', 175, 40)
        closeButton.clicked.connect(self.closeClicked)

        # Add data to dataLayout
        dataLayout.addLayout(wcaLayout)

	# Add buttons to buttonLayout
        buttonsLayout.addWidget(closeButton)

        # Collect layouts/widgets into one layout
        self.layout.addLayout(dataLayout)        
        self.layout.addStretch(0)
        self.layout.addLayout(buttonsLayout)       

        # Finalize layout of window and show
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('ACTIVE WCAs')
        self.setGeometry(50, 50, 50, 65)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = WCA()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
