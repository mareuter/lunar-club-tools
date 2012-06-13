'''
Created on Jun 11, 2012

@author: Michael Reuter
'''
from PyQt4 import QtCore
import os

class LunarFeature(object):
    '''
    This class is responsible for holding the information for a given lunar 
    feature.
    '''

    def __init__(self, name, latitude, longitude, feature_type,
                 delta_latitude, delta_longitude, club_type=None):
        '''
        Constructor
        '''
        self.name = QtCore.QString(name)
        self.latitude = latitude
        self.longitude = longitude
        self.feature_type = QtCore.QString(feature_type)
        self.delta_latitude = delta_latitude
        self.delta_longitude = delta_longitude
        #self.code_name = QtCore.QString(code_name)
        self.club_type = QtCore.QString(club_type)
        
    def __str__(self):
        result = []
        result.append("Name = %s" % self.name)
        result.append("Lat/Long = (%.2lf, %.2lf)" % (self.latitude, self.longitude))
        result.append("Type = %s" % self.feature_type)
        return os.linesep.join(result)
    
    def __repr__(self):
        return self.__str__()