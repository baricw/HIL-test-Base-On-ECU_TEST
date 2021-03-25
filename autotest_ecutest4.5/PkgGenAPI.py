# -*- coding: utf-8 -*-
from ApiClient import ApiClient

class PkgGenAPI:
      def __init__(self):
         api=ApiClient()
         
         self.pkgapi=api.PackageApi
         self.testapi=api.PackageApi.TestStepApi
         self.mapapi=api.PackageApi.MappingApi
         self.expectapi=api.PackageApi.ExpectationApi
         self.sigrecapi=api.PackageApi.SignalRecordingApi
         self.varapi=api.PackageApi.VariableApi
         self.traceanayapi=api.PackageApi.TraceAnalysisApi

         self.sigroup =None

      def CreatePackage(self):
            self.pkg=self.pkgapi.CreatePackage()
            
            blk_pre=self.testapi.CreateTsBlock()
            blk_pre.SetActionColumnText(u'pre')
            self.pkg.AppendTestStep(blk_pre)

            blk_action=self.testapi.CreateTsBlock()
            blk_action.SetActionColumnText(u'action')
            self.pkg.AppendTestStep(blk_action)

            blk_pos=self.testapi.CreateTsBlock()
            blk_pos.SetActionColumnText(u'pos')
            self.pkg.AppendTestStep(blk_pos)            

            return blk_pre,blk_action,blk_pos

      def SavePackage(self,filename):
            self.pkg.Save(filename)
            self.pkg.Close()

      def addteststepswrite(self,parent,sysid,mapName,signal_value_str,raster=None):
            """
            sysid: (unicode) – Name of system according to the test configuration,for example:u'Plant model',u'Powertrain'
            parent:pakage block or mutichek which be create
            mapname:model name(unicode),for example:u'Model Root/MDL/DriverInterface/KL30/Value'
            signal_value_str:value(unicode)
            """
            sysid = unicode(sysid)
            signal_value_str=unicode(signal_value_str)
            mapitem=self.mapapi.CreateMappingItem(sysid,mapName)
            if raster != None:
                  mapitem.SetRaster(raster)
            wrt=self.testapi.CreateTsWrite(mapitem)
            wrt.SetValue(signal_value_str)
            parent.AppendTestStep(wrt)

      def addteststepsread(self,parent,sysid,mapName,signal_expect,raster=None):
            sysid = unicode(sysid)
            signal_expect=unicode(signal_expect)
            mapitem=self.mapapi.CreateMappingItem(sysid,mapName)
            if raster != None:
                  mapitem.SetRaster(raster)
            exp=self.expectapi.CreateNumericExpressionExpectation(signal_expect)# signal_expect is unicode
            red=self.testapi.CreateTsRead(mapitem)
            red.SetExpectation(exp)
            parent.AppendTestStep(red)

      def addteststepsread_var(self,parent,sysid,mapName,store_name,raster=None):

            returnvar=self.pkg.GetVariable(store_name)
            if returnvar==None:
                self.addvar(store_name)

            sysid = unicode(sysid)
                
            mapitem=self.mapapi.CreateMappingItem(sysid,mapName)
            if raster != None:
                  mapitem.SetRaster(raster)
            red=self.testapi.CreateTsRead(mapitem)
            parent.AppendTestStep(red)
            red.SetSaveInVariableName(store_name)
            #parent.AppendTestStep(red)

      def addteststepsreadANDvar(self,parent,sysid,mapName,signal_expect,store_name,raster=None):
            
            sysid = unicode(sysid)
            self.addvar(store_name)
            mapitem=self.mapapi.CreateMappingItem(sysid,mapName)
            if raster != None:
                  mapitem.SetRaster(raster)
            exp=self.expectapi.CreateNumericExpressionExpectation(signal_expect)
            red=self.testapi.CreateTsRead(mapitem)
            red.SetExpectation(exp)
            parent.AppendTestStep(red)
            red.SetSaveInVariableName(store_name)
            #parent.AppendTestStep(red)

      def addteststepjob(self,parent,toolId,jobName,savename=None):

            toolId=unicode(toolId)
            jobName=unicode(jobName)
            
            mapitem=self.mapapi.CreateJobMappingItem(toolId,jobName)
            job=self.testapi.CreateTsJob(mapitem)
            parent.AppendTestStep(job)
            if savename!=None:

                  returnvar=self.pkg.GetVariable(savename)
                  if returnvar==None:
                        self.addvar(savename)                  
                        job.SetSaveInVariableName(savename)
                  else:
                        job.SetSaveInVariableName(savename)

      def addvar(self,store_name):
            var=self.varapi.CreateVariable(store_name)
            self.pkg.AddVariable(var)
            var.SetInitialNumericValue(0)
            var.SetReturn(True)
            #var.SetRecorded(True)
            
      def addMutiCheck(self,parent,option,timeout):
            timeout=str(float(timeout)*1000)#timeout is string            
            mutichk=self.testapi.CreateTsMultiCheck()
            
            if option=='until':
                  mutichk.SetTimeOptionWaitUntilTrue(timeout)
            elif option=='still':
                  mutichk.SetTimeOptionTrueForAtLeast(timeout)
            else:
                  pass

            parent.AppendTestStep(mutichk)

            return mutichk

      def addtsblock(self,parent,name):
            name = unicode(name)
            tsblock=self.testapi.CreateTsBlock()
            #tsblock.AddTag(name)
            tsblock.SetActionColumnText(name)
            parent.AppendTestStep(tsblock)

            return tsblock

      def wait(self,parent,timeout):
            timeout=unicode(timeout)
            wait=self.testapi.CreateTsWait()
            wait.SetDelay(timeout,u's')#timeout is unicode
            parent.AppendTestStep(wait)

      def ifthenelse(self,parent,condtion):
            conditon=unicode(condition)
            ifthen=self.testapi.CreateTsIfThenElse()
            ifthen.SetCondition(condtion)
            parent.AppendTestStep(ifthen)
            nodethen=ifthen.GetThenNode()
            nodeelse=ifthen.GetElseNode()

            return nodthen,nodelse

      def loop(self,parent,inputcond,loopcount=u'100'):
            inputcond=unicode(inputcond)
            loopcount = unicode(loopcount)
            loop=self.testapi.CreateTsLoop()
            loop.SetLoopCountExpression(loopcount)
            loop.SetStartCondition(inputcond)
            parent.AppendTestStep(loop)

            return loop

      def addsigroup(self,parent,recname):

            '''
            Add signalgroup for pkg
            This function is used with function 'addsigforec'
            For sinals for recording have model signal and calibration signal ,so I separate the two function
            '''
            
            recname=unicode(recname)
            
            self.sigroup=self.sigrecapi.CreateSignalGroup()
            recd=self.sigrecapi.CreateRecordingGroup(recname)
