#!/usr/bin/python2

from PyQt4 import QtGui, QtCore
import sys

class Info(QtGui.QDialog):
    def __init__(self):
        super(Info, self).__init__()
        self.initUI()

    def makeInfoBox(self, name, string):
        thisLayout = QtGui.QVBoxLayout()
        lineEdit = QtGui.QLineEdit(string)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        thisBox = QtGui.QGroupBox(name)
        thisBox.setLayout(thisLayout)
        self.layout.addWidget(thisBox)

    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        button.setPalette(color)
        return button    

    def closeClicked(self):
        self.close()

    def initUI(self):
        
        # Set up the Layouts
        self.layout = QtGui.QVBoxLayout()

        ## Create the Labels and Text Fields for the values
        #self.makeInfoBox('AWESIM VERSION', 'SMMTT 8.3')
        #self.makeInfoBox('AWESIM ARRAY DATA VERSION', 'SMMTT 8.3')
        #self.makeInfoBox('AMPS DATA VERSION', 'SMMTT 8.3')
        #self.makeInfoBox('STAPLE VERSION', 'STAPLE 5.5')
        #self.makeInfoBox('PLATFORM CLASS', 'SSN###')
        #self.makeInfoBox('PROCESSOR TYPE(S)', 'HS22 Blade')
        #self.makeInfoBox('TACTICAL COFIGURATION', 'TI10/APB11')

        infoArray = [ ['AWESIM VERSION', 'SMMTT 8.3'],
                       ['AWESIM ARRAY DATA VERSION', 'SMMTT 8.3'],
                       ['AMPS DATA VERSION', 'SMMTT 8.3'],
                       ['STAPLE VERSION', 'STAPLE 5.5'],
                       ['PLATFORM CLASS', 'SSN###'], 
                       ['PROCESSOR TYPE(S)', 'HS22 Blade'],
                       ['TACTICAL COFIGURATION', 'TI10/APB11'] ]

        for i in infoArray:
            self.makeInfoBox(i[0], i[1])


	# Close button
        closeButton = self.makeActionButton('CLOSE', '', 200, 30)
        closeButton.clicked.connect(self.closeClicked)
        self.layout.addWidget(closeButton)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 150, 400)
        self.setWindowTitle('AWESIM INFO')
        #self.setModal(True)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Info()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
