'''
Created on Jun 1, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui
from ui_moon_info_tab import Ui_MoonInfoTabWidget
import utils

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
        self.moon_phase_edit.setValidator(QtGui.QDoubleValidator())
        self.moon_colong_edit.setValidator(QtGui.QDoubleValidator())
        
    def updateUI(self):
        obsinfo = utils.ObservingInfo()
        obsinfo.update()
        self.obs_date_edit.setText(obsinfo.obs_site.getLocalDate())
        self.obs_time_edit.setText(obsinfo.obs_site.getLocalTime())
        self.location_edit.setText(obsinfo.obs_site.getLocationString())
        self.moon_phase_edit.setText(obsinfo.moonPhase())
        self.moon_colong_edit.setText(obsinfo.moonColong())
        self.moon_age_edit.setText(obsinfo.moonAge())
        
        