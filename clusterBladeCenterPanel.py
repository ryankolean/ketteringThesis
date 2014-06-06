#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

class BladeCenterPanel(QtGui.QDialog):

    def __init__(self):
        super(BladeCenterPanel, self).__init__()
        self.font = QtGui.QFont()
        self.initUI()

    def closeClicked(self):
        self.close()
    
    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        self.font.setBold(True)
        button.setFont(self.font)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        color.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        button.setPalette(color)
        return button

    def makeInfoBox(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        label = QtGui.QLabel('%s:' % (name))
        self.font.setBold(True)
        label.setFont(self.font)
        thisLayout.addWidget(label)
        lineEdit = QtGui.QLineEdit(string)
        self.font.setBold(False)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        return thisLayout

    def makeInfoBoxExtended(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        label = QtGui.QLabel('%s:' % (name))
        self.font.setBold(True)
        label.setFont(self.font)
        thisLayout.addWidget(label)
        lineEdit = QtGui.QTextEdit()
        lineEdit.setPlainText(string)
        self.font.setBold(False)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        return thisLayout

    def initUI(self):
        # This will be used to to set the window's overall layout
        self.layout = QtGui.QVBoxLayout()
        dataLayout = QtGui.QHBoxLayout()
        textSize = 8

        # make 2 vertical layouts for 2 "columns"
        leftLayout = QtGui.QVBoxLayout()
        rightLayout = QtGui.QVBoxLayout()
        # make 2 frames from those column layouts
        leftFrame = QtGui.QFrame()
        leftFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        rightFrame = QtGui.QFrame()
        rightFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        # add data to col1Layout
        leftLayout.addLayout(self.makeInfoBox('IBM Machine Type', 'XYX Blade Center', textSize))
        leftLayout.addLayout(self.makeInfoBox('Model Number', '654HIJ87', textSize))
        leftLayout.addLayout(self.makeInfoBox('Serial Number', '123456789', textSize))
        leftLayout.addLayout(self.makeInfoBox('Physical Location', 'abc123ef45', textSize))
        leftLayout.addLayout(self.makeInfoBox('Media Tray Assignment', 'xxxxxx', textSize))
        leftLayout.addLayout(self.makeInfoBox('KVM Assignment', 'yyyyyyy', textSize))
        leftFrame.setLayout(leftLayout)
        # add data to col3Layout
        rightLayout.addLayout(self.makeInfoBox('AMM IP Address', '11.222.333.5757', textSize))
        rightLayout.addLayout(self.makeInfoBoxExtended('SWITCH IP Address(es)', '11.222.333.4545\n 11.222.333.5656', textSize))
        rightLayout.addLayout(self.makeInfoBoxExtended('BLADE IP Address(es)', '11.222.333.4444 \n11.222.333.5555 \n11.222.333.6666 \n11.222.333.7777 \n11.222.333.8888 \n11.222.333.9999 \n11.222.333.1212 \n11.222.333.1231 \n11.222.333.1232 \n11.222.333.1233 \n11.222.333.1234 \n11.222.333.1235 \n11.222.333.1236 \n11.222.333.1237', textSize)) 
        rightFrame.setLayout(rightLayout)
        # Add each column layout to lowerLayout
        dataLayout.addWidget(leftFrame)
        dataLayout.addWidget(rightFrame)
        self.layout.addLayout(dataLayout)

        closeButton = self.makeActionButton('CLOSE', '', 350, 25)
        closeButton.clicked.connect(self.closeClicked)
        self.layout.addWidget(closeButton) 

        # Finalize layout of window and display
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('BLADE CENTER PANEL')
        self.setGeometry(5, 5, 350, 300)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = BladeCenterPanel()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
