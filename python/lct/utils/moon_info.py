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
    
    NM, WAXING_CRESENT, FQ, WAXING_GIBBOUS, FM, WANING_GIBBOUS, TQ, \
    WANING_CRESENT = range(8)
    PHASE_NAMES = ("New Moon", "Waxing Cresent", "First Quarter", 
                   "Waxing Gibbous", "Full Moon", "Waning Gibbous",
                   "Third Quarter", "Waning Cresent")
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
    
    def _getPhase(self):
        '''
        This function returns the moon phase according to standard nomenclature.
        @return: The moon phase as an enum value.
        '''
        colong = self._moon.colong
        if colong == 270.0:
            return MoonInfo.NM
        if 270.0 < colong < 360.0:
            return MoonInfo.WAXING_CRESENT
        if colong == 0.0 or colong == 360.0:
            return MoonInfo.FQ
        if 0.0 < colong < 90.0:
            return MoonInfo.WAXING_GIBBOUS
        if colong == 90.0:
            return MoonInfo.FM
        if 90.0 < colong < 180.0:
            return MoonInfo.WANING_GIBBOUS
        if colong == 180.0:
            return MoonInfo.TQ
        if 180.0 < colong < 270.0:
            return MoonInfo.WANING_CRESENT
    
    def getPhaseAsString(self):
        '''
        This function returns the phase of the moon as a string.
        @return: The moon phase as a string.
        '''
        return MoonInfo.PHASE_NAMES[self._getPhase()]
    
    def _getTimeOfDay(self):
        '''
        This function determines the current time of day on the moon. In 
        otherwords, if the sun is rising on the moon it is (morning) or if the 
        sun is setting on the moon it is evening.
        @return: The current time of day.
        '''
        phase = self._getPhase()
        if phase in (MoonInfo.NM, MoonInfo.WAXING_CRESENT, MoonInfo.FQ,
                     MoonInfo.WAXING_GIBBOUS):
            return MoonInfo.MORNING
        if phase in (MoonInfo.FM, MoonInfo.WANING_GIBBOUS, MoonInfo.TQ,
                     MoonInfo.WANING_CRESENT):
            return MoonInfo.EVENING
