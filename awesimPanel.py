#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

from awesimConfirm import Confirm
from awesimWCA import WCA


class Panel(QtGui.QDialog):

    def __init__(self, array, panelData, procData, wcaData):
        super(Panel, self).__init__()
        self.font = QtGui.QFont()
        self.initUI(array, panelData, procData, wcaData)

    def closeClicked(self):
        self.close()
    
    # Slots for the button triggers
    def slotConfirm(self, arrayName):
        self.confirmWindow = Confirm(arrayName)
        self.confirmWindow.exec_()

    def slotWCA(self, wcaData):
        self.wcaWindow = WCA(wcaData)
        self.wcaWindow.exec_()

    def slotMessage(self, messageData):
        message = QtGui.QMessageBox(self)
        message.setText(messageData)
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.exec_()

    def makeProgressBar(self, percentage):
        progressBar = QtGui.QProgressBar(self)
        progressBar.setValue(percentage)
        progressBar.setAlignment(QtCore.Qt.AlignCenter)
        progressBar.setFont(self.font)
        progressBar.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
	if( percentage > 85 and percentage <= 110):
            progressColor = progressBar.palette()
            progressColor.setColor(QtGui.QPalette.Highlight, QtGui.QColor(0,102,0))
            progressBar.setPalette(progressColor)
        elif( percentage > 50 and percentage < 84 or percentage > 110 and percentage < 130):
            progressColor = progressBar.palette()
            progressColor.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255,221,68))
            progressBar.setPalette(progressColor)
        else:
            progressColor = progressBar.palette()
            progressColor.setColor(QtGui.QPalette.Highlight, QtGui.QColor(221,0,0))
            progressBar.setPalette(progressColor)
        return progressBar        

    def makeConnButton(self, state):
        labelIcon = QtGui.QLabel()
        if state == 1:
            pixmap = QtGui.QPixmap('images/checkmark.png')
        else:
            pixmap = QtGui.QPixmap('images/xmark.png')
        labelIcon.setPixmap(pixmap)
        labelIcon.setMinimumSize(25,25)
        return labelIcon

    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        self.font.setBold(True)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        button.setFont(self.font)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        color.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        button.setPalette(color)
        return button

    def makeBoldLabel(self, label):
        label = QtGui.QLabel(label)
        self.font.setBold(True)
        label.setFont(self.font)
        return label

    def makeLabel(self, label):
        label = QtGui.QLabel(label)
        self.font.setBold(False)
        label.setFont(self.font)
        return label


    def initUI(self, array, panelData, procData, wcaData):
        # This will be used to to set the window's overall layout
        self.layout = QtGui.QVBoxLayout()

        # Layouts/Frames to store the objects, ie. buttons, text, etc.
        dataLayout = QtGui.QHBoxLayout()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsFrame = QtGui.QFrame()
        buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)

        # Make grid for the arrays that are being passed in
        dataGrid = QtGui.QGridLayout()

        # Static list for the column headers of the grid 
        headerList = ['<center><b>CONNECTION NAME</b></center>',
                      '<center><b>IP/PORT ADDRESS</b></center>',
                      '<center><b>TACTICAL CONNECTION</b></center>',
                      '<center><b>METER QUEUE RATE</b></center>',
                      '<center><b>SEND RATE</b></center>']
        
        # Datalist is static now for testing, MUST BECOME DYNAMICALLY LOADED
        #dataList = [['%s_1' % (array), '11.222.333.444:5555', 'CONN', 100, 100],
        #            ['%s_2' % (array), '11.222.333.444:6666', 'CONN', 100, 100],
        #            ['%s_3' % (array), '11.222.333.444:7777', 'DISC', 15, 0],
        #            ['%s_4' % (array), '11.222.333.444:8888', 'CONN', 100, 100]]

        dataList = panelData

        k = 0
        # Fill the headers for each column in the grid
        for i in headerList:
            dataGrid.addWidget(self.makeBoldLabel(i), 0, k)
            k = k + 1

        j = 1
        # Fill in the actual data
        for i in dataList:
            dataGrid.addWidget(self.makeLabel(i[0]), j, 0)
            dataGrid.addWidget(self.makeLabel(i[1]), j, 1)
            dataGrid.addWidget(self.makeConnButton(i[2]), j, 2, QtCore.Qt.AlignCenter) 
            dataGrid.addWidget(self.makeProgressBar(i[3]), j, 3)
            dataGrid.addWidget(self.makeProgressBar(i[4]), j, 4)
            j = j + 1
        dataLayout.addLayout(dataGrid)

        # Make action buttons
        wcaButton = self.makeActionButton('WARNING/CAUTION/ADVISORY', 'View active warnings,\ncautions, and advisories\nfor %s' % (array), 170, 35)
        if not wcaData:
            wcaButton.clicked.connect(lambda: self.slotMessage('Currently no warnings, cautions, or advisories for the  %s' % (array)))
        else:
            wcaButton.clicked.connect(lambda: self.slotWCA(wcaData))
        controlButton = self.makeActionButton('START/STOP', 'Launch Array Control Panel', 170, 35)
        controlButton.clicked.connect(lambda: self.slotConfirm(array))
        closeButton = self.makeActionButton('CLOSE', 'Close this panel', 170, 35)
        closeButton.clicked.connect(self.closeClicked)

	# Add each button to buttonLayout
        buttonsLayout.addWidget(wcaButton)
        buttonsLayout.addWidget(controlButton)
        buttonsLayout.addWidget(closeButton)
        buttonsFrame.setLayout(buttonsLayout)

        # Add each layout into the overall layout
        self.layout.addLayout(dataLayout)        
        self.layout.addStretch(0)
        self.layout.addWidget(buttonsFrame)       

        # Finalize layout of window and display
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('%s ARRAY DIAGNOSTIC PANEL' % (array))
        self.setGeometry(50, 50, 900, 70)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Panel()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
