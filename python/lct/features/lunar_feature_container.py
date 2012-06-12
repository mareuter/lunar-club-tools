'''
Created on Jun 11, 2012

@author: Michael Reuter
'''
import sqlite3
from lunar_feature import LunarFeature

class LunarFeatureContainer(object):
    '''
    This class is responsible for gathering and distributing the lunar 
    feature information.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.con = sqlite3.connect("moon.db")