####            recdinfo=self.sigrecapi.CreateRecordingInfo(path,recordingName=recname)
            recd.EnableAutoStartStop()
            recd.SetName(recname)
            parent.AppendSignalGroup(self.sigroup,allowNewName=True)
            self.sigroup.AppendRecordingGroup(recd)
##            recd.AppendRecordingInfo(recdinfo)
            
            aa=self.sigroup.GetRecordingGroups()
            self.sigroup.RemoveRecordingGroup(aa[0])
            #return sigroup
            
      def addsigforec(self,sysid,mapname):
##            for mapname in maplist:
##            mapname = unicode(mapname)
##            print mapname
##            mapnamelist = self.sigroup.GetMappingItemNames()
##            print mapnamelist
            '''
            This function is used with function 'addsigroup'
            With using 'try...except',for 'mapnamelist = self.sigroup.GetMappingItemNames()' can get mapnamelist but not fullname,
            for example,'Plant model/Model Root/MDL/DriverInterface/AccPedal[%]/Value' has local map name 'DriverInterface/AccPedal[%]/Value'
             not full name
            so using 'try...except' can ignore error '<Fault 1: 'ApiError: Signal already added to the signal group!'>'
            '''
            try:
##            if mapname in mapnamelist:
##                  pass
            #else:
                  mapitem=self.mapapi.CreateMappingItem(sysid,mapname)
                  self.sigroup.AppendMappingItem(mapitem)

            except Exception,e:
                  print Exception,':',e
                  pass

