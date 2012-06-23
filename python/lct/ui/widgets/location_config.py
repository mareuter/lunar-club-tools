'''
Created on Jun 22, 2012

@author: Michael Reuter
'''
from PyQt4 import QtCore, QtGui
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
        
        # Validator for degrees
        degval = QtGui.QIntValidator()
        degval.setRange(0, 180)
        # Validator for minutes/seconds
        hexval = QtGui.QIntValidator()
        hexval.setRange(0, 60)
        
        self.lat_deg_edit.setValidator(degval)
        self.lat_min_edit.setValidator(hexval)
        self.lat_sec_edit.setValidator(hexval)
        
        self.long_deg_edit.setValidator(degval)
        self.long_min_edit.setValidator(hexval)
        self.long_sec_edit.setValidator(hexval)
        
    def setLocation(self):
        obs_info = utils.ObservingInfo()
        lat_deg = self.lat_deg_edit.text().toInt()[0]
        lat_min = self.lat_min_edit.text().toInt()[0]
        lat_sec = self.lat_sec_edit.text().toInt()[0]
        lat_dir = self.lat_dir_cb.currentText()
        if lat_dir == 'S':
            lat_deg *= -1
    
        long_deg = self.long_deg_edit.text().toInt()[0]
        long_min = self.long_min_edit.text().toInt()[0]
        long_sec = self.long_sec_edit.text().toInt()[0]
        long_dir = self.long_dir_cb.currentText()
        if long_dir == 'W':
            long_deg *= -1
        
        obs_info.obs_site.setLocationName(self.loc_edit.text())
        obs_info.obs_site.fromCoordTuple('lat', (lat_deg, lat_min, lat_sec))
        obs_info.obs_site.fromCoordTuple('long', (long_deg, long_min, long_sec))
        self.emit(QtCore.SIGNAL("updateLocation"))
        