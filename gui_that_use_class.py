import sys
from PyQt4 import QtGui, QtCore
from Sat_Reader import Reader

class Example(QtGui.QMainWindow, Reader):
    
    def __init__(self):
        super(Example, self).__init__()
        Reader.__init__(self)
        
        self.initUI()
        self.string1 = ' '
        
    def initUI(self):      

        parse_list = []    

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.show()   
      
     #supposed to call web parser when button is pressed   
    def buttonClicked(self):
  

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.string1 = 'COSMOS 1174'
        string1 = ' '
        string1 = sender.text()
        print (self.Read_TLE(self.string1))
        print ' '
        print(self.SAT_BIO(self.string1))
        print string1
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':    
    main()