##            return recd

      def addstatrace(self,parent,rec):
            startrac=self.testapi.CreateTsStartTrace()
            parent.AppendTestStep(startrac)
            startrac.SetRecordingGroup(rec)

      def addstoptrace(self,parent,rec):
            stoptrac=testapi.CreateTsStopTrace()
            parent.AppendTestStep(stoptrac)
            stoptrac.SetRecordingGroup(rec)

      def initinca(self,parent):
            self.wait(parent,'5')
            self.addvar('result')
            reloop=self.loop(parent,'result==False',loopcount=u'3')
            self.addteststepjob(reloop,'INCA01','InitializeHardware',savename='result')
            self.wait(reloop,'10')
            
            self.addteststepjob(parent,'INCA01','StopMeasurement')
            self.wait(parent,'5')

            self.addteststepjob(parent,'INCA01','Start')
            self.wait(parent,'5')
            
            
            
            

##      def addtraceanalysis(self,parent,mapName):#no mapname ,cannot use
##            trace=self.traceanayapi.CreateTraceAnalysis(u'trace')
##            self.pkg.AppendTraceAnalysis(trace)
####            trace.SetEnabled(True)
##            episode=self.traceanayapi.CreateEpisode(u'episode')
##            trace.AppendTraceStep(episode)
##            
####            trace.AppendTraceStep(a[0])
##            TemlateTrace=self.traceanayapi.CreateTemplateBasedTraceStep(u'CheckPwmSignal')
##            TemlateTrace.SetTemplateById(u'CheckPwmSignal')
##            episode.AppendTraceStep(TemlateTrace)
####            TemlateTrace.SetTemplate
####            
##            
####            GenericSignal=self.traceanayapi.CreateGenericSignal(u'signal1')
######            
####            trace.AppendGenericSignal(GenericSignal)
##            recd=self.addsigrec(parent,'a',[mapName])
########            
######            GenericSignal.AssignRecordingSignal(recd,mapName)

            
            
            
            
            
            

if __name__=='__main__':
      pakg=PkgGenAPI()
      pre,action,pos=pakg.CreatePackage()
      mapname=u'Can_BCM_LDoorWindowStateDlc_C'
 #     pakg.addteststepsread(pre,u'Powertrain',mapname,u'value==1')
      pakg.initin(pre)
##      mapName=u'Model Root/MDL/DriverInterface/KL30/Value'
##      mapname1=u'Model Root/MDL/DriverInterface/CTRL/Value'
##      mapname2=u'Model Root/MDL/DriverInterface/AccPedal[%]/Value'
      ##toolId='INCA01'
      ##jobName='InitializeHardware'
      ##storename='result'
      
      ##pakg.addteststepjob(pre,toolId,jobName,savename=storename)
      #pakg.addteststepsreadANDvar(pre,mapName,'value==1','s0','Periodic Task 1')
      #parent=pakg.pkg
      #pakg.addtraceanalysis(parent,mapName)
      
      
      #pakg.addteststepswrite(pre,mapName,u'1')
      
      #pakg.addteststepswrite(action,mapName,u'1')
      #mutick=pakg.addMutiCheck(action,None,'1')
##      pakg.addteststepsread(mutick,mapname1,u'value==1')
##      pakg.addteststepsread(mutick,mapname2,u'value==1')
##      pakg.addteststepsread_var(action,mapname2,'s0')
##      loop=pakg.loop(action,u's0==0')
##      
##      pakg.wait(loop,u'1')
##      pakg.addteststepswrite(action,mapname2,u's0')
##      
##      pakg.addteststepswrite(pos,mapName,u'1')

      
      
      pakg.SavePackage('E:\\temp\\bb.pkg')
