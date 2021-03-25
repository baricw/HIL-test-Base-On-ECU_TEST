# -*- coding: utf-8 -*-
import os 
import xlwt
from case_teststep_check_read_old import *

def modelcase_Create(case_dict):
##        ErroNum=0
##        
##        pkg=self.pkg
##        decimal.getcontext().prec=4
##        percent_case=decimal.Decimal(0)
##        precent_progress=decimal.Decimal(0)
##        print 'Start Create Packages.....'

    

    list_casedict_key=list(case_dict.keys())
##        percent_factor=decimal.Decimal(1)/decimal.Decimal(len(list_casedict_key))
##        #print 'percent_factor='+str(percent_factor)
    for filenum in range(len(list_casedict_key)):

        wk=xlwt.Workbook()
        
        case_tuple=case_dict[list_casedict_key[filenum]]
        
##            case_name_array_sheet=case_name_array_xls[filenum]
##            case_test_array_sheet=case_test_array_xls[filenum]
##            check_array_sheet=check_array_xls[filenum]
##            case_pretest_array_sheet=case_pretest_array_xls[filenum]
##            case_postest_array_sheet=case_postest_array_xls[filenum]
##            case_trace_array_sheet=case_trace_array_xls[filenum]

        #percent_file=percent_case*percent_factor
        #print 'percent_file='+str(percent_file)
        

##            for sheetnum in range(len(case_name_array_sheet)):

##                case_name_array=case_name_array_sheet[sheetnum]
##                case_test_array=case_test_array_sheet[sheetnum]
##                check_array=check_array_sheet[sheetnum]
##                case_pretest_array=case_pretest_array_sheet[sheetnum]
##                case_postest_array=case_postest_array_sheet[sheetnum]
##                case_trace_array=case_trace_array_sheet[sheetnum]

        case_name_array=case_tuple[0]
        case_test_array=case_tuple[2]
        check_array=case_tuple[3]
        case_pretest_array=case_tuple[1]
        case_postest_array=case_tuple[4]
        case_trace_array=case_tuple[5]

        sheetname=wk.add_sheet('case',cell_overwrite_ok=True)
        sheetname.write(0,0,'Requirement')
        sheetname.write(0,1,'Priority')
        sheetname.write(0,2,'ID')
        sheetname.write(0,3,'Time(s)')
        sheetname.write(0,4,'Logic')
        sheetname.write(0,5,'Conditon')

        row_num1=1
        row_num2=3        

##            percent_sheet=decimal.Decimal(sheetnum+1)/decimal.Decimal(len(case_name_array_sheet))
        #percent_case=decimal.Decimal(1)/decimal.Decimal(len(case_test_array))
        
        for case_test_num_loopnum in range(len(case_test_array)):

            

            #percent_case=decimal.Decimal(case_test_num_loopnum+1)/decimal.Decimal(len(case_test_array))
            #print 'percent_case='+str(percent_case)
            
            #precent_progress=(percent_case*percent_factor)*100+precent_progress
            #print '.'+str(int(precent_progress))+'%',
            colm_num1=5
            colm_num_pre=6
            colm_num_act=6
            colm_num_chk=16
            colm_num_pos=6

            case_name=case_name_array[case_test_num_loopnum]
            #case_name=case_name.strip("u''")
            case_check_dict=check_array[case_test_num_loopnum]
            if case_name!='':
                #try:
                #sheetname=wk.add_sheet(case_name,cell_overwrite_ok=True)
                sheetname.write(row_num1,2,case_name)
                row_num1=row_num1+1
                    #preparent,acparent,postparent=pkg.CreatePackage()
                #except:
                    #print '\nPlease check licence,cannot creat package'
                    #ErroNum+=1
                    
            else:
                continue

            pre_dict_colmpos=dict()
            

