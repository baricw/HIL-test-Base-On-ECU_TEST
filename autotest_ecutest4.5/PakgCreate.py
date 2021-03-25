# -*- coding: utf-8 -*-
import decimal
from PkgGenAPI import *
import sys


class PkgCreate:
    def __init__(self):
##        self.constant_name=('KL30','Key','Key_ST','Gear','BrkPedal','AccPedal','DriveMode','VehMode','Chrg','Initial_SOC','PT_Bus','Chassis_Bus','Hybrid_Bus','AC_PowerReq','RemoteControl')
        self.pkg=PkgGenAPI()
        self.list_case_recorder=[]
##    def PakgCreate(self,filepath,case_name_array_xls,case_test_array_xls,check_array_xls,case_pretest_array_xls,case_postest_array_xls,case_trace_array_xls):
    def PakgCreate(self,filepath,case_dict,HILname,precent_str,listmessagebox,flgerror,):
        #ErroNum=0
        
        pkg=self.pkg
        decimal.getcontext().prec=4
        percent_case=decimal.Decimal(0)
        precent_progress=decimal.Decimal(0)
        print 'Start Create Packages.....'
        listmessagebox.append('Start Create Packages.....')

        list_casedict_key=list(case_dict.keys())
        percent_factor=decimal.Decimal(1)/decimal.Decimal(len(list_casedict_key))
        #print 'percent_factor='+str(percent_factor)
        for filenum in range(len(list_casedict_key)):
            
            case_list=case_dict[list_casedict_key[filenum]]
            


            case_name_array=case_list[0]
            
            case_predata_array=case_list[1]
            case_prechk_array=case_list[2]
            case_pretime_array=case_list[3]
            case_prelogic_array=case_list[4]

            case_actdata_array=case_list[5]
            case_actchk_array=case_list[6]
            case_acttime_array=case_list[7]
            case_actlogic_array=case_list[8]

            case_posdata_array=case_list[9]
            case_poschk_array=case_list[10]
            case_postime_array=case_list[11]
            case_poslogic_array=case_list[12]

            


##            percent_sheet=decimal.Decimal(sheetnum+1)/decimal.Decimal(len(case_name_array_sheet))
            percent_case=decimal.Decimal(1)/decimal.Decimal(len(case_name_array))
            
            for case_test_num_loopnum in range(len(case_name_array)):                
                
                precent_progress=(percent_case*percent_factor)*100+precent_progress
                print '.'+str(int(precent_progress))+'%',
                precent_str.append(str(int(precent_progress)))
                listmessagebox.append(str(int(precent_progress))+'%')

                case_name=case_name_array[case_test_num_loopnum][0]
                flag_casetype = case_name_array[case_test_num_loopnum][1]
                case_name=case_name.strip("u''")
##                case_check_dict=check_array[case_test_num_loopnum]
                self.list_case_recorder=[]
                
                if case_name!='':
                    try:
            #######create parent package
                        preparent,acparent,postparent=pkg.CreatePackage()
            ########add signal group
                        pkg.addsigroup(self.pkg.pkg,case_name)


            ########create precondition
                        case_predata_step_list=case_predata_array[case_test_num_loopnum][1]
                        case_prechk_step_list=case_prechk_array[case_test_num_loopnum][1]
                        presignal_list=case_predata_array[case_test_num_loopnum][0]
                        presigchk_list=case_prechk_array[case_test_num_loopnum][0]
                        pretstime_list=case_pretime_array[case_test_num_loopnum][0]
                        pretslogic_list=case_prelogic_array[case_test_num_loopnum][0]

                        flag_block = self.creatblock(pkg,preparent,case_predata_step_list,case_prechk_step_list,presignal_list,presigchk_list,\
                                        pretstime_list,pretslogic_list,HILname,listmessagebox)
                        if flag_block== False:
                            return False

            ########add inca initialization after precondition if need
                        if flag_casetype == 1:
                            incablock=pkg.addtsblock(preparent,'IncaInit')
                            pkg.initinca(incablock)

                        
            ########create action

                        case_actdata_step_list=case_actdata_array[case_test_num_loopnum][1]
                        case_actchk_step_list=case_actchk_array[case_test_num_loopnum][1]
                        actsignal_list=case_actdata_array[case_test_num_loopnum][0]
                        actsigchk_list=case_actchk_array[case_test_num_loopnum][0]
                        acttstime_list=case_acttime_array[case_test_num_loopnum][0]
                        acttslogic_list=case_actlogic_array[case_test_num_loopnum][0]

                        flag_block=self.creatblock(pkg,acparent,case_actdata_step_list,case_actchk_step_list,actsignal_list,actsigchk_list,\
                                        acttstime_list,acttslogic_list,HILname,listmessagebox)
                        if flag_block== False:
                            return False
            ########create poscondition
                        case_posdata_step_list=case_posdata_array[case_test_num_loopnum][1]
                        case_poschk_step_list=case_poschk_array[case_test_num_loopnum][1]
                        possignal_list=case_posdata_array[case_test_num_loopnum][0]
                        possigchk_list=case_poschk_array[case_test_num_loopnum][0]
                        poststime_list=case_postime_array[case_test_num_loopnum][0]
                        postslogic_list=case_poslogic_array[case_test_num_loopnum][0]

                        flag_block=self.creatblock(pkg,postparent,case_posdata_step_list,case_poschk_step_list,possignal_list,possigchk_list,\
                                        poststime_list,postslogic_list,HILname,listmessagebox)
                        if flag_block== False:
                            return False
           #####recorder
                        for recordlist in self.list_case_recorder:
                            sysid = recordlist[1]
                            signal_rec = recordlist[0]
                            pkg.addsigforec(sysid,signal_rec)
                            
