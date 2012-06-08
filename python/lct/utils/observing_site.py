'''
Created on Jun 1, 2012
@author: Michael Reuter
'''
import ephem
import os
import time

class ObservingSite(object):
    '''
    This class handles the information for the observing site include 
    latitude/longitude and date/time
    '''
    _name = "Oak Ridge, TN"
    _latitude = (35, 58, 10)
    _longitude = (-84, 19, 0)
    _observer = None

    def __init__(self):
        '''
        Constructor
        '''
        curtime = time.time()
        obdatetime = ephem.Date(time.gmtime(curtime)[:-3])
        self._observer = ephem.Observer()
        self._observer.date = obdatetime
        self._observer.lat = self.toCoordString("lat")
        self._observer.long = self.toCoordString("long")
    
    def __str__(self):
        result = []
        result.append("Latitude: %s" % self.toCoordString("lat"))
        result.append("Longitude: %s" % self.toCoordString("long"))
        result.append("DateTime: %s" % self.getDateTime())
        return os.linesep.join(result)
    
    def _tupleToString(self, coordinate):
        return ":".join([str(x) for x in coordinate])
    
    def toCoordString(self, coord_type):
        coord = getattr(self, "_"+coord_type+"itude")
        return self._tupleToString(coord)
    
    def toCoordTuple(self, coord_type):
        return getattr(self, "_"+coord_type+"itude")
    
    def getDateTime(self):
        return self._observer.date
    
    def getObserver(self):
        return self._observer
        
if __name__ == "__main__":
    obs = ObservingSite()
    print obs
    
    