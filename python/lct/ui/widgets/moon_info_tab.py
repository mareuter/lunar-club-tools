'''
Created on Jun 1, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui
from ui_moon_info_tab import Ui_MoonInfoTabWidget
import utils

class MoonInfoTab(QtGui.QWidget, Ui_MoonInfoTabWidget):
    '''
    This class handles displaying common information about the Moon.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(MoonInfoTab, self).__init__(parent)
        self.setupUi(self)
        self._set_css_labels(self.obs_date_label, self.obs_time_label,
                            self.location_label, self.moon_age_label,
                            self.moon_colong_label, self.moon_phase_label)
        self._set_css_edits(self.obs_date_edit, self.obs_time_edit,
                            self.location_edit, self.moon_age_edit,
                            self.moon_colong_edit, self.moon_phase_edit)
        
    def updateUI(self):
        '''
        This function is responsible for updating the GUI widgets with the 
        current Moon information from the current observation time.
        '''
        obsinfo = utils.ObservingInfo()
        obsinfo.update()
        self.obs_date_edit.setText(obsinfo.obs_site.getLocalDate())
        self.obs_time_edit.setText(obsinfo.obs_site.getLocalTime())
        self.location_edit.setText(obsinfo.obs_site.getLocationString())
        self.moon_phase_edit.setText(obsinfo.moon_info.phase())
        self.moon_colong_edit.setText(obsinfo.moon_info.colong())
        self.moon_age_edit.setText(obsinfo.moon_info.age())
        
    def _set_css_labels(self, *args):
        '''
        This function sets the stylesheets for the labels.
        @param args: The set of QLabels to be styled. 
        '''
        for arg in args:
            arg.setStyleSheet(utils.CSS_MOON_INFO_LABELS)
        
    def _set_css_edits(self, *args):
        '''
        This function sets the stylesheets for the "lineedits".
        @param args: The set of QLabels to be styled. 
        '''
        for arg in args:
            arg.setStyleSheet(utils.CSS_MOON_INFO_EDITS)
        