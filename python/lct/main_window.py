'''
Created on Jun 1, 2012
@author: Michael Reuter
'''
from PyQt4 import QtGui
import ui

class LunarClubTools(QtGui.QMainWindow, ui.Ui_MainWindow):
    '''
    This is the main class for the program.
    '''
    
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(LunarClubTools, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        
        self.updateUI()
        
    def updateUI(self):
        self.moonInfoTab.updateUI()
        self.featuresTab.updateUI()
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("Type II Software")
    app.setApplicationName("Lunar Club Tools")
    form = LunarClubTools()
    form.show()
    app.exec_()
    