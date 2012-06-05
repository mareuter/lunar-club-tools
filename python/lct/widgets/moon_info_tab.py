'''
Created on Jun 1, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui
import ui

class MoonInfoTab(QtGui.QWidget, ui.Ui_MoonInfoTabWidget):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(MoonInfoTab, self).__init__(parent)
        self.setupUi(self)