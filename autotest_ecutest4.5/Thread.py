# -*- coding: utf-8 -*-

from PyQt4.QtCore import (Qt, QString,QThread,QMutex)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
import time
import demo

class pkgThread(QThread):
      finished = Signal(bool)
      

      def __init__(self,parent=None):
            super(pkgThread,self).__init__(parent)
            #self.lock=lock
            
            self.stopped=False
            self.completed=False

      def initialize(self,prtlist):
            self.prtlist=prtlist 

      def run(self):
            demo.prt(self.prtlist)

            self.stop()
            self.finished.emit(self.completed)


      def stop(self):

            self.stopped = True
##            try:
##                  #self.mutex.lock()
##                  self.stopped = True
##            finally:
##                  self.mutex.unlock()
