import sys
from PyQt4 import QtGui, QtCore

### How can I use QtGui.QWidget here??? ###

class Example(QtGui.QMainWindow):                                  
     def __init__(self):
          super(Example, self).__init__()
          self.initUI()

     def initUI(self):               

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))    
        self.setToolTip('This is a <b>QWidget</b> Window widget')

        exitAction = QtGui.QAction(QtGui.QIcon('exit-icon-2.png'), '&Exit', self)

        exitAction.setShortcut('Ctrl+Q')                        
        exitAction.setStatusTip('Exit/Terminate application')   

        exitAction.triggered.connect(QtGui.qApp.quit)           

        self.statusBar()                                       

        menubar = self.menuBar()                                
        menubar.setToolTip('This is a <b>QWidget</b> for MenuBar')                                

        fileMenu = menubar.addMenu('&File')                     
        fileMenu.addAction(exitAction)                          
        toolbar = self.addToolBar('Exit')                       
        toolbar.addAction(exitAction)                           

        qbtn = QtGui.QPushButton('Quit', self)                  

        qbtn.setToolTip('This is a <b>QPushButton</b> widget')  
        qbtn.clicked.connect(self.launchAAA)                    
        qbtn.resize(qbtn.sizeHint())                           
        qbtn.move(170, 190)                                     



        self.setGeometry(500, 180, 400, 400)                    
        self.setWindowTitle('Quit button with Message')        
        self.show()                                            

    def launchAAA(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:  
           QtGui.QApplication.quit()
        else:
           pass                                              


def main():

   app = QtGui.QApplication(sys.argv)                          
   ex=Example()

   sys.exit(app.exec_())                                       


if __name__ == '__main__':
   main() 