####                        path=filepath+'\\'+list_casedict_key[filenum]+'\\Data'
##                        pkg.addsigrec(self.pkg.pkg,case_name,self.list_case_recorder)
                        

           #############save package
                        pkg.SavePackage(filepath+'\\'+list_casedict_key[filenum]+'\\'+case_name+'.pkg')             
                        
                        
                    except:
                        s=sys.exc_info()
                        print "\Error '%s' happend on line %d"%(s[1],s[2].tb_lineno)
                        print '\nThere is some wrong in case %s when it creat package'%(case_name)
                        messagebox='There is some wrong in case '+str(case_name)+' when it creat package'
                        listmessagebox.append(messagebox)
                    
                        flgerror=True
                        return False 
                        #ErroNum+=1
                        
                else:
                    continue

        return True

                        

        #return ErroNum             
                         

    def creatblock(self,pkg,parent,case_predata_step_list,case_prechk_step_list,
                   signal_list,sigchk_list,pretstime_list,pretslogic_list,HILname,listmessagebox):

        if HILname=='ETAS':
            
            raster='TaskDVEModel'
        elif HILname=='DSPACE':
            raster='Periodic Task 1'
        else:
            print 'Please check HIL type...'
            listmessagebox.append('Please check HIL type...')
            
        #bparent=parent
        flag_logic = False
        
        for step_num in range(len(case_predata_step_list)):
            

            stepname='step'+str(step_num+1)
            tstime=pretstime_list[step_num]
            tslogic=pretslogic_list[step_num]

            #if tslogic=='':
            if tslogic=='' and flag_logic==False:
                bparent=pkg.addtsblock(parent,stepname)            
                flag_step = self.step(pkg,bparent,case_predata_step_list,case_prechk_step_list,signal_list,sigchk_list,tstime,tslogic,raster,
                          step_num,listmessagebox)

                if flag_step == False:
                    return False
                

            else:
                if tslogic.find('loop')==0 and flag_logic==False:
                    flag_logic = True
                    kqpos=tslogic.find('(')
                    khpos=tslogic.find(')')

                    condition=tslogic[kqpos+1:khpos]
                    lparent=pkg.loop(parent,condition)
                    bparent = pkg.addtsblock(lparent,stepname)
                    #bparent=pkg.loop(bparent,condition)

                    flag_step = self.step(pkg,bparent,case_predata_step_list,case_prechk_step_list,signal_list,sigchk_list,
                                          tstime,tslogic,raster,step_num,listmessagebox)
                    if flag_step == False:
                        return False
                elif tslogic.find('end')==0 and flag_logic==True:
                    flag_logic = False
                    bparent = pkg.addtsblock(lparent,stepname)
                    flag_step = self.step(pkg,bparent,case_predata_step_list,case_prechk_step_list,signal_list,sigchk_list,
                                          tstime,tslogic,raster,step_num,listmessagebox)
                    if flag_step == False:
                        return False
                    bparent=parent
                elif flag_logic==True:
                    bparent = pkg.addtsblock(lparent,stepname)
                    flag_step = self.step(pkg,bparent,case_predata_step_list,case_prechk_step_list,signal_list,sigchk_list,
                                          tstime,tslogic,raster,step_num,listmessagebox)
                    if flag_step == False:
                        return False

                else:
                    print 'loop....end has used not incorrectly...'
                    listmessagebox.append('loop....end has used not incorrectly...')
                    return False
        return True
                    


    def step(self,pkg,parent,case_predata_step_list,case_prechk_step_list,signal_list,sigchk_list,
             tstime,tslogic,raster,step_num,listmessagebox):
        
        flag_addmutichk=0
        sysid_model = u'Plant model'
        sysid_cal = u'Powertrain'
        raster_cal = u'5ms time synchronous'
        if len(case_predata_step_list)>0:
                
            #signal_list=case_predata_array[case_test_num_loopnum][0]
            value_list=case_predata_step_list[step_num]
            
            
            #tslogic=case_prelogic_array[case_test_num_loopnum][0][step_num]               

            for signal_num in range(len(signal_list)):
                value_temp=value_list[signal_num]

                if value_temp=='':
                     pass
                elif value_temp=='sw':                            
                    signal_temp_list=signal_list[signal_num]
                    if len(signal_temp_list)==2:
                        signal_temp=signal_temp_list[0]
                        signal_temp_sw=signal_temp_list[1]
                        pkg.addteststepswrite(parent,sysid_model,signal_temp_sw,'0',raster)
                        pkg.addteststepswrite(parent,sysid_model,signal_temp,'0',raster)

