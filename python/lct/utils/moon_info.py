'''
Created on Jun 13, 2012

@author: Michael Reuter
'''
import ephem
import utils

class MoonInfo(object):
    '''
    This class is responsible for handling all of the information and 
    calculations dealing with the Moon.
    '''
    
    NM, FQ, FM, TQ = range(4)
    WAXING_CRESENT, WAXING_GIBBOUS, WANING_GIBBOUS, WANING_CRESENT = range(4)
    MORNING, EVENING = range(2)
    FEATURE_CUTOFF = 15.0 # degrees

    def __init__(self):
        '''
        Constructor
        '''
        self._moon = ephem.Moon()
        
    def compute(self, observer):
        '''
        This function sets the observer into the Moon object and triggers the 
        calculations for the Moon's parameters.
        @param observer: The object holding the current location and date/time.
        '''
        self._observer = observer
        self._moon.compute(self._observer)
            
    def age(self):
        '''
        This function returns the age of the Moon (time since New).
        @return: The age of the Moon in days.
        '''
        prev_new = ephem.previous_new_moon(self._observer.date)
        age = self._observer.date - prev_new
        return utils.StrFmt.floatString(age, 2)
        
    def colong(self):
        '''
        This function returns the current selenographic colongitude.
        @return: The selenographic colongitude in DMS.
        '''
        return str(self._moon.colong)
    
    def phase(self):
        '''
        This function returns the illuminated fraction of the Moon.
        @return: The fraction of the illuminated Moon (<=1).
        '''
        phase_fraction = self._moon.phase / 100.0
        return utils.StrFmt.floatString(phase_fraction, 2)
    
    def isVisible(self, lfeature):
        '''
        This function determines if the given lunar feature is visible based 
        on the current selenographic colongitude (SELCO). For most features 
        near the equator, from NM to FM once the SELCO recedes about 15 
        degrees, the shadow relief makes it tough to observe. Conversely, the 
        SELCO needs to be within 15 degrees of the feature from FM to NM. 
        Features closer to the poles are visible much longer after the 15 
        degree cutoff. A 1/cos(latitude) will be applied to the cutoff. 
        Mare are a special exception and once FULLY visible they are always 
        visible.
        @param lfeature: The lunar feature to check for visibility
        @return: True if the feature is visible.
        '''
        return True
    
    def _getTimeOfDay(self):
        colong = self._moon.colong
        if 270.0 <= colong < 360.0 or 0.0 <= colong < 90.0:
            return MoonInfo.MORNING
        if 90.0 <= colong < 180.0 or 180.0 <= colong < 270.0:
            return MoonInfo.EVENING
    
    def _getQuarter(self):
        '''
        This function determines the current lunar quarter based on the 
        selenographic colongitude.
        @return: The current lunar quarter.
        '''
        return MoonInfo.NM