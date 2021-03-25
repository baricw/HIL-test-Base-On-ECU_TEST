### -*- coding: utf-8 -*-
import xlrd,os


        

##class nowfile:
##    def __init__(self):
##        self.xlsname=[]
##        self.xlsinfo=[]
class xlsfile:
    def __init__(self):
##        self.sheetname=[]
##        self.sheetinfo=[]
##class sheetfile:
##    def __init__(self):
        self.testname=[]
        self.testinfo=[]
class testcase:
    def __init__(self):
        self.preinfo=[]
        self.caseinfo=[]
        self.posinfo=[]
class prestep:
    def __init__(self):
##        self.pre_num=[]
        self.pre_data=[]
class casestep:
    def __init__(self):
##        self.case_num=[]
        self.case_name=[]
        self.case_data=[]
        self.check=[]
        self.trace=[]
class posstep:
    def __init__(self):
##        self.pos_num=[]
        self.pos_data=[]


class test_case_prepare:
    def __init__(self):
##        self.fileinfo=nowfile()
        self.xlsinfo=xlsfile()
##        self.fileinfo.xlsinfo.sheetinfo=sheetfile()
        self.xlsinfo.testinfo=testcase()        
        self.xlsinfo.testinfo.preinfo=prestep()
        self.xlsinfo.testinfo.caseinfo=casestep()
        self.xlsinfo.testinfo.posinfo=posstep()
        
    def filter_file(self,filelist,filetype):
        filelist_name=[]
        for file_name in filelist:
            if file_name.find(filetype)>0 and file_name.find('$')<0:
                filelist_name.append(file_name)
##                self.fileinfo.xlsname.append(file_name)  #append xlsname
            else:
                pass
        return filelist_name
                 

    def testcase_rd_wt(self,filelist_array,filelist_name):
##        case_name_array_xls=[]
##        case_test_array_xls=[]
##        check_array_xls=[]
##        case_pretest_array_xls=[]
##        case_postest_array_xls=[]
##        trace_array_xls=[]

        testcase={}        
        
        for num in range(len(filelist_array)):
            
            #print filelist_name
            filename=filelist_name[num].split('.')
            filename=filename[0]
            print filename
            filename_path=filelist_array[num]
            wk=xlrd.open_workbook(filename_path)
           
##            case_name_array_sheet=[]
##            case_test_array_sheet=[]
##            check_array_sheet=[]
##            case_pretest_array_sheet=[]
##            case_postest_array_sheet=[]
##            trace_array_sheet=[]
            self.xlsinfo.testname=[]
            self.xlsinfo.testinfo.caseinfo.case_name=[]
            self.xlsinfo.testinfo.preinfo.pre_data=[]            
            self.xlsinfo.testinfo.caseinfo.case_data=[]
            self.xlsinfo.testinfo.caseinfo.check=[]
            self.xlsinfo.testinfo.caseinfo.trace=[]
            self.xlsinfo.testinfo.posinfo.pos_data=[]
            
                
            for sheetname in wk.sheets():
                sheet1=wk.sheet_by_name(sheetname.name)
