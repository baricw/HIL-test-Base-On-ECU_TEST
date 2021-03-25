# -*- coding: utf-8 -*-

from PyQt4.QtCore import (Qt, QString,QThread,QMutex)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
import time,os

from case_teststep_check_read import *
from matrixrd import *
from check_rw import *
from PakgCreate import *



class ACThread(QThread):

      finished = Signal(bool)
      stoped = Signal(bool)
      
      def __init__(self,parent=None):
            super(ACThread,self).__init__(parent)

            self.error = False
            self.completed = False
            self.stopped = False

            self.casepath=None
            #self.a2lpath=None
      def initialize(self,casepath,usermapdir,a2ldir,HILname,modelmapdir,listmessagebox,progressvalue,flgerror):
            self.casepath=casepath
            self.a2ldir=a2ldir
            self.modelmapdir=modelmapdir
            self.usermapdir=usermapdir
            self.HILname=HILname
            #print str(self.HILname)
            
            self.listmessagebox = listmessagebox
            self.progressvalue = progressvalue
            self.flgerror=flgerror

      def stop(self):
           
            self.stopped=True
            #self.wait()

      def isStopped(self):
            
            return self.stopped

      def run(self):
            
            #print 'bbbb'
            reflag=self.ACCreate(self.casepath)
            #print 'cccc'
            if reflag == True:
                  self.wait()
                  self.finished.emit(self.completed)
            else:
                 self.wait() 


      def ACCreate(self,casepath):
            try:
                  list_fcasename=[]
                  list_casename=[]
                  #list_fa2lname=[]
                  #print casepath
                  for root, dirs, files in os.walk(str(casepath)):
                        if self.isStopped():
                              return False
                        for name in [name for name in files
                                     if name.endswith((".xls", ".xlsx")) and not name.startswith("~$")]:
                              fname = os.path.join(root, name)
                              list_casename.append(name)
                              list_fcasename.append(fname)

                  if len(list_fcasename) == 0:
                        print 'Please check your testcase path......'
                        self.listmessagebox.append('Please check your testcase path......')
                        self.stoped.emit(True)
                        return False
                  #print  list_fcasename     
                              
                  if self.isStopped():
                        return

                  testcase=test_case_prepare()
                  case_dict=testcase.testcase_rd_wt(list_fcasename,list_casename,self.listmessagebox,self.flgerror)
                  if case_dict == None:
                        self.stoped.emit(True)
                        return False 

##                  can_info=MatrixInfo()
##                  candbc=can_info.CanMatrixDb(list_fdbcname,self.listmessagebox)
##
##                  if candbc == False:
##                        self.stoped.emit(True)
##                        return False
                        

                  check=Check_rw()
                  case_dict_f=check.check_map(case_dict,str(self.HILname).strip(),str(self.usermapdir),str(self.modelmapdir),
                                              str(self.a2ldir),self.listmessagebox,self.flgerror)

                  if case_dict_f == None:
                        self.stoped.emit(True)
                        return False

                  pkgcreat=PkgCreate()
                  reflag=pkgcreat.PakgCreate(str(casepath),case_dict_f,str(self.HILname).strip(),self.progressvalue,self.listmessagebox,self.flgerror)
                  #print self.progressvalue

                  if reflag == True:
                        self.completed = True
                  else:
                        self.stoped.emit(True)
                        return False
            except:
                  return False

            return True
