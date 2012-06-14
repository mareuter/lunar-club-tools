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