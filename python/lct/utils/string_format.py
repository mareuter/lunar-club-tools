'''
Created on Jun 9, 2012

@author: Michael Reuter
'''

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
    def float_string(cls, ifloat, precision):
        """
        This function prints a float as a string with a given precision.
        """
        fmt = "%%.%df" % precision
        return fmt % ifloat