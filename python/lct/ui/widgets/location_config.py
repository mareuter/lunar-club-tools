'''
Created on Jun 22, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui
from ui_location_config import Ui_LocationConfigDialog
import utils

class LocationConfig(QtGui.QDialog, Ui_LocationConfigDialog):
    '''
    This dialog is for setting the latitude and longitude for an observing 
    location.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(LocationConfig, self).__init__(parent)
        self.setupUi(self)
        
    def setLocation(self):
        obs_info = utils.ObservingInfo()