##                self.fileinfo.xlsinfo.sheetname.append(sheetname.name) #append sheetname
                case_test_num=sheet1.nrows  #sheet1 numbers
                case_test_num_loopnum=0
                #sheet中的所有用例
                for case_test_num_loopnum in range(case_test_num-1):
                
                
                    check_case_num=[]        
                    check_dict={}
                    trace_step_Prototype=[]
                    trace_dict={}

                    
                    case_name=sheet1.row(case_test_num_loopnum+1)[0]
                    case_name=case_name.value
                    #case_name=case_name.strip('text:')
                    if case_name.strip()!='':
                        #case_name_array.append(case_name)
                        self.xlsinfo.testinfo.caseinfo.case_name.append(case_name)  #append testname
                        
            #############precondition##################
                        try:
                            case_prestep_array=[]
                            precase=sheet1.row(case_test_num_loopnum+1)[6]
                            precase=precase.value
                            #precase=precase.strip('text:')
                            precase_step=precase.split(';')

                            for step_num in range(len(precase_step)-1):
                                step_temp1=precase_step[step_num].split(':')
                                #print step_temp1
                                #self.fileinfo.xlsinfo.sheetinfo.preinfo.append(step_temp1[0].strip('step'))#append step_num
                                step_temp2=step_temp1[1].split(',')
                                #print step_temp2
                                step_temp2_num=0

                                pretest_signal=[]
                                pretest_value=[]

                #precondition signals            
                                for step_temp2_num in range(len(step_temp2)):
                                               
                                    step_temp3=step_temp2[step_temp2_num].split('=')
                                
                                
                                    test_signal_temp=''.join(step_temp3[0].split('\\n'))
                                    test_value_temp=''.join(step_temp3[1].split('\\n'))
                               
                                 
                                    pretest_signal.append(test_signal_temp.strip())
                                    pretest_value.append(test_value_temp.strip())
                                
                                
                        
                                case_prestep_array.append((pretest_signal,pretest_value))
                                                    
                            self.xlsinfo.testinfo.preinfo.pre_data.append(case_prestep_array)
                        except:
                            print 'Excel_testcase '+case_name+' of precondition has some wrong'
                        

            #############poscondition##################
                        try:
                            case_posstep_array=[]
                            poscase=sheet1.row(case_test_num_loopnum+1)[9]
                            poscase=poscase.value
                            #poscase=poscase.strip('text:')
                            poscase_step=poscase.split(';')

                            for step_num in range(len(poscase_step)-1):
                                step_temp1=poscase_step[step_num].split(':')
                                #print step_temp1
                                #self.fileinfo.xlsinfo.sheetinfo.posinfo.pos_num.append(step_temp1[0].strip('step'))
                                step_temp2=step_temp1[1].split(',')
                                #print step_temp2
                                step_temp2_num=0

                                postest_signal=[]
                                postest_value=[]

                #poscondition signals            
                                for step_temp2_num in range(len(step_temp2)):
                                               
                                    step_temp3=step_temp2[step_temp2_num].split('=')
                                
                                
                                    test_signal_temp=''.join(step_temp3[0].split('\\n'))
                                    test_value_temp=''.join(step_temp3[1].split('\\n'))
                               
                                 
                                    postest_signal.append(test_signal_temp.strip())
                                    postest_value.append(test_value_temp.strip())
                                
                                
                        
                                case_posstep_array.append((postest_signal,postest_value))           
                                
                            
                            #case_postest_array.append(case_posstep_array)
                            self.xlsinfo.testinfo.posinfo.pos_data.append(case_posstep_array)
                        except:
                            print 'Excel_testcase '+case_name+' of poscondition has some wrong'




                        
            #############action step&check##################
                        try:
                            case_step_array=[]
                            case=sheet1.row(case_test_num_loopnum+1)[7]
                            case=case.value
                            #case=case.strip('text:')
                            case_step=case.split(';')       
                            

                #testcase steps       
                            
                            for step_num in range(len(case_step)-1):
                                step_temp1=case_step[step_num].split(':')
                                #print step_temp1
                                step_temp2=step_temp1[1].split(',')
                                #print step_temp2
                                step_temp2_num=0

                                test_signal=[]
                                test_value=[]                            

                #step signals            
                                for step_temp2_num in range(len(step_temp2)):
                                               
                                    step_temp3=step_temp2[step_temp2_num].split('=')
                                
                                
                                    test_signal_temp=''.join(step_temp3[0].split('\\n'))
                                    test_value_temp=''.join(step_temp3[1].split('\\n'))
                               
                                 
                                    test_signal.append(test_signal_temp.strip())
                                    test_value.append(test_value_temp.strip())
                                
                                
                        
                                case_step_array.append((test_signal,test_value))           
                                
                            
                            #case_test_array.append(case_step_array)
                            self.xlsinfo.testinfo.caseinfo.case_data.append(case_step_array)
                        except:
                            print 'Excel_testcase '+case_name+' of test_step has some wrong'


                        try:                
                            check_step_array=[]
                            check=sheet1.row(case_test_num_loopnum+1)[8]
                            check=check.value
                            #check=check.strip('text:')
                            if len(check)!=0:
                                check_step=check.split(';')
                    #check numbers
                            
                                for check_num in range(len(check_step)-1):
                                    check_temp1=check_step[check_num].split(':')
                                    #print check_temp1
                                    check_temp2=check_temp1[1].split(',')
                                    #print check_temp2
                                    check_temp22=check_temp1[0].split('check')
                                    check_temp33=check_temp22[1]
                                    check_case_num.append(check_temp33)
                                    check_signal=[]
                                    check_value=[]
                                    check_time=[]
                                
                    #check signals
                                    for check_temp2_num in range(len(check_temp2)):
                                        #####（）replace @，so add the module#####
                                        check_temp3=[]                               
                                        left_index=check_temp2[check_temp2_num].index('(')
                                        right_index=check_temp2[check_temp2_num].rindex(')')
                                        check_temp3.append(check_temp2[check_temp2_num][0:left_index])
                                        #print check_temp3
                                        check_temp22=check_temp2[check_temp2_num][left_index+1:right_index]
                                        check_temp23=check_temp22.split('@')
                                        for check_temp23_temp in check_temp23:
                                            check_temp3.append(check_temp23_temp)
                                        ##########the module######    
                                        #print check_temp3
                                        if len(check_temp3)==3:
                                            check_signal_temp=''.join(check_temp3[0].split('\\n'))
                                            check_value_temp=''.join(check_temp3[1].split('\\n'))
                                            check_time_temp=''.join(check_temp3[2].split('\\n'))
                                            check_signal.append(check_signal_temp.strip())
                                            check_value.append(check_value_temp.strip())
                                            check_time.append(check_time_temp.strip())
                                        elif len(check_temp3)==2:
                                            check_signal_temp=''.join(check_temp3[0].split('\\n'))
                                            check_value_temp=''.join(check_temp3[1].split('\\n'))
                                            check_time_temp=0
                                            check_signal.append(check_signal_temp.strip())
                                            check_value.append(check_value_temp.strip())
                                            check_time.append(check_time_temp)                        
                                        else:
                                            print case_name+' check_step have wrong'
                                            
                                            
                                            
                                    check_step_array.append((check_signal,check_value,check_time))
                                    
                                    for (k,v) in zip(check_case_num,check_step_array):
                                        check_dict[k]=v

                            else:
                                check_dict={}
                            
                            #check_array.append(check_dict)
                            self.xlsinfo.testinfo.caseinfo.check.append(check_dict)
                        except:
                            print 'Excel_testcase '+case_name+' of check_step has some wrong'

            #############trace analysis##################
                        try:
                            
                            traceAnalysis_array=[]
                            traceAnalysis=sheet1.row(case_test_num_loopnum+1)[10]
                            traceAnalysis=traceAnalysis.value
                            #traceAnalysis=traceAnalysis.strip('text:')
                            if len(traceAnalysis)!=0:                
                                trace_step=traceAnalysis.split(';')
                                #print len(trace_step)
                                for trace_step_num in range(len(trace_step)-1):
                                    trace_step_temp1=trace_step[trace_step_num].split(':')
                                    trace_step_temp11=trace_step_temp1[0].strip()
                                    trace_step_Prototype.append(trace_step_temp11)
                                    trace_step_temp2=trace_step_temp1[1].split(',')

                                    trace_Innname=[]
                                    trace_mapName=[]                
                            

                                    for trace_step_temp2_num in range(len(trace_step_temp2)):
                                        trace_step_temp3=trace_step_temp2[trace_step_temp2_num].split('=')
                                    
                                    
                                        trace_Inname_temp=''.join(trace_step_temp3[0].split('\\n'))
                                        trace_mapName_temp=''.join(trace_step_temp3[1].split('\\n'))
                                        
                                        trace_Innname.append(trace_Inname_temp.strip())
                                        trace_mapName.append(trace_mapName_temp.strip())
                                    traceAnalysis_array.append((trace_Innname,trace_mapName))
                                    
                                for (k,v) in zip(trace_step_Prototype,traceAnalysis_array):
                                    trace_dict[k]=v

                                #print trace_dict
                                
                            else:
                                trace_dict={}

                            #case_trace_array.append(trace_dict)
                            self.xlsinfo.testinfo.caseinfo.trace.append(trace_dict)
                        except:
                            print  'Excel_testcase '+case_name+' of case_trace has some wrong'
                    else:
                        pass
            testcase[filename]=(self.xlsinfo.testinfo.caseinfo.case_name,self.xlsinfo.testinfo.preinfo.pre_data,\
					    self.xlsinfo.testinfo.caseinfo.case_data,self.xlsinfo.testinfo.caseinfo.check,\
        				    self.xlsinfo.testinfo.posinfo.pos_data,self.xlsinfo.testinfo.caseinfo.trace)
        return testcase
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




        
