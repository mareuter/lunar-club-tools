# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\ui\widgets\features_tab.ui'
#
# Created: Sat Jun 09 21:54:33 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FeaturesTabWidget(object):
    def setupUi(self, FeaturesTabWidget):
        FeaturesTabWidget.setObjectName(_fromUtf8("FeaturesTabWidget"))
        FeaturesTabWidget.resize(538, 239)
        FeaturesTabWidget.setWindowTitle(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(FeaturesTabWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(FeaturesTabWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lunar_club_label = QtGui.QLabel(self.widget)
        self.lunar_club_label.setObjectName(_fromUtf8("lunar_club_label"))
        self.verticalLayout.addWidget(self.lunar_club_label)
        self.treeView = QtGui.QTreeView(self.widget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout.addWidget(self.treeView)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lunar_ii_label = QtGui.QLabel(self.widget1)
        self.lunar_ii_label.setObjectName(_fromUtf8("lunar_ii_label"))
        self.verticalLayout_2.addWidget(self.lunar_ii_label)
        self.treeView_2 = QtGui.QTreeView(self.widget1)
        self.treeView_2.setObjectName(_fromUtf8("treeView_2"))
        self.verticalLayout_2.addWidget(self.treeView_2)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(FeaturesTabWidget)
        QtCore.QMetaObject.connectSlotsByName(FeaturesTabWidget)

    def retranslateUi(self, FeaturesTabWidget):
        self.lunar_club_label.setText(QtGui.QApplication.translate("FeaturesTabWidget", "Lunar Club", None, QtGui.QApplication.UnicodeUTF8))
        self.lunar_ii_label.setText(QtGui.QApplication.translate("FeaturesTabWidget", "Lunar II", None, QtGui.QApplication.UnicodeUTF8))