##                        pkg.addsigforec(sysid_model,signal_temp)
##                        pkg.addsigforec(sysid_model,signal_temp_sw)
                        self.appendlist([signal_temp,sysid_model],self.list_case_recorder)
                        self.appendlist([signal_temp_sw,sysid_model],self.list_case_recorder)
                else:
                    signal_temp_list=signal_list[signal_num]
                    if len(signal_temp_list)==2:
                        if signal_temp_list[1] == 'Calibration':
                            signal_temp=signal_temp_list[0]
                            pkg.addteststepswrite(parent,sysid_cal,signal_temp,value_temp)

##                            pkg.addsigforec(sysid_cal,signal_temp)
                            self.appendlist([signal_temp,sysid_cal],self.list_case_recorder)
##                        elif signal_temp_list[1] == 'Measurement':
##                            signal_temp=signal_temp_list[0]
##                            pkg.addteststepswrite(parent,sysid_cal,signal_temp,value_temp,raster_cal)
##                            self.appendlist(signal_temp,self.list_case_recorder)

                        else:                       
                            signal_temp=signal_temp_list[0]
                            #print signal_temp
                            signal_temp_sw=signal_temp_list[1]
                            pkg.addteststepswrite(parent,sysid_model,signal_temp,value_temp,raster)
                            pkg.addteststepswrite(parent,sysid_model,signal_temp_sw,'1',raster)

##                            pkg.addsigforec(sysid_model,signal_temp)
##                            pkg.addsigforec(sysid_model,signal_temp_sw)
                            self.appendlist([signal_temp,sysid_model],self.list_case_recorder)
                            self.appendlist([signal_temp_sw,sysid_model],self.list_case_recorder)
                    elif len(signal_temp_list)==1:
                        signal_temp=signal_temp_list[0]
                        pkg.addteststepswrite(parent,sysid_model,signal_temp,value_temp,raster)

##                        pkg.addsigforec(sysid_model,signal_temp)
                        self.appendlist([signal_temp,sysid_model],self.list_case_recorder)
                        
                    else:
                        print 'Please Check check_rw,contact lyh'
                        listmessagebox.append('Please Check check_rw,contact lyh')
                        return False
        if len(case_prechk_step_list)>0:
            #sigchk_list=case_prechk_array[case_test_num_loopnum][0]                        
            valchk_list=case_prechk_step_list[step_num]

            if tstime.find('s')==0:
                timeout=tstime[1:]
                tschk=pkg.addMutiCheck(parent,'still',timeout)

                for sigchk_num in range(len(sigchk_list)):
                    valchk_temp=valchk_list[sigchk_num]
                    
                    if valchk_temp=='':
                        pass
                    elif valchk_temp.find('s')==0:
                        
                        sigchk_temp_list=sigchk_list[sigchk_num]
                        if len(sigchk_temp_list) == 2:
                            if sigchk_temp_list[1] == 'Calibration':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread_var(tschk,sysid_cal,sigchk_temp,valchk_temp)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            elif sigchk_temp_list[1] == 'Measurement':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread_var(tschk,sysid_cal,sigchk_temp,valchk_temp,raster_cal)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            else:
                                print 'Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh'
                                listmessagebox.append('Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh')
                                return False

                        elif len(sigchk_temp_list) == 1:                            
                        
                            sigchk_temp=sigchk_temp_list[0]
                            pkg.addteststepsread_var(tschk,sysid_model,sigchk_temp,valchk_temp,raster)