########create precondition
            sheetname.write(row_num1,colm_num1,'pre')
            for step_num in range(len(case_pretest_array[case_test_num_loopnum])):
                flag_havetime=0
                
                haveval_pos=[]
                
                for signal_num in range(len(case_pretest_array[case_test_num_loopnum][step_num][0])):
                     
                     signal_name_temp=case_pretest_array[case_test_num_loopnum][step_num][0][signal_num]
                     signal_value_temp=case_pretest_array[case_test_num_loopnum][step_num][1][signal_num]
                     #signal_IO_status=signal_name_temp in io_dict
                     #signal_name_temp_wt=signal_name_temp+'_wt'

                     try:
                        if signal_name_temp=='wait':
                            time=signal_value_temp                            
                            sheetname.write(row_num2,3,time)
                            flag_havetime=1
                        else:
                            if signal_name_temp in list(pre_dict_colmpos.keys()):
                                colm_num_temp=pre_dict_colmpos[signal_name_temp]

                                if (row_num2,colm_num_temp) in haveval_pos:
                                    row_num2=row_num2+1
                                    sheetname.write(row_num2,colm_num_temp,signal_value_temp)
                                    
                                    if flag_havetime==0:                    
                                        sheetname.write(row_num2,3,'0')
                                    else:
                                        flag_havetime=0                                
                                        
                                    haveval_pos.append((row_num2,colm_num_temp))
                                else:
                                    sheetname.write(row_num2,colm_num_temp,signal_value_temp)
                                    haveval_pos.append((row_num2,colm_num_temp))
                                #row_num2=row_num2+1
                            else:
                                pre_dict_colmpos[signal_name_temp]=colm_num_pre
                                sheetname.write(row_num1,colm_num_pre,signal_name_temp)

                                if (row_num2,colm_num_pre) in haveval_pos:
                                    row_num2=row_num2+1
                                    sheetname.write(row_num2,colm_num_pre,signal_value_temp)

                                    if flag_havetime==0:                    
                                        sheetname.write(row_num2,3,'0')
                                    else:
                                        flag_havetime=0
                                        
                                    haveval_pos.append((row_num2,colm_num_pre))
                                else:
                                    sheetname.write(row_num2,colm_num_pre,signal_value_temp)
                                    haveval_pos.append((row_num2,colm_num_pre))

                                
                                #sheetname.write(row_num2,colm_num1,signal_value_temp)
                                colm_num_pre=colm_num_pre+1
                                #row_num2=row_num2+1                           
    
                     except:
                        print '\nThere are some problems in Testcase '
                if flag_havetime==0:                    
                    sheetname.write(row_num2,3,'0')
                    
									
                row_num2=row_num2+1

            row_num1=row_num2
            row_num2=row_num2+1

            act_dict_colmpos=dict()
            check_dict_colmpos=dict()

##########create step&check
            sheetname.write(row_num1,colm_num1,'action')
            sheetname.write(row_num1,colm_num_chk-1,'check')
            for step_num in range(len(case_test_array[case_test_num_loopnum])):                
                flag_havetime=0
                haveval_pos=[]
                #print case_test_array[case_test_num_loopnum][step_num][0]

                for signal_num in range(len(case_test_array[case_test_num_loopnum][step_num][0])):                    
                     
                    signal_name_temp=case_test_array[case_test_num_loopnum][step_num][0][signal_num]
                    signal_value_temp=case_test_array[case_test_num_loopnum][step_num][1][signal_num]

                    try:
                        if signal_name_temp=='wait':
                            time=signal_value_temp                            
                            sheetname.write(row_num2,3,time)
                            flag_havetime=1
                        else:
                            if signal_name_temp in list(act_dict_colmpos.keys()):
                                colm_num_temp=act_dict_colmpos[signal_name_temp]

                                if (row_num2,colm_num_temp) in haveval_pos:
                                    row_num2=row_num2+1
                                    sheetname.write(row_num2,colm_num_temp,signal_value_temp)
                                    if flag_havetime==0:                    
                                        sheetname.write(row_num2,3,'0')
                                    else:
                                        flag_havetime=0
                                    haveval_pos.append((row_num2,colm_num_temp))
                                else:
                                    sheetname.write(row_num2,colm_num_temp,signal_value_temp)
                                    haveval_pos.append((row_num2,colm_num_temp))
                                
                            else:
                                act_dict_colmpos[signal_name_temp]=colm_num_act
                                sheetname.write(row_num1,colm_num_act,signal_name_temp)

                                if (row_num2,colm_num_act) in haveval_pos:
                                    row_num2=row_num2+1
                                    sheetname.write(row_num2,colm_num_act,signal_value_temp)
                                    if flag_havetime==0:                    
                                        sheetname.write(row_num2,3,'0')
                                    else:
                                        flag_havetime=0
                                    haveval_pos.append((row_num2,colm_num_act))
                                else:
                                    sheetname.write(row_num2,colm_num_act,signal_value_temp)
                                    haveval_pos.append((row_num2,colm_num_act))                                
                                
                                colm_num_act=colm_num_act+1                                                         
    
                    except:
                        print '\nThere are some problems in Testcase '


                step_num_str=str(step_num+1)
                key_state=step_num_str in case_check_dict

                if key_state == True:
                    check_step_temp=case_check_dict[step_num_str]

                    #try:
                    for check_signal_num in range(len(check_step_temp[0])):
                        check_time=check_step_temp[2][check_signal_num]
                        if check_time==0:
                        
                            if check_step_temp[1][check_signal_num].find('save')==0:
                                check_signal= check_step_temp[0][check_signal_num]
                                store_name = check_step_temp[1][check_signal_num][5:]



                                if check_signal in list(check_dict_colmpos.keys()):
                                    colm_num_temp=check_dict_colmpos[check_signal]
                                    
                                    sheetname.write(row_num2,colm_num_temp,store_name)                                            
                                else:
                                    check_dict_colmpos[check_signal]=colm_num_chk
                                    sheetname.write(row_num1,colm_num_chk,check_signal)
                                    sheetname.write(row_num2,colm_num_chk,store_name)                                                                          
                                    
                                    colm_num_chk=colm_num_chk+1                                 

                                
                                
