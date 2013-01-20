# -*- coding: utf8 -*-
'''
Created on 2013-1-12

@author: Administrator
'''

import sys
from PyQt4 import QtCore, QtGui
from main.logic import videoscan

def populateTableWidget(tableWidget):
    
    row = 0
    videoData = videoscan.getVideoInfo(tableWidget.rowCount())
    for info in videoData:
        item0 = QtGui.QTableWidgetItem(info.filename.decode('gbk'))
        item1 = QtGui.QTableWidgetItem(str(info.size))
        item2 = QtGui.QTableWidgetItem(info.mtime_str)
        item3 = QtGui.QTableWidgetItem() 
        
        tableWidget.setItem(row, 0, item0)
        tableWidget.setItem(row, 1, item1)
        tableWidget.setItem(row, 2, item2)
        tableWidget.setItem(row, 3, item3)
        row+=1
                
def Launch():
    app = QtGui.QApplication(sys.argv)

    num_item = 10
    tableWidget = QtGui.QTableWidget(num_item, 4)
    
    #tableWidget.setItemDelegate(StarDelegate())
    tableWidget.setEditTriggers(
            QtGui.QAbstractItemView.DoubleClicked |
            QtGui.QAbstractItemView.SelectedClicked)
    tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

    headerLabels = ("Name", "Size", "Date", "Rating")
    tableWidget.setHorizontalHeaderLabels(headerLabels)

    populateTableWidget(tableWidget)

    tableWidget.resizeColumnsToContents()
    tableWidget.resize(1024, 768)
    tableWidget.show()

    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    Launch()
    

    
