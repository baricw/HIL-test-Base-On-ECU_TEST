# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *


from PyQt4.QtCore import (Qt, QString,QTimer,QReadWriteLock,QDir)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
from PyQt4.QtGui import (QApplication, QMainWindow,QDialog,QFileDialog,QTextCursor)
import ui_MainCreate,ui_NewCreate,ui_Progress,ui_Error,ui_Complete,ui_Matrix

import os,sys

import acthread
import dbthread

##from PakgCreate import *
##from case_teststep_check_read import *
##from map_read import *
##from dbc_read import *
##from check_rw import *
##
###import decimal
##from PkgGenAPI import *


class MainCreate(QMainWindow,
           ui_MainCreate.Ui_MainCreateMw):

      def __init__(self,parent=None):
            super(MainCreate,self).__init__(parent)

            self.__diaexec = False
            self.__startflg = False
            self.__stopflg = False

            self.listmessagebox=[]
            self.error=False
            self.progressvalue=[]

            self.timer=QTimer(self)
            self.timer.timeout.connect(self.showtime)

            self.thread=acthread.ACThread()
            

            self.thread.finished.connect(self.finished)
            #self.thread1.result.connect(self.hsresult)

            self.thread.stoped.connect(self.stoped)
                      
            self.setupUi(self)

      @Slot()
      def on_ActNewOpen_triggered(self):
            self.createdlg=NewCreate(parent=self)
            self.createdlg.show()
            self.__diaexec=self.createdlg.exec_()
            if self.__diaexec:
                  self.casedir = self.createdlg.casedir
                  self.lineEditTSPath.setText(self.casedir)
                  #print self.lineEditTSPath.text()

                  self.a2ldir = self.createdlg.a2ldir
                  self.lineEdita2lPath.setText(self.a2ldir)

                  self.modelmapdir = self.createdlg.modelmapdir
                  self.lineEditModelmap.setText(self.modelmapdir)

                  self.usermapdir = self.createdlg.usermapdir
                  self.lineEditUsermap.setText(self.usermapdir)

                  self.HILName = self.createdlg.HILtype
                 
                  self.lineEditHILType.setText(self.HILName)
                  self.lineEditCreatetype.setText("New Create Type")
      @Slot()            
      def on_ActCreateDB_triggered(self):
      	    self.createdb=Matrix(parent=self)
      	    self.createdb.show()                           
                  
      @Slot()
      def on_pushButtonStart_clicked(self):

            self.pushButtonStart.setEnabled(False)
                        
            if self.__diaexec:
                  #self.textBrowser.append("aaa")
                                    
                  self.timer.start(1)
                  self.thread.initialize(self.casedir,self.usermapdir,self.a2ldir,self.HILName,self.modelmapdir,\
                  self.listmessagebox,self.progressvalue,self.error)
                  self.thread.start()

                  self.diaprogress = progress(parent=None)
                  self.diaprogress.show()
                  
                  
            #self.textBrowser.append("aaa")
            
            
      @Slot()
      def on_pushButtonStop_clicked(self):

            self.pushButtonStart.setEnabled(True)
            
            if self.__diaexec:
                  self.timer.stop()
                  self.thread.wait()
                 

                  self.listmessagebox=[]
                  self.error=False
                  self.progressvalue=[]

                  self.__diaexec = False
            #self.textBrowser.append("bbb")
##            self.diacomplete = complete(parent=None)
##            self.diacomplete.show()

      @Slot()
      def on_pushButtonClear_clicked(self):
            self.textBrowser.clear()
            
            self.lineEditTSPath.setText("")
            self.lineEdita2lPath.setText("")                 
            self.lineEditModelmap.setText("")                  
            self.lineEditUsermap.setText("")          
            self.lineEditHILType.setText("")
            self.lineEditCreatetype.setText("")
            

      def showtime(self):

            self.textBrowser.clear()
            if len(self.progressvalue) > 0:
                  pre=self.progressvalue[len(self.progressvalue)-1]
                  self.diaprogress.progressBar.setValue(int(pre))
##                  if int(pre) >= 100:
##                        self.diaprogress.accept()
                        
            
            
            #self.textBrowser.append(QString(self.progressvalue))

            for prt in self.listmessagebox:
                  self.textBrowser.append(prt)

##            if self.error:
##                  digerror = error(parent=None)
##
##                  diaerror.show()
##
##                  self.timer.stop()
##                  self.thread.wait()
                  

      def finished(self, completed):

            self.timer.stop()

            self.diaprogress.progressBar.setValue(100)
            self.diaprogress.accept()

            self.textBrowser.append("All packages are complete !!!")
            
            self.diacomplete = complete(parent=None)
            self.diacomplete.show()
            self.thread.wait()

            self.listmessagebox=[]
            self.progressvalue=[]

            self.pushButtonStart.setEnabled(True)
      def stoped(self):
            self.timer.stop()

            self.textBrowser.append("There is some error!")
            
            self.thread.wait()
            self.diaprogress.accept()
            self.diaerror = error(parent=None)
            self.diaerror.show()
            

                  
            
