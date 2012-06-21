'''
Created on Jun 11, 2012

@author: Michael Reuter
'''
import sqlite3
from lunar_feature import LunarFeature
import utils

ID, NAME, DIAMETER, LATITUDE, LONGITUDE, D_LAT, D_LONG, TYPE, QUAD_NAME, \
QUAD_CODE, LUNAR_CODE, LUNAR_CLUB_TYPE = range(12)

class LunarFeatureContainer(object):
    '''
    This class is responsible for gathering and distributing the lunar 
    feature information.
    '''
    DEBUG = True


    def __init__(self, dbname="lct/db/moon.db"):
        '''
        Constructor
        '''
        self.conn = sqlite3.connect(dbname)
        self.features = {}
        self.club_type = set()
        self.feature_type = set()
        
    def __len__(self):
        '''
        This function gives the number of Lunar features.
        @return: The number of lunar features in the container.
        '''
        return len(self.features)
    
    def __iter__(self):
        '''
        This function allows the container to be iterable.
        @return: The current feature object.
        '''
        for feature in self.features.values():
            yield feature
            
    def load(self):
        '''
        This function reads the database and creates a feature for every 
        record. It then fills a dictionary and a couple of sets with 
        information that tree views will need.
        '''
        obs_info = utils.ObservingInfo()
        c = self.conn.cursor()
        c.execute('select * from Features')
        for row in c:
            feature = LunarFeature(row[NAME], row[LATITUDE], row[LONGITUDE],
                                   row[TYPE], row[D_LAT], row[D_LONG],
                                   row[LUNAR_CODE], row[LUNAR_CLUB_TYPE])
            if LunarFeatureContainer.DEBUG or obs_info.moon_info.isVisible(feature):
                self.features[id(feature)] = feature
                self.club_type.add(row[LUNAR_CLUB_TYPE])
                self.feature_type.add(row[TYPE])
if __name__ == "__main__":
    lfc = LunarFeatureContainer("../db/moon.db")
    lfc.load()
    print lfc.features
