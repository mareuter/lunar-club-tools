'''
Created on Jun 9, 2012

@author: Michael Reuter
'''
from PyQt4 import QtGui, QtCore
from ui_features_tab import Ui_FeaturesTabWidget
import features

class FeaturesTab(QtGui.QWidget, Ui_FeaturesTabWidget):
    '''
    This class is responsible for listing the features visible for the Lunar 
    Club and Lunar II clubs target lists.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(FeaturesTab, self).__init__(parent)
        self.setupUi(self)
        self.features1 = features.LunarClubFeatureContainer()
        
    def updateUI(self):
        self.populateLunarClubTree()
        
    def populateLunarClubTree(self):
        self.features1.load()
        self.lunar_club_tree.clear()
        self.lunar_club_tree.setColumnCount(2)
        self.lunar_club_tree.setHeaderLabels("Target/Type/Name", "Latitude")
        self.lunar_club_tree.setItemsExpandable(True)
        parentFromTarget = {}
        parentFromType = {}
        for feature in self.features1:
            ancestor = parentFromTarget.get(feature.club_type)
            if ancestor is None:
                ancestor = QtGui.QTreeWidgetItem(self.lunar_club_tree,
                                           [feature.club_type])
                parentFromTarget[feature.club_type] = ancestor
            targettype = feature.club_type + "/" + feature.feature_type
            parent = parentFromType.get(targettype)
            if parent is None:
                parent = QtGui.QTreeWidgetItem(ancestor, [feature.feature_type])
                parentFromType[targettype] = parent
            item = QtGui.QTreeWidgetItem(parent, [feature.name, 
                                                  QtCore.QString("%L1").arg(feature.latitude)])
            item.setTextAlignment(1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.lunar_club_tree.expandItem(parent)
            self.lunar_club_tree.expandItem(ancestor)
        