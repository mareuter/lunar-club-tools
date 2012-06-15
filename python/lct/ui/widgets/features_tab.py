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
        self.features = features.LunarFeatureContainer()
        
    def updateUI(self):
        self.features.load()
        self.populateLunarClubTree()
        self.populateLunarIITree()
        
    def populateLunarClubTree(self):
        self.lunar_club_tree.clear()
        self.lunar_club_tree.setColumnCount(2)
        self.lunar_club_tree.setHeaderLabels(["Target/Type/Name", "Latitude"])
        self.lunar_club_tree.setItemsExpandable(True)
        parentFromTarget = {}
        parentFromType = {}
        for feature in self.features:
            if feature.code_name in ("Lunar", "Both"):
                ancestor = parentFromTarget.get(feature.club_type)
                if ancestor is None:
                    ancestor = QtGui.QTreeWidgetItem(self.lunar_club_tree,
                                                     [feature.club_type])
                    parentFromTarget[feature.club_type] = ancestor
                    targettype = feature.club_type + "/" + feature.feature_type
                    parent = parentFromType.get(targettype)
                    if parent is None:
                        parent = QtGui.QTreeWidgetItem(ancestor, 
                                                       [feature.feature_type])
                        parentFromType[targettype] = parent
                        item = QtGui.QTreeWidgetItem(parent, [feature.name,
                                                              QtCore.QString("%L1").arg(feature.latitude)])
                        item.setTextAlignment(1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        self.lunar_club_tree.expandItem(parent)
                        self.lunar_club_tree.expandItem(ancestor)
        
    def populateLunarIITree(self):
        self.lunar_ii_tree.clear()
        self.lunar_ii_tree.setColumnCount(2)
        self.lunar_ii_tree.setHeaderLabels(["Type/Name", "Latitude"])
        self.lunar_ii_tree.setItemsExpandable(True)
        parentFromType = {}
        for feature in self.features:
            if feature.code_name in ("LunarII", "Both"):
                ancestor = parentFromType.get(feature.club_type)
                if ancestor is None:
                    ancestor = QtGui.QTreeWidgetItem(self.lunar_ii_tree,
                                                     [feature.feature_type])
                    parentFromType[feature.feature_type] = ancestor
                    item = QtGui.QTreeWidgetItem(ancestor, [feature.name,
                                                            QtCore.QString("%L1").arg(feature.latitude)])
                    item.setTextAlignment(1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.lunar_ii_tree.expandItem(ancestor)