##                            pkg.addsigforec(sysid_model,sigchk_temp)
                            self.appendlist([sigchk_temp,sysid_model],self.list_case_recorder)
                        else:
                            print 'Please Check check_rw,contact lyh'
                            listmessagebox.append('Please Check check_rw,contact lyh')
                            return False
                        
                    else:
                        #tschk=pkg.addMutiCheck(parent,'still',timeout)
                        sigchk_temp_list=sigchk_list[sigchk_num]

                        if len(sigchk_temp_list) == 2:
                            if sigchk_temp_list[1] == 'Calibration':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread(tschk,sysid_cal,sigchk_temp,valchk_temp)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            elif sigchk_temp_list[1] == 'Measurement':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread(tschk,sysid_cal,sigchk_temp,valchk_temp,raster_cal)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            else:
                                print 'Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh'
                                listmessagebox.append('Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh')
                                return False

                        elif len(sigchk_temp_list) == 1:                            
                        
                            sigchk_temp=sigchk_temp_list[0]
                            pkg.addteststepsread(tschk,sysid_model,sigchk_temp,valchk_temp,raster)

##                            pkg.addsigforec(sysid_model,sigchk_temp)
                            self.appendlist([sigchk_temp,sysid_model],self.list_case_recorder)
                        else:
                            print 'Please Check check_rw,contact lyh'
                            listmessagebox.append('Please Check check_rw,contact lyh')
                            return False

                        
##                        sigchk_temp=sigchk_temp_list[0]
##                        pkg.addteststepsread(tschk,sigchk_temp,valchk_temp,raster)
##                        self.appendlist(sigchk_temp,self.list_case_recorder)
            
            elif tstime.find('u')==0:
                timeout=tstime[1:]
                tschk=pkg.addMutiCheck(parent,'until',timeout)

                for sigchk_num in range(len(sigchk_list)):
                    valchk_temp=valchk_list[sigchk_num]
                    if valchk_temp=='':
                        pass
                    elif valchk_temp.find('s')==0:
                        sigchk_temp_list=sigchk_list[sigchk_num]
                        if len(sigchk_temp_list) == 2:
                            if sigchk_temp_list[1] == 'Calibration':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread_var(tschk,sysid_cal,sigchk_temp,valchk_temp)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            elif sigchk_temp_list[1] == 'Measurement':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread_var(tschk,sysid_cal,sigchk_temp,valchk_temp,raster_cal)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            else:
                                print 'Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh'
                                listmessagebox.append('Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh')
                                return False

                        elif len(sigchk_temp_list) == 1:                            
                        
                            sigchk_temp=sigchk_temp_list[0]
                            pkg.addteststepsread_var(tschk,sysid_model,sigchk_temp,valchk_temp,raster)

##                            pkg.addsigforec(sysid_model,sigchk_temp)
                            self.appendlist([sigchk_temp,sysid_model],self.list_case_recorder)
                        else:
                            print 'Please Check check_rw,contact lyh'
                            listmessagebox.append('Please Check check_rw,contact lyh')
                            return False
                        
                        
##                        sigchk_temp_list=sigchk_list[sigchk_num]
##                        sigchk_temp=sigchk_temp_list[0]
##                        pkg.addteststepsread_var(tschk,sigchk_temp,valchk_temp,raster)
##
##                        self.appendlist(sigchk_temp,self.list_case_recorder)
                        
                    else:
                        #tschk=pkg.addMutiCheck(parent,'until',timeout)
                        sigchk_temp_list=sigchk_list[sigchk_num]

                        if len(sigchk_temp_list) == 2:
                            if sigchk_temp_list[1] == 'Calibration':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread(tschk,sysid_cal,sigchk_temp,valchk_temp)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            elif sigchk_temp_list[1] == 'Measurement':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread(tschk,sysid_cal,sigchk_temp,valchk_temp,raster_cal)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            else:
                                print 'Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh'
                                listmessagebox.append('Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh')
                                return False

                        elif len(sigchk_temp_list) == 1:                            
                        
                            sigchk_temp=sigchk_temp_list[0]
                            pkg.addteststepsread(tschk,sysid_model,sigchk_temp,valchk_temp,raster)

