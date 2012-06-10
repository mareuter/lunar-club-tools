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
    
    def _tupleToDmsString(self, coord_type):
        dir_str = ""
        coord = getattr(self, "_"+coord_type+"itude")
        if coord_type == "lat":
            if coord[0] < 0:
                dir_str = "S"
            else:
                dir_str = "N"
        if coord_type == "long":
            if coord[0] < 0:
                dir_str = "W"
            else:
                dir_str = "E"
        import math
        return str(int(math.fabs(coord[0])))+u'\u00b0 '+str(coord[1])+"\' "+ str(coord[2])+"\" "+dir_str  
    
    def toCoordString(self, coord_type):
        coord = getattr(self, "_"+coord_type+"itude")
        return self._tupleToString(coord)
    
    def toCoordTuple(self, coord_type):
        return getattr(self, "_"+coord_type+"itude")
    
    def getDateTime(self):
        local_time = ephem.localtime(self._observer.date)
        return str(local_time.strftime("%Y-%m-%dT%H:%M:%S%z"))
    
    def getLocalDate(self):
        return self.getDateTime().split('T')[0]
    
    def getLocalTime(self):
        return self.getDateTime().split('T')[-1]
    
    def getObserver(self):
        return self._observer
    
    def getLocationString(self):
        result = []
        result.append(self._tupleToDmsString("lat"))
        result.append(self._tupleToDmsString("long"))
        return "  ".join(result)
        
if __name__ == "__main__":
    obs = ObservingSite()
    print obs
    
    