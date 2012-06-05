'''
Created on Jun 1, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui
from ui_moon_info_tab import Ui_MoonInfoTabWidget

class MoonInfoTab(QtGui.QWidget, Ui_MoonInfoTabWidget):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(MoonInfoTab, self).__init__(parent)
        self.setupUi(self)