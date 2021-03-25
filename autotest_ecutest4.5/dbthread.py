# -*- coding: utf-8 -*-

from PyQt4.QtCore import (Qt, QString,QThread,QMutex)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
import time,os

from matrixrd import *

class DBThread(QThread):
      result = Signal(bool)
      def __init__(self,parent=None):
            super(DBThread,self).__init__(parent)
            
            self.dbcpath=None

      def initialize(self,dbcpath,listmessageboxfile,listmessageboxinsert):           
            self.dbcpath=dbcpath
            self.listmessageboxfile = listmessageboxfile
            self.listmessageboxinsert = listmessageboxinsert

      def run(self):         
            
            reflag=self.DBCreate(self.dbcpath)

            if reflag == True:
                  self.wait()
                  self.listmessageboxfile.append('All Database haved be created')
            else:
                  self.wait()
                  self.listmessageboxfile.append('It generate error when creating Database')

            self.result.emit(True)
            

      def DBCreate(self,dbcpath):
            

            list_fdbcname=[]

            for root, dirs, files in os.walk(str(dbcpath)):
                  
                  for name in [name for name in files
                               if name.endswith((".dbc", ".ldf"))]:
                        fname = os.path.join(root, name)
                        list_fdbcname.append(fname)

            can_info=MatrixInfo()
            candbc=can_info.CanMatrixDb(list_fdbcname,self.listmessageboxfile,self.listmessageboxinsert)
            
            return candbc
      
            
