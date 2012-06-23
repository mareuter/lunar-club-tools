'''
Created on Jun 1, 2012
@author: Michael Reuter
'''
from PyQt4 import QtCore, QtGui
import ui.widgets

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
        
        self.connect(self.actionExit, QtCore.SIGNAL("triggered()"),
                     self.close)
        self.connect(self.actionLocation, QtCore.SIGNAL("triggered()"),
                     self.openLocationConfigDialog)
        
        self.updateUI()
        
    def updateUI(self):
        self.moonInfoTab.updateUI()
        self.featuresTab.updateUI()
        
    def closeEvent(self, event):
        pass
        
    def openLocationConfigDialog(self):
        dialog = ui.widgets.LocationConfig()
        self.connect(dialog, QtCore.SIGNAL("updateLocation"), self.updateUI)
        if dialog.exec_():
            dialog.setLocation()
           
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("Type II Software")
    app.setApplicationName("Lunar Club Tools")
    form = LunarClubTools()
    form.show()
    app.exec_()
    