##                            pkg.addsigforec(sysid_model,sigchk_temp)
                            self.appendlist([sigchk_temp,sysid_model],self.list_case_recorder)
                        else:
                            print 'Please Check check_rw,contact lyh'
                            listmessagebox.append('Please Check check_rw,contact lyh')
                            return False                        
##                        sigchk_temp=sigchk_temp_list[0]
##                        pkg.addteststepsread(tschk,sigchk_temp,valchk_temp,raster)
##
##                        self.appendlist(sigchk_temp,self.list_case_recorder)
            else:
                timeout=tstime
                if timeout!='0.0':
                    pkg.wait(parent,timeout)                             

                for sigchk_num in range(len(sigchk_list)):
                    valchk_temp=valchk_list[sigchk_num]
                    if valchk_temp=='':
                        pass
                    elif valchk_temp.find('s')==0:
                        if flag_addmutichk == 0:
                            tschk=pkg.addMutiCheck(parent,None,timeout)
                            flag_addmutichk = 1
                        sigchk_temp_list=sigchk_list[sigchk_num]

                        if len(sigchk_temp_list) == 2:
                            if sigchk_temp_list[1] == 'Calibration':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread_var(tschk,sysid_cal,sigchk_temp,valchk_temp)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            elif sigchk_temp_list[1] == 'Measurement':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread_var(tschk,sysid_cal,sigchk_temp,valchk_temp,raster_cal)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            else:
                                print 'Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh'
                                listmessagebox.append('Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh')
                                return False

                        elif len(sigchk_temp_list) == 1:                            
                        
                            sigchk_temp=sigchk_temp_list[0]
                            pkg.addteststepsread_var(tschk,sysid_model,sigchk_temp,valchk_temp,raster)

##                            pkg.addsigforec(sysid_model,sigchk_temp)
                            self.appendlist([sigchk_temp,sysid_model],self.list_case_recorder)
                        else:
                            print 'Please Check check_rw,contact lyh'
                            listmessagebox.append('Please Check check_rw,contact lyh')
                            return False                 

                        
##                        sigchk_temp=sigchk_temp_list[0]
##                        pkg.addteststepsread_var(tschk,sigchk_temp,valchk_temp,raster)
##
##                        self.appendlist(sigchk_temp,self.list_case_recorder)
                        
                    else:
                        if flag_addmutichk == 0:
                            tschk=pkg.addMutiCheck(parent,None,timeout)
                            flag_addmutichk = 1
                        sigchk_temp_list=sigchk_list[sigchk_num]
                        if len(sigchk_temp_list) == 2:
                            if sigchk_temp_list[1] == 'Calibration':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread(tschk,sysid_cal,sigchk_temp,valchk_temp)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            elif sigchk_temp_list[1] == 'Measurement':
                                sigchk_temp=sigchk_temp_list[0]
                                pkg.addteststepsread(tschk,sysid_cal,sigchk_temp,valchk_temp,raster_cal)

##                                pkg.addsigforec(sysid_cal,sigchk_temp)
                                self.appendlist([sigchk_temp,sysid_cal],self.list_case_recorder)
                            else:
                                print 'Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh'
                                listmessagebox.append('Calibration or Measurement Cannot be find,Please Check check_rw,contact lyh')
                                return False

                        elif len(sigchk_temp_list) == 1:                            
                        
                            sigchk_temp=sigchk_temp_list[0]
                            #print sigchk_temp
                            pkg.addteststepsread(tschk,sysid_model,sigchk_temp,valchk_temp,raster)

##                            pkg.addsigforec(sysid_model,sigchk_temp)
                            self.appendlist([sigchk_temp,sysid_model],self.list_case_recorder)
                        else:
                            print 'Please Check check_rw,contact lyh'
                            listmessagebox.append('Please Check check_rw,contact lyh')
                            return False 


                        
##                        sigchk_temp=sigchk_temp_list[0]
##                        pkg.addteststepsread(tschk,sigchk_temp,valchk_temp,raster)
##
##                        self.appendlist(sigchk_temp,self.list_case_recorder)

        else:
            timeout=tstime
            if timeout!='0.0':
                pkg.wait(parent,timeout)

        return True
                    
                    
        
        
        
    def hexid(self,intid):
        a=int(intid)
        b=hex(a)
        c=str(b)
        d=c[2: ]
        return d
    def appendlist(self,mapname,reclist):
        if mapname in reclist:
            pass
        else:
            reclist.append(mapname)
