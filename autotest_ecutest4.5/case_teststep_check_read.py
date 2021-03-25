# -*- coding: utf-8 -*-
import xlrd,os,sys        


class xlsfile:
    def __init__(self):
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
        self.pre_check=[]
        self.pre_time=[]
        self.pre_logic=[]
class casestep:
    def __init__(self):
##        self.case_num=[]
        #self.case_name=[]
##        self.case_data=[]
##        self.case_check=[]
        self.case_data=[]
        self.case_check=[]
        self.case_time=[]
        self.case_logic=[]
        
        #self.trace=[]
class posstep:
    def __init__(self):
##        self.pos_num=[]
        self.pos_data=[]
        self.pos_check=[]
        self.pos_time=[]
        self.pos_logic=[]


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

    def read_sig_val(self,case_colm_num,rownum_counter,case_test_num,sheet1,case_ID_temp,listmessagebox,flgerror):
        
        colmnum_counter=6
        flag_check=0

        list_signal_temp=[]
        list_value_temp=[]
        list_cksig_temp=[]
        list_ckval_temp=[]
        list_time_temp=[]
        list_logic_temp=[]

        try:

             ####read siganal#####
            while colmnum_counter<case_colm_num:
                signal_temp=sheet1.row(rownum_counter)[colmnum_counter].value
            #print signal_temp
                signal_temp=signal_temp.strip()

                if signal_temp=='check':
                    flag_check=1

                    colmnum_counter=colmnum_counter+1
                    colmnum_ckbg=colmnum_counter
           
                elif signal_temp!='' and flag_check==0:
                    list_signal_temp.append(signal_temp)
                    
                    colmnum_counter=colmnum_counter+1
                    colmnum_ac=colmnum_counter

                    #signal_temp=sheet1.row(rownum_counter)[colmnum_counter].value
                    #print signal_temp
                    #signal_temp=signal_temp.strip()                              
                    
                elif signal_temp!='' and flag_check==1:
                    list_cksig_temp.append(signal_temp)
                    
                    colmnum_counter=colmnum_counter+1
                    colmnum_cked=colmnum_counter
                else:
                    colmnum_counter=colmnum_counter+1
            

            rownum_counter=rownum_counter+1
            exl_value_temp=sheet1.row(rownum_counter)[5].value
            exl_value_temp1=sheet1.row(rownum_counter)[2].value
            ####read value#####
            while exl_value_temp.strip()=='' and exl_value_temp1=='':                            
            ##read pre action value##
                list_value_step_temp=[]
                colmnum_counter_temp=6
                while colmnum_counter_temp<colmnum_ac:
                    value_step_temp=sheet1.row(rownum_counter)[colmnum_counter_temp].value
                    value_step_temp=str(value_step_temp)
                    list_value_step_temp.append(value_step_temp)
                    colmnum_counter_temp=colmnum_counter_temp+1
                list_value_temp.append(list_value_step_temp)
            ##read pre check value##
                if flag_check==1:
                    list_value_ckstep_temp=[]
                    colmnum_counter_temp=colmnum_ckbg
                    while colmnum_counter_temp<colmnum_cked:
                        value_step_temp=sheet1.row(rownum_counter)[colmnum_counter_temp].value
                        value_step_temp=str(value_step_temp)
        ##                                    if not 'value' in value_step_temp and value_step_temp!='':
        ##                                        value_step_temp='value=='+value_step_temp
                        list_value_ckstep_temp.append(value_step_temp)
                        colmnum_counter_temp=colmnum_counter_temp+1
                    list_ckval_temp.append(list_value_ckstep_temp)

                
            ##read pre time##
                time_value_temp=sheet1.row(rownum_counter)[3].value
                time_value_temp=str(time_value_temp)
                list_time_temp.append(time_value_temp)

        ##read pre logic##

                logic_value_temp=sheet1.row(rownum_counter)[4].value
                logic_value_temp=str(logic_value_temp)
                list_logic_temp.append(logic_value_temp)
                
                rownum_counter=rownum_counter+1
                if rownum_counter<case_test_num:
                    exl_value_temp=sheet1.row(rownum_counter)[5].value
                    exl_value_temp1=sheet1.row(rownum_counter)[2].value
                else:#if rownum_counter is lager than case_test_num(total row number)
                    exl_value_temp='none'
                    exl_value_temp1='none'

            return True,rownum_counter,list_signal_temp,list_value_temp,list_cksig_temp,list_ckval_temp,list_time_temp,list_logic_temp

        except:
                
            print 'Please Check row %d column %d of case %s '%(rownum_counter+1,colmnum_counter_temp+1,str(case_ID_temp))

            message='Please Check row '+str(rownum_counter+1)+' column'+str(colmnum_counter_temp+1)+' of case '+ str(case_ID_temp)
            listmessagebox.append(message)
            flgerror=True
            return False,[],[],[],[],[],[],[]
            #sys.exit()

        
        
                 

    def testcase_rd_wt(self,filelist_array,filelist_name,listmessagebox,flgerror):

        testcase={}        
        
        for num in range(len(filelist_array)):
            
            #print filelist_name
            filename=filelist_name[num].split('.')
            filename=filename[0]
            print filename
            listmessagebox.append(filename)
            filename_path=filelist_array[num]
            wk=xlrd.open_workbook(filename_path)
           

            self.xlsinfo.testname=[]
            self.xlsinfo.testinfo.caseinfo.case_name=[]
            
            self.xlsinfo.testinfo.preinfo.pre_data=[]
            self.xlsinfo.testinfo.preinfo.pre_check=[]
            self.xlsinfo.testinfo.preinfo.pre_time=[]
            self.xlsinfo.testinfo.preinfo.pre_logic=[]

            self.xlsinfo.testinfo.caseinfo.case_data=[]
            self.xlsinfo.testinfo.caseinfo.case_check=[]
            self.xlsinfo.testinfo.caseinfo.case_time=[]
            self.xlsinfo.testinfo.caseinfo.case_logic=[]


            self.xlsinfo.testinfo.posinfo.pos_data=[]
            self.xlsinfo.testinfo.posinfo.pos_check=[]
            self.xlsinfo.testinfo.posinfo.pos_time=[]
            self.xlsinfo.testinfo.posinfo.pos_logic=[]          


            rownum_counter=1
            
                
            for sheetname in wk.sheets():

                if sheetname.name!='parameter':
                    sheet1=wk.sheet_by_name(sheetname.name)
    ##                self.fileinfo.xlsinfo.sheetname.append(sheetname.name) #append sheetname

                    case_test_num=sheet1.nrows  #sheet1 row numbers
                    case_colm_num=sheet1.ncols  #sheet1 colm numbers

                    while rownum_counter<case_test_num:
                        case_ID_temp_val=sheet1.row(rownum_counter)[2]
                        case_ID_temp_val=case_ID_temp_val.value
                        #print case_ID_temp

                        if case_ID_temp_val.strip()!='':##maybe error
                            case_ID_temp=case_ID_temp_val
                            self.xlsinfo.testinfo.caseinfo.case_name.append(case_ID_temp)  #append testname
                            rownum_counter=rownum_counter+1#after read caseID,rownum_counter which add 1 can read next row next time                    
                            
                        exl_value_temp=sheet1.row(rownum_counter)[5].value
                        #rownum_counter=rownum_counter+1
                        
    #############precondition##################
                        if exl_value_temp=='pre':
                            #colmnum_counter=6

                            case_prestep_array=[]
                            case_preck_array=[]
                            case_time_array=[]
                            case_logic_array=[]

                            list_signal_temp=[]
                            list_value_temp=[]
                            list_cksig_temp=[]
                            list_ckval_temp=[]
                            list_time_temp=[]
                            list_logic_temp=[]

                            reflag,rownum_counter,list_signal_temp,list_value_temp,list_cksig_temp,list_ckval_temp,list_time_temp,\
                            list_logic_temp=self.read_sig_val(case_colm_num,rownum_counter,case_test_num,sheet1,case_ID_temp,\
                                                              listmessagebox,flgerror)

                            if reflag == True:                            
                                case_prestep_array.append(list_signal_temp)
                                case_prestep_array.append(list_value_temp)
                                self.xlsinfo.testinfo.preinfo.pre_data.append(case_prestep_array)

                                case_preck_array.append(list_cksig_temp)
                                case_preck_array.append(list_ckval_temp)
                                self.xlsinfo.testinfo.preinfo.pre_check.append(case_preck_array)

                                case_time_array.append(list_time_temp)
                                self.xlsinfo.testinfo.preinfo.pre_time.append(case_time_array)

                                case_logic_array.append(list_logic_temp)
                                self.xlsinfo.testinfo.preinfo.pre_logic.append(case_logic_array)
                            else:
                                return None                                

    #############action##################
                        elif exl_value_temp=='action':
                            #colmnum_counter=6

                            case_prestep_array=[]
                            case_preck_array=[]
                            case_time_array=[]
                            case_logic_array=[]
                            

                            list_signal_temp=[]
                            list_value_temp=[]
                            list_cksig_temp=[]
                            list_ckval_temp=[]
                            list_time_temp=[]
                            list_logic_temp=[]

                            reflag,rownum_counter,list_signal_temp,list_value_temp,list_cksig_temp,list_ckval_temp,list_time_temp,\
                            list_logic_temp=self.read_sig_val(case_colm_num,rownum_counter,case_test_num,sheet1,case_ID_temp,\
                                                              listmessagebox,flgerror)


                            if reflag == True:
                                
                                case_prestep_array.append(list_signal_temp)
                                case_prestep_array.append(list_value_temp)
                                self.xlsinfo.testinfo.caseinfo.case_data.append(case_prestep_array)

                                case_preck_array.append(list_cksig_temp)
                                case_preck_array.append(list_ckval_temp)
                                self.xlsinfo.testinfo.caseinfo.case_check.append(case_preck_array)

                                case_time_array.append(list_time_temp)
                                self.xlsinfo.testinfo.caseinfo.case_time.append(case_time_array)

                                case_logic_array.append(list_logic_temp)
                                self.xlsinfo.testinfo.caseinfo.case_logic.append(case_logic_array)
                            else:
                                return None

    #############poscondition##################
                        elif exl_value_temp=='pos':
                            #colmnum_counter=6

                            case_prestep_array=[]
                            case_preck_array=[]
                            case_time_array=[]
                            case_logic_array=[]
                            

                            list_signal_temp=[]
                            list_value_temp=[]
                            list_cksig_temp=[]
                            list_ckval_temp=[]
                            list_time_temp=[]
                            list_logic_temp=[]

                            reflag,rownum_counter,list_signal_temp,list_value_temp,list_cksig_temp,list_ckval_temp,list_time_temp,\
                            list_logic_temp=self.read_sig_val(case_colm_num,rownum_counter,case_test_num,sheet1,case_ID_temp,\
                                                              listmessagebox,flgerror)

                                
                            if reflag == True:
                                case_prestep_array.append(list_signal_temp)
                                case_prestep_array.append(list_value_temp)
                                self.xlsinfo.testinfo.posinfo.pos_data.append(case_prestep_array)

                                case_preck_array.append(list_cksig_temp)
                                case_preck_array.append(list_ckval_temp)
                                self.xlsinfo.testinfo.posinfo.pos_check.append(case_preck_array)

                                case_time_array.append(list_time_temp)
                                self.xlsinfo.testinfo.posinfo.pos_time.append(case_time_array)

                                case_logic_array.append(list_logic_temp)
                                self.xlsinfo.testinfo.posinfo.pos_logic.append(case_logic_array)
                            else:
                                return None
                            
                        else:
                            rownum_counter=rownum_counter+1
            testcase[filename]=[self.xlsinfo.testinfo.caseinfo.case_name,self.xlsinfo.testinfo.preinfo.pre_data,\
                            self.xlsinfo.testinfo.preinfo.pre_check,self.xlsinfo.testinfo.preinfo.pre_time,\
                            self.xlsinfo.testinfo.preinfo.pre_logic,self.xlsinfo.testinfo.caseinfo.case_data,\
                            self.xlsinfo.testinfo.caseinfo.case_check,self.xlsinfo.testinfo.caseinfo.case_time,\
                            self.xlsinfo.testinfo.caseinfo.case_logic,self.xlsinfo.testinfo.posinfo.pos_data,\
                            self.xlsinfo.testinfo.posinfo.pos_check,self.xlsinfo.testinfo.posinfo.pos_time,\
                            self.xlsinfo.testinfo.posinfo.pos_logic]
        return testcase

    

if __name__=='__main__':
    import window_f

    listmessagebox=[]
    flgerror=False
    
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
    case_dict=testcase.testcase_rd_wt(filelist_array,filelist_array_temp,listmessagebox,flgerror)
    #print case_dict