class NewCreate(QDialog,
        ui_NewCreate.Ui_NewCreateDlg):
      def __init__(self,parent=None):
            super(NewCreate,self).__init__(parent)
            self.casedir=''
            self.a2ldir=''
            self.modelmapdir=''
            self.usermapdir=''
            self.HILtype=''

            self.setModal(True)#True为模态对话框，False为非模态对话框
            
            self.setupUi(self)
      @Slot()
      def on_pushButtoncase_clicked(self):
            
            casedir=QFileDialog.getExistingDirectory(self,"Select case",QString(os.getcwd()),QFileDialog.DontResolveSymlinks)
            #self.casedir=QDir.toNativeSeparators(casedir)
            self.casedir=QDir.convertSeparators(casedir)
            
            #print type(self.casedir[0])
            self.lineEditcase.setText(self.casedir)

      @Slot()
      def on_pushButtona2l_clicked(self):
            
            a2ldir=QFileDialog.getOpenFileName(self,"Select a2l",QString(os.getcwd()),"*.a2l")
            #self.casedir=QDir.toNativeSeparators(casedir)
            self.a2ldir=QDir.convertSeparators(a2ldir)
            
            #print type(self.casedir[0])
            self.lineEdita2l.setText(self.a2ldir)
     
      @Slot()
      def on_pushButtonmodelmap_clicked(self):
            
            modelmapdir=QFileDialog.getOpenFileName(self,"Select modelmap",QString(os.getcwd()),"*.txt")
            self.modelmapdir=QDir.convertSeparators(modelmapdir)
            self.lineEditmodelmap.setText(self.modelmapdir)
      @Slot()            
      def on_pushButtonusermap_clicked(self):
            
            usermapdir=QFileDialog.getOpenFileName(self,"Select usermap",QString(os.getcwd()),"*.xls")
            self.usermapdir=QDir.convertSeparators(usermapdir)
            self.lineEditusermap.setText(self.usermapdir)
      @Slot()            
      def on_pushButtonOK_clicked(self):
            self.HILtype=self.comboBoxHIL.currentText()
            QDialog.accept(self)

class Matrix(QDialog,
        ui_Matrix.Ui_MatrixDlg):
      def __init__(self,parent=None):
            super(Matrix,self).__init__(parent)
            
            self.DBCdir=''
            self.setModal(True)#True为模态对话框，False为非模态对话框

            self.listmessageboxfile=[]
            self.listmessageboxinsert=[]

            self.timer1=QTimer(self)
            self.timer1.timeout.connect(self.showtime1)

            self.thread1 = dbthread.DBThread()
            self.thread1.result.connect(self.hsresult)
            
            
            self.setupUi(self)
      @Slot()
      def on_pushButtonDBC_clicked(self):
            
            DBCdir=QFileDialog.getExistingDirectory(self,"Select DBC",QString(os.getcwd()),QFileDialog.DontResolveSymlinks)
            self.DBCdir=QDir.convertSeparators(DBCdir)
            #print type(self.DBCdir)
            self.lineEditDBC.setText(self.DBCdir)

      @Slot()
      def on_pushButtonGen_clicked(self):
            self.pushButtonGen.setEnabled(False)
            self.thread1.initialize(self.DBCdir,self.listmessageboxfile,self.listmessageboxinsert)
            self.timer1.start(1)
            self.thread1.start()
            

      def hsresult(self):
            self.thread1.wait()
            self.timer1.stop()
            self.pushButtonGen.setEnabled(True)           	
            
      def showtime1(self):

            self.textBrowserfile.clear()
            self.textBrowserinsert.clear()
            
            if len(self.listmessageboxfile):
                  for prt in self.listmessageboxfile:
                        self.textBrowserfile.append(prt)

            if len(self.listmessageboxinsert):

                  for prt in self.listmessageboxinsert:
                        self.textBrowserinsert.append(prt)  
            
##            self.textBrowserfile.append(self.listmessageboxfile[0])
##            self.textBrowserinsert.append(self.listmessageboxinsert[0])     
            

class progress(QDialog,
               ui_Progress.Ui_ProgressDlg):
      def __init__(self,parent=None):
            super(progress,self).__init__(parent)
            #self.progressBar.setRange(0,100)
            
            #self.setModal(True)#True为模态对话框，False为非模态对话框
            self.setupUi(self)


class error(QDialog,
               ui_Error.Ui_ErrorDgl):
      def __init__(self,parent=None):
            super(error,self).__init__(parent)
            self.setModal(True)
            self.setupUi(self)

class complete(QDialog,
               ui_Complete.Ui_CompleteDgl):
      def __init__(self,parent=None):
            super(complete,self).__init__(parent)

            self.setModal(True)

            self.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form=MainCreate()
    form.show()
    app.exec_()
