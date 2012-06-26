'''
Created on Jun 9, 2012

@author: Michael Reuter
'''
import math
import utils

class StrFmt(object):
    '''
    This is a static class that will handle string formatting
    '''

    def __init__(self):
        '''
        Constructor. Do nothing as this class will be used statically.
        '''
        pass
    
    @classmethod
    def floatString(cls, ifloat, precision):
        """
        This function prints a float as a string with a given precision.
        """
        fmt = "%%.%df" % precision
        return fmt % ifloat
    
    @classmethod
    def ddString(cls, decdeg, precision, coord_type):
        '''
        This function returns a string representation of a decimal degrees 
        coordinate.
        @param decdeg: The decimal degrees coordinate.
        @param precision: The precision for formatting the coordinate.
        @param coord_type: The particular coordinate type.
        @return: The formatting decimal degree string.
        '''
        dir_tag = ''
        if coord_type == utils.LATITUDE:
            if decdeg < 0:
                decdeg = math.fabs(decdeg)
                dir_tag = "S"
            else:
                dir_tag = "N"
        if coord_type == utils.LONGITUDE:
            if decdeg < 0:
                decdeg = math.fabs(decdeg)
                dir_tag = "W"
            else:
                dir_tag = "E"
                
        dd_str = cls.floatString(decdeg, precision)
        return dd_str + u'\u00b0' + ' ' + dir_tag