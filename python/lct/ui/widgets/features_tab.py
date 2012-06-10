'''
Created on Jun 9, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui
from ui_features_tab import Ui_FeaturesTabWidget

class FeaturesTab(QtGui.QWidget, Ui_FeaturesTabWidget):
    '''
    This class is responsible for listing the features visible for the Lunar 
    Club and Lunar II clubs target lists.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(FeaturesTab, self).__init__(parent)
        self.setupUi(self)
        
    def updateUI(self):
        pass