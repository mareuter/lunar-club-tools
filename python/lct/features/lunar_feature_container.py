'''
Created on Jun 11, 2012

@author: Michael Reuter
'''
import sqlite3
from PyQt4 import QtXml
from lunar_feature import LunarFeature
from ui.qrc_resources import *
import utils

ID, NAME, DIAMETER, LATITUDE, LONGITUDE, D_LAT, D_LONG, TYPE, QUAD_NAME, \
QUAD_CODE, LUNAR_CODE, LUNAR_CLUB_TYPE = range(12)

class LunarClubFeatureContainer(object):
    '''
    This class is responsible for gathering and distributing the lunar 
    feature information.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # Prototype of XML feature DB that seems to work in program mode.
        fh = QtCore.QFile(QtCore.QString(":/moon.xml"))
        dom = QtXml.QDomDocument()
        dom.setContent(fh)
        root = dom.documentElement()
        print "C:", root.tagName()
        
        # DATABASE DOES NOT WORK IN PROGRAM MODE! ONLY STANDALONE! Sigh
        self.conn = sqlite3.connect(":/db/moon.db")
        self.features = {}
        self.club_type = set()
        self.feature_type = set()
        
    def __len__(self):
        return len(self.features)
    
    def __iter__(self):
        for feature in self.features.values():
            yield feature
            
    def load(self):
        obs_info = utils.ObservingInfo()
        c = self.conn.cursor()
        c.execute('select * from Features')
        for row in c:
            lun_code = row[LUNAR_CODE]
            if lun_code in ("Lunar", "Both"):
                feature = LunarFeature(row[NAME], row[LATITUDE], row[LONGITUDE],
                                       row[TYPE], row[D_LAT], row[D_LONG],
                                       row[LUNAR_CLUB_TYPE])
                self.features[id(feature)] = feature
                self.club_type.add(row[LUNAR_CLUB_TYPE])
                self.feature_type.add(row[TYPE])
                
if __name__ == "__main__":
    lcfc = LunarClubFeatureContainer()
    lcfc.load()
    print lcfc.features