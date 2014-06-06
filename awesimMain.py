#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore 

from awesimPanel import Panel
from awesimInfo import Info

from awesimData import awesimData

class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.font = QtGui.QFont()
        self.initUI()

    def slotPanel(self, arrayName, panelData, procData, wcaData):
        self.panel = Panel(arrayName, panelData, procData, wcaData)
        self.panel.exec_()

    def slotInfo(self):
        self.info = Info()
        self.info.exec_()

    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.font.setBold(True)
        button.setFont(self.font)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        color.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        button.setPalette(color)
        return button

    def makeArrayButton(self, label, state, sizeX, sizeY, panelData, procData, wcaData):
        button = QtGui.QPushButton(label)
        button.setMinimumSize(sizeX, sizeY)
        button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.font.setBold(True)
        button.setFont(self.font)
        buttonsColor = button.palette()
        if state == 1:
            buttonsColor.setColor(button.backgroundRole(), QtGui.QColor(0,102,0))
            buttonsColor.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        elif state == 2:
            buttonsColor.setColor(button.backgroundRole(), QtGui.QColor(255,221,68))
            buttonsColor.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        else:
            buttonsColor.setColor(button.backgroundRole(), QtGui.QColor(221,0,0))
            buttonsColor.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        button.setPalette(buttonsColor)
        button.clicked.connect(lambda: self.slotPanel(label, panelData, procData, wcaData))
        return button

    def initUI(self):
        # This will be used to to set the window's layout
        self.layout = QtGui.QVBoxLayout()

        # Layout box to store the two upper buttons
	upperBox = QtGui.QHBoxLayout()

        # Make 2 upper buttons for info and help, link them to slots
        infoButton = self.makeActionButton('INFO', 'Information on current environment', 302, 60)
        infoButton.clicked.connect(self.slotInfo)
        helpButton = self.makeActionButton('HELP/GUIDE', 'Browser based guide for AWESIM tool', 302, 60)

        # --------------------THE INPUT ---------------------- #
        # Center grid of arrays that will need to be self-populating
        # NEEDS TO BECOME SELF-POPULATING -> like bunnies 
        # Paradigm: ['arrayName', state?, [ipAddress&Port, connected?, meterQrate, sendQrate] ]
        # Note the ipPort, connected, meterQrate, and sendQrate each get their own list
        # True = 1, False = 0 for the time being, rates are 1-100
        # Then the Process array
        # Then the WCA array
        arrayList = awesimData.arrayList

        # Make grid layout for the array buttons
        arrayGrid = QtGui.QGridLayout()

	# Make grid for the arrays to populate
        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3)]

        # Place buttons using labels list and grid
        for i in arrayList:
            button = self.makeArrayButton(i[0], i[1], 148, 120, i[2], i[3], i[4])
            arrayGrid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        upperBox.addWidget(infoButton)
        upperBox.addWidget(helpButton)

        # -------------Matryoshka Assembly!---------------------
        # Widgets: should each be contained in a layout
        # Layouts: each get added to the main layout
        self.layout.addLayout(upperBox)        
        self.layout.addStretch(0)
        self.layout.addLayout(arrayGrid)

        # Finalize layout of window and show 
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('AWESIM')
        self.setGeometry(50, 50, 630, 440)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
