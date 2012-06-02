'''
Created on Jun 1, 2012
@author: Michael Reuter
'''
import ephem
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
        datetime = ephem.Date(time.gmtime(curtime)[:-3])
        self._observer = ephem.Observer()
        self._observer.date = datetime
        self._observer.lat = self.toCoordString("lat")
        self._observer.long = self.toCoordString("long")
    
    def _tupleToString(self, coordinate):
        return ":".join([str(x) for x in coordinate])
    
    def toCoordString(self, coord_type):
        coord = getattr(self, "_"+coord_type+"itude")
        return self._tupleToString(coord)
    
    def toCoordTuple(self, coord_type):
        return getattr(self, "_"+coord_type+"itude")
    
    def getDateTime(self):
        return self._observer.date
        
if __name__ == "__main__":
    obs = ObservingSite()
    print "Latitude:", obs.toCoordString("lat") 
    print "Longitude:", obs.toCoordString("long")
    print "DateTime:", obs.getDateTime()
    
    