##                                        pkg.addteststepsread_var(parent,check_signal,store_name)
                            else:
                                check_signal= check_step_temp[0][check_signal_num]
                                check_value = check_step_temp[1][check_signal_num]

                                if 'value==' in check_value and not 'or' in check_value and not 'and' in check_value:
                                    check_value=check_value.strip('value==')
                                

                                if check_signal in list(check_dict_colmpos.keys()):
                                    colm_num_temp=check_dict_colmpos[check_signal]                                        
                                    sheetname.write(row_num2,colm_num_temp,check_value)                                            
                                else:
                                    check_dict_colmpos[check_signal]=colm_num_chk
                                    sheetname.write(row_num1,colm_num_chk,check_signal)
                                    sheetname.write(row_num2,colm_num_chk,check_value)                                                                          
                                    
                                    colm_num_chk=colm_num_chk+1 


                                
                                #pkg.addteststepsread(parent,check_signal,check_value)
                        elif check_time.find('until')!=-1:
                            check_time=check_time.strip('until')
                            check_signal= check_step_temp[0][check_signal_num]
                            check_value = check_step_temp[1][check_signal_num]

                            if 'value==' in check_value and not 'or' in check_value and not 'and' in check_value:
                                check_value=check_value.strip('value==')

                            sheetname.write(row_num2,3,'u'+check_time)
                            flag_havetime=1

                            if check_signal in list(check_dict_colmpos.keys()):
                                colm_num_temp=check_dict_colmpos[check_signal]
                                
                                sheetname.write(row_num2,colm_num_temp,check_value)                                            
                            else:
                                check_dict_colmpos[check_signal]=colm_num_chk
                                sheetname.write(row_num1,colm_num_chk,check_signal)
                                sheetname.write(row_num2,colm_num_chk,check_value)                                                                          
                                
                                colm_num_chk=colm_num_chk+1

                                
                           # pkg.addteststepsread_until(parent,check_signal,check_value,check_time)
                        elif check_time.find('still')!=-1:
                            check_time=check_time.strip('still')
                            check_signal= check_step_temp[0][check_signal_num]
                            check_value = check_step_temp[1][check_signal_num]

                            if 'value==' in check_value and not 'or' in check_value and not 'and' in check_value:
                                check_value=check_value.strip('value==')

                            sheetname.write(row_num2,3,'s'+check_time)
                            flag_havetime=1

                            if check_signal in list(check_dict_colmpos.keys()):
                                colm_num_temp=check_dict_colmpos[check_signal]
                                
                                sheetname.write(row_num2,colm_num_temp,check_value)                                            
                            else:
                                check_dict_colmpos[check_signal]=colm_num_chk
                                sheetname.write(row_num1,colm_num_chk,check_signal)
                                sheetname.write(row_num2,colm_num_chk,check_value)                                                                          
                                
                                colm_num_chk=colm_num_chk+1
                            #pkg.addteststepsread_still(parent,check_signal,check_value,check_time)
                        else:
                            print  case_name+' check'+str(step_num+1)+' time has wrong'

                if flag_havetime==0:
                    sheetname.write(row_num2,3,'0')

                        #except:
                            #print 'wrong'
                row_num2=row_num2+1
                 
            row_num1=row_num2
            row_num2=row_num2+1

            pos_dict_colmpos=dict()

###########create posstep
            sheetname.write(row_num1,colm_num1,'pos')
            for step_num in range(len(case_postest_array[case_test_num_loopnum])):
                flag_havetime=0
                haveval_pos=[]
                
                for signal_num in range(len(case_postest_array[case_test_num_loopnum][step_num][0])):
                     
                     signal_name_temp=case_postest_array[case_test_num_loopnum][step_num][0][signal_num]
                     signal_value_temp=case_postest_array[case_test_num_loopnum][step_num][1][signal_num]
##                     signal_IO_status=signal_name_temp in io_dict
##                     signal_name_temp_wt=signal_name_temp+'_wt'

                     try:
                        if signal_name_temp=='wait':
                            time=signal_value_temp

                            sheetname.write(row_num2,3,time)
                            flag_havetime=1
                            #pkg.waittime(postparent,time)
                        else:
                            if signal_name_temp in list(pos_dict_colmpos.keys()):
                                colm_num_temp=pos_dict_colmpos[signal_name_temp]

                                if (row_num2,colm_num_temp) in haveval_pos:
                                    row_num2=row_num2+1
                                    sheetname.write(row_num2,colm_num_temp,signal_value_temp)

                                    if flag_havetime==0:                    
                                        sheetname.write(row_num2,3,'0')
                                    else:
                                        flag_havetime=0
                                        
                                    haveval_pos.append((row_num2,colm_num_temp))
                                else:
                                    sheetname.write(row_num2,colm_num_temp,signal_value_temp)
                                    haveval_pos.append((row_num2,colm_num_temp))
                                #row_num2=row_num2+1
                            else:
                                pos_dict_colmpos[signal_name_temp]=colm_num_pos
                                sheetname.write(row_num1,colm_num_pos,signal_name_temp)

                                if (row_num2,colm_num_pos) in haveval_pos:
                                    row_num2=row_num2+1
                                    sheetname.write(row_num2,colm_num_pos,signal_value_temp)

                                    if flag_havetime==0:                    
                                        sheetname.write(row_num2,3,'0')
                                    else:
                                        flag_havetime=0
                                        
                                    haveval_pos.append((row_num2,colm_num_pos))
                                else:
                                    sheetname.write(row_num2,colm_num_pos,signal_value_temp)
                                    haveval_pos.append((row_num2,colm_num_pos))

                                
                                #sheetname.write(row_num2,colm_num1,signal_value_temp)
                                colm_num_pos=colm_num_pos+1
    
                     except:
                        print '\nThere are some problems in Testcase '+case_name+' posstep'+str(step_num+1)

                if flag_havetime==0:
                    sheetname.write(row_num2,3,'0')
                        #ErroNum+=1
                row_num2=row_num2+1
                 
            row_num1=row_num2
            row_num2=row_num2+2

            

        path=os.getcwd()
        wk.save(path+'\\'+list_casedict_key[filenum]+'.xls')
        del wk

if __name__=='__main__':
    import window_f
    testinfo=window_f.test_info()
    oldpath=os.getcwd()
    filepath=testinfo.select_dir('testcase')
    os.chdir(filepath)
    filelist = os.listdir(os.getcwd())
    os.chdir(oldpath)
##    
    
    testcase=test_case_prepare()
    filetype='.xls'    
    filelist_array_temp=testcase.filter_file(filelist,filetype)
    print filelist_array_temp
##
    filelist_array=[]
    for file_name in filelist_array_temp:
        filename_temp=filepath+'\\'+file_name
        filelist_array.append(filename_temp)
##        
##        
    case_dict=testcase.testcase_rd_wt(filelist_array,filelist_array_temp)

    modelcase_Create(case_dict)    
