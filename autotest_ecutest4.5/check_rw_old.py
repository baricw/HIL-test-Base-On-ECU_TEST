# -*- coding: utf-8 -*-
import os ,sys,sqlite3
from case_teststep_check_read import *
from map_read import *
#from dbc_read import *
from a2l_read import *

import ui_MainCreate

class testcase_excute:
    def __init__(self):
        self.casename=[]
        self.casedetail=[]
        self.caseresult=[]
    

class Check_rw:

    def create_maplist(self,HILname,modelmapfpath,listmessagebox,flgerror):

        if HILname=='ETAS':
            #f=open('E:\\temp\\py\\autotest_ecutest4.5\\MappingFile.txt')#ETAS HIL
            f=open(modelmapfpath)#ETAS HIL
            
            map_file=f.readlines()
            map_list=[]
            for map_file_every in map_file:
                map_file_temp = map_file_every.split('=')
                if len(map_file_temp)==2:
                    map_list.append(map_file_temp[1].strip())
            
        elif HILname=='DSPACE':
            #f=open('E:\\temp\\py\\autotest_ecutest4.5\\maplist.txt')
            f=open(modelmapfpath)
            map_file=f.readlines()
            #print map_file
            map_list=[]
            for map_file_every in map_file:
                map_file_every=map_file_every.strip()
                #print map_file_every
                
                map_list.append(map_file_every)
        else:
            print 'Please Select HIL Type....!!!'
            messagebox='Please Select HIL Type....!!!'
            listmessagebox.append(messagebox)
                    
            flgerror=True
            return None
            
        return map_list

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass

    def list_postion(self,signal,flag_bc):
          #flag_bc:1--CLN  0--BUS

        flag_find = 0

        conn = sqlite3.connect('Matrix.db')
        cursor = conn.cursor()

        cursor.execute("select name from sqlite_master where type='table'")
        tablename_list = cursor.fetchall()
        #table_list = []
        for table in tablename_list:
            tablename = str(table[0])
            if flag_bc == 1:
                  excu = "select messagename from "+tablename+" where signalname='"+signal+"'"
                  cursor.execute(excu)

                  temp_list = cursor.fetchall()
                  if temp_list:
                      msgname = temp_list[0][0]
                      flag_find = 1                
                      break
                  else:
                      pass
            if flag_bc == 0:
                  excu = "select * from "+tablename+" where messagename='"+signal+"'"
                  cursor.execute(excu)

                  temp_list = cursor.fetchall()
                  if temp_list:
                      flag_find = 1
                      msgname = signal
                      break
                  else:
                        pass

        if flag_find:
            return (tablename,msgname)
        else:
            return (None, None)

        cursor.close()
        conn.close()

    
          

    def data_repalce(self,blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,listmessagebox,flgerror):
        #print len(data_val_list)
        for n in range(len(data_val_list)):
            data_val=data_val_list[n][m]

            if data_val.find('s')!=-1:
                flag_save=1
            else:
                flag_save=0
                
            
            if data_val.strip()=='':
                pass
            else:
                if flag_chk==False:
                    if data_val in map_exl_enum_dict.keys():
                        data_val=str(map_exl_enum_dict[data_val])
                        data_val_list[n][m]=data_val
                    else:
                        data_val_list[n][m]=data_val

                elif flag_chk==True:

                    equ_pos=data_val.rfind('=')
                    great_pos=data_val.rfind('>')
                    lower_pos=data_val.rfind('<')
                    
                    if data_val in map_exl_enum_dict.keys():
                        data_val='value=='+str(map_exl_enum_dict[data_val])
                        data_val_list[n][m]=data_val
                    elif  self.is_number(data_val):
                        data_val='value=='+data_val
                        data_val_list[n][m]=data_val
                    elif 'value' in data_val:#expection have 'value'
                        if 'and' in data_val or 'or' in data_val:
                            pass
                            
                        elif equ_pos != -1:
                            data_val_num=data_val[equ_pos+1:]
                            if data_val_num in map_exl_enum_dict.keys():
                                data_val_num=map_exl_enum_dict[data_val_num]
                                data_val=data_val[:equ_pos+1]+str(data_val_num)
                                data_val_list[n][m]=data_val                                                        
                            elif self.is_number(data_val_num):
                                pass
                            elif flag_save==1:
                                pass
                            else:
                                print 'Case<%s> Block<%s> Colm%d Row %d donot have right value'%(name_temp,blockname,m,n)
                                messagebox='Case<'+str(name_temp)+'> Block<'+str(blockname)+'> Colm'+str(m)+' Row '+str(n)+' donot have right value'
                                listmessagebox.append(messagebox)
                    
                                flgerror=True
                                return None
                                #sys.exit()

                        elif great_pos != -1:
                            data_val_num=data_val[great_pos+1:]
                            if data_val_num in map_exl_enum_dict.keys():
                                data_val_num=map_exl_enum_dict[data_val_num]
                                data_val=data_val[:great_pos+1]+str(data_val_num)
                                data_val_list[n][m]=data_val                                                        
                            elif self.is_number(data_val_num):
                                pass
                            elif flag_save==1:
                                pass
                            else:
                                print 'Case<%s> Block<%s> Colm%d Row %d donot have right value'%(name_temp,blockname,m,n)
                                messagebox='Case<'+str(name_temp)+'> Block<'+str(blockname)+'> Colm'+str(m)+' Row '+str(n)+' donot have right value'
                                listmessagebox.append(messagebox)
                    
                                flgerror=True
                                return None
                                #sys.exit()

                        elif lower_pos != -1:
                            
                            data_val_num=data_val[lower_pos+1:]
                            if data_val_num in map_exl_enum_dict.keys():
                                data_val_num=map_exl_enum_dict[data_val_num]
                                data_val=data_val[lower_pos+1:]+str(data_val_num)
                                data_val_list[n][m]=data_val                                                        
                            elif self.is_number(data_val_num):
                                pass
                            elif flag_save==1:
                                pass
                            else:
                                print 'Case<%s> Block<%s> Colm%d Row %d donot have right value'%(name_temp,blockname,m,n)
                                messagebox='Case<'+str(name_temp)+'> Block<'+str(blockname)+'> Colm'+str(m)+' Row '+str(n)+' donot have right value'
                                listmessagebox.append(messagebox)
                    
                                flgerror=True
                                return None
                                #sys.exit()
                        else:
                            print 'Case<%s> Block<%s> Colm%d Row %d donot have right value'%(name_temp,blockname,m,n)
                            messagebox='Case<'+str(name_temp)+'> Block<'+str(blockname)+'> Colm'+str(m)+' Row '+str(n)+' donot have right value'
                            listmessagebox.append(messagebox)
                    
                            flgerror=True
                            return None
                            #sys.exit()

                    elif flag_save==1:
                        data_val_list[n][m]=data_val

                    else:
                        print 'Case<%s> Block<%s> Colm%d Row %d donot have right value'%(name_temp,blockname,m,n)
                        messagebox='Case<'+str(name_temp)+'> Block<'+str(blockname)+'> Colm'+str(m)+' Row '+str(n)+' donot have right value'
                        listmessagebox.append(messagebox)
                    
                        flgerror=True
                        return None
                        #sys.exit()
                else:
                    print 'Case<%s> Block<%s> Colm%d Row %d donot have right value'%(name_temp,blockname,m,n)
                    messagebox='Case<'+str(name_temp)+'> Block<'+str(blockname)+'> Colm'+str(m)+' Row '+str(n)+' donot have right value'
                    listmessagebox.append(messagebox)
                    
                    flgerror=True
                    return None
                    #sys.exit()
                

        return data_val_list

    def hexid(self,intid):
        a=int(intid)
        b=hex(a)
        c=str(b)
        d=c[2: ]
        return d

    def cal_check(self,map_exl_name,blockname,m,name_temp,data_val_list,
                  map_exl_enum_dict,flag_chk,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror):
        #cal_name_temp = CAL_name+map_exl_name
        #print cal_name_temp
        if map_exl_name in a2l_cal_dict.keys():
            flag_casetype = 1 #0:no cal&mea 1:cal&mea
            data_sig_list_temp = [map_exl_name,'Calibration']
            data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                     listmessagebox,flgerror)

        elif map_exl_name in a2l_mea_dict.keys():
            flag_casetype = 1 #0:no cal&mea 1:cal&mea
            data_sig_list_temp = [map_exl_name,'Measurement']
            data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                     listmessagebox,flgerror)
        else:
            print 'Please Check Type OR Cal&Mea of [%s] !'%(map_exl_name)
            messagebox='Please Check Type OR Cal&Mea of ['+str(map_exl_name)+']'
            listmessagebox.append(messagebox)            
            #flgerror=True
            return False,None,None,None

        return True,data_sig_list_temp,data_val_list_temp,flag_casetype        

    def can_check(self,HILname,modelname_ETAS,modelname_DSPACE,CAN_name,message_name,map_exl_name,map_dev,can_type,
                  blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,listmessagebox,flgerror):
        if HILname=='ETAS':
            can_prio_name_in=modelname_ETAS+CAN_name+'from'+can_type+'/'+message_name+'/'+map_exl_name+'_sub/Const/Value'#tx signal for write
            can_prio_name_inout=modelname_ETAS+CAN_name+'from'+can_type+'/'+message_name+'/'+map_exl_name+'_sub/Out1'#tx signal for read
            can_prio_name_out=modelname_ETAS+CAN_name+'to'+can_type+'/'+message_name+'/'+map_exl_name+'_Out/Out'#rx signal for read
            #print can_prio_name_in
            
            if flag_chk==True:
                if can_prio_name_inout in map_dev:
                    data_sig_final=can_prio_name_inout
                    

                    data_sig_list_temp=[data_sig_final]
                    data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                         listmessagebox,flgerror)
                    if data_val_list_temp == None:
                        return False,None,None
                elif can_prio_name_out in map_dev:
                    data_sig_final=can_prio_name_out
                    data_sig_list_temp=[data_sig_final]
                    data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                         listmessagebox,flgerror)

                    if data_val_list_temp == None:
                        return False,None,None

                else:
                    print 'Please Check Type OR ModelName of [%s] !'%(map_exl_name)
                    messagebox='Please Check Type OR ModelName of ['+str(map_exl_name)+'] !'
                    listmessagebox.append(messagebox)
                    
                    flgerror=True
                    return False,None,None
                    #sys.exit()
            else:
                if can_prio_name_in in map_dev:
                    can_prio_name_sw=modelname_ETAS+CAN_name+'from'+can_type+'/'+message_name+'/'+map_exl_name+'_sub/Const_SW/Value'

                    if can_prio_name_sw in map_dev:

                        data_sig_final=can_prio_name_in
                        data_sig_sw_final=can_prio_name_sw

                        data_sig_list_temp=[data_sig_final,data_sig_sw_final]
                        data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                             listmessagebox,flgerror)

                        if data_val_list_temp == None:
                            return False,None,None
                    else:
                        print 'Please Check [%s] in Model'%(can_prio_name_sw)
                        messagebox='Please Check ['+str(can_prio_name_sw)+'] in Model'
                        listmessagebox.append(messagebox)
                    
                        flgerror=True
                        return False,None,None
                        #sys.exit()
                else:
                    print 'Please Check Type OR ModelName of [%s] !'%(map_exl_name)
                    messagebox='Please Check Type OR ModelName of ['+str(map_exl_name)+'] !'
                    listmessagebox.append(messagebox)
                    
                    flgerror=True
                    return False,None,None
                    #sys.exit()
                
                    

                
        elif HILname=='DSPACE':
            
            can_prio_name_in=modelname_DSPACE+CAN_name+'from'+can_type+'/'+message_name+'/'+map_exl_name+'_sub/Const/Value'
            can_prio_name_inout=modelname_DSPACE+CAN_name+'from'+can_type+'/'+message_name+'/'+map_exl_name+'_sub/Out1'
            can_prio_name_out=modelname_DSPACE+CAN_name+'to'+can_type+'/'+message_name+'/'+map_exl_name+'_Out/Out1'

            if flag_chk==True:
                if can_prio_name_inout in map_dev:
                    data_sig_final=can_prio_name_inout
                    

                    data_sig_list_temp=[data_sig_final]
                    data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                         listmessagebox,flgerror)
                    if data_val_list_temp == None:
                        return False,None,None
                elif can_prio_name_out in map_dev:
                    data_sig_final=can_prio_name_out
                    data_sig_list_temp=[data_sig_final]
                    data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                         listmessagebox,flgerror)

                    if data_val_list_temp == None:
                        return False,None,None

                else:
                    print 'Please Check Type OR ModelName of [%s] !'%(map_exl_name)
                    messagebox='Please Check Type OR ModelName of ['+str(map_exl_name)+'] !'
                    listmessagebox.append(messagebox)
                    
                    flgerror=True
                    return False,None,None
                    #sys.exit()

            else:             
            
                if can_prio_name_in in map_dev:
                    can_prio_name_sw=modelname_DSPACE+CAN_name+'from'+can_type+'/'+message_name+'/'+map_exl_name+'_sub/Const_SW/Value'

                    if can_prio_name_sw in map_dev:

                        data_sig_final=can_prio_name_in
                        data_sig_sw_final=can_prio_name_sw

                        data_sig_list_temp=[data_sig_final,data_sig_sw_final]
                        data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                             listmessagebox,flgerror)

                        if data_val_list_temp == None:
                            return False,None,None
                    else:
                        print 'Please Check [%s] in Model'%(can_prio_name_sw)
                        messagebox='Please Check ['+str(can_prio_name_sw)+'] in Model'
                        listmessagebox.append(messagebox)
                    
                        flgerror=True
                        return False,None,None
                
                else:
                    print 'Please Check Type OR ModelName of [%s] !'%(map_exl_name)
                    messagebox='Please Check Type OR ModelName of ['+str(map_exl_name)+'] !'
                    listmessagebox.append(messagebox)
                    
                    flgerror=True
                    return False,None,None
                    #sys.exit()

        else:
            print 'Please Select HIL Type.... '
            messagebox='Please Select HIL Type.... '
            listmessagebox.append(messagebox)
                    
            flgerror=True
            return False,None,None
            #sys.exit()
        return True,data_sig_list_temp,data_val_list_temp
    def io_check(self,HILname,modelname_ETAS,modelname_DSPACE,IO_outname,IO_houzhui,map_exl_name,map_dev,
                 blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,listmessagebox,flgerror):
        data_sig_temp_out = IO_outname+map_exl_name+IO_houzhui
        #data_sig_temp_drive = IO_drivname+map_exl_name+'/Value'

        if HILname=='ETAS':
                    #data_sig_temp_in=modelname_ETAS+data_sig_temp_in
            data_sig_temp_out=modelname_ETAS+data_sig_temp_out
                    #data_sig_temp_drive=modelname_ETAS+data_sig_temp_drive
                
            if data_sig_temp_out in map_dev:#replace case value which is defind in map_excel
##                    data_sig_final='Plant model/'+data_sig_temp
                data_sig_final=data_sig_temp_out
                data_sig_list_temp=[data_sig_final]
                #data_sig_list_final.append(data_sig_final)

                data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                     listmessagebox,flgerror)

                if data_val_list_temp == None:
                    return False,None,None

            else:
                print 'Please Check Type OR ModelName of [%s] !'%(map_exl_name)
                messagebox='Please Check Type OR ModelName of ['+str(map_exl_name)+']'
                listmessagebox.append(messagebox)
            
                flgerror=True
                return False,None,None
                #sys.exit()
        elif HILname=='DSPACE':
            data_sig_temp_out=modelname_DSPACE+data_sig_temp_out
            #data_sig_temp_drive=modelname_DSPACE+data_sig_temp_drive
        
            
            if data_sig_temp_out in map_dev:#replace case value which is defind in map_excel
##                    data_sig_final='Plant model/'+data_sig_temp
                data_sig_final=data_sig_temp_out
                data_sig_list_temp=[data_sig_final]
                #data_sig_list_final.append(data_sig_final)

                data_val_list_temp=self.data_repalce(blockname,m,name_temp,data_val_list,map_exl_enum_dict,flag_chk,
                                                     listmessagebox,flgerror)

                if data_val_list_temp == None:
                    return False,None,None

            else:
                print 'Please Check Type OR ModelName of [%s] !'%(map_exl_name)

                messagebox='Please Check Type OR ModelName of ['+str(map_exl_name)+']'
                listmessagebox.append(messagebox)
            
                flgerror=True
                return False,None,None
                #sys.exit()

        else:
            print 'Please Select HIL Type.... '

            messagebox='Please Select HIL Type.... '
            listmessagebox.append(messagebox)
            
            flgerror=True
            return False,None,None
            #sys.exit()

        return True,data_sig_list_temp,data_val_list_temp
        

    def signal_check(self,blockname,m,name_temp,data_val_list,data_sig,map_exlin,map_exlout,map_dev,flag_chk,HILname,
                     a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror):

        #sig_dbcpos_info=self.list_postion(data_sig,1)#signal in DBC postion
        #print sig_dbcpos_info
        
        #io_prio_name='Geely_HiL_System/MDL/DriverInterface/'
        modelname_ETAS = 'Geely_HiL_System/'
        modelname_DSPACE = 'Model Root/'

        #IO_inname = 'MDL/DriverInterface/'
        IO_outname = 'IO/HardwareInterface/HWIN/'
        IO_outhouzhui='/Out1'
        IO_drivename = 'MDL/DriverInterface/'
        IO_drivehouzhui='/Value'
        CAN_name = 'IO/Protocols/'
        BUS_name = 'IO/Protocols/'
        #CAL_name = 'Powertrain/'
        map_exlin_enum_dict={}
        map_exlout_enum_dict={}

        flag_casetype = 0

        if flag_chk==True:

            if data_sig in map_exlout.keys():#find signal in map_excel
            
                map_exlout_sig=map_exlout[data_sig]
                map_exlout_type=map_exlout_sig[0][1]
                map_exlout_name=map_exlout_sig[0][0]
                map_exlout_enum_dict=map_exlout_sig[1]


                if map_exlout_type=='IO': #find signal type and name in model
                    reflag,data_sig_list_temp,data_val_list_temp=self.io_check(HILname,modelname_ETAS,modelname_DSPACE,IO_outname,IO_outhouzhui,
                                                                        map_exlout_name,map_dev,blockname,m,name_temp,data_val_list,map_exlout_enum_dict,flag_chk,listmessagebox,flgerror) 

                    if reflag == False:
                        return False,None,None,None
                        
                    #return True data_sig_list_temp,data_val_list_temp 

                elif map_exlout_type=='CLN': #find signal type and name in model
                    dbc_pos_info=self.list_postion(map_exlout_name,1)
                    if dbc_pos_info:
                        if dbc_pos_info[0]:
                            can_type = dbc_pos_info[0]
                            message_name = dbc_pos_info[1]

                            reflag,data_sig_list_temp,data_val_list_temp=self.can_check(HILname,modelname_ETAS,modelname_DSPACE,CAN_name,message_name,
                                                                                 map_exlout_name,map_dev,can_type,blockname,m,name_temp,data_val_list,map_exlout_enum_dict,flag_chk,listmessagebox,flgerror)
                            
                            if reflag == False:
                                return False,None,None,None
                            #return True data_sig_list_temp,data_val_list_temp         
                        
                        else:
                            print map_exlout_name+' cannot find in dbc&ldf'
                            messagebox = map_exlout_name+' cannot find in dbc&ldf'
                            listmessagebox.append(messagebox)
                        
                            flgerror=True
                            return False,None,None,None                           
                            #sys.exit()
                    else:
                        print 'Signal<%s> of Case<%s> cannot find in dbc'%(map_exl_name,name_temp)
                        #ui_MainCreate.Ui_MainCreateMw.textBrowser.append('aaaaaaaa')
                        messagebox='Signal<'+str(map_exl_name)+'> of Case<'+str(name_temp)+'> cannot find in dbc&ldf'
                        listmessagebox.append(messagebox)
                        
                        flgerror=True
                        return False,None,None,None
                        #sys.exit()
                elif map_exlout_type=='CAL':
                    #print 'aaa'
                    reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.cal_check(map_exlout_name,blockname,m,name_temp,data_val_list,
                                                                                map_exlout_enum_dict,flag_chk,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror) 

                    if reflag == False:
                        return False,None,None,None     

                else:
                    print 'Signal<%s> of Case<%s> have  wrong type'%(map_exlout_name,name_temp)
                            #ui_MainCreate.Ui_MainCreateMw.textBrowser.append('aaaaaaaa')

                    messagebox='Signal<'+str(map_exlout_name)+'> of Case<'+str(name_temp)+'> have  wrong type'
                    listmessagebox.append(messagebox)
                        
                    flgerror=True
                    return False,None,None,None

            else:
                print data_sig+' cannot find in out map'
                messagebox=str(data_sig)+' cannot find in out map'
                listmessagebox.append(messagebox)
                        
                flgerror=True
                return False,None,None,None

        elif flag_chk==False:

            if data_sig in map_exlin.keys():#find signal in map_excel
            
                map_exlin_sig=map_exlin[data_sig]
                map_exlin_type=map_exlin_sig[0][1]
                map_exlin_name=map_exlin_sig[0][0]
                map_exlin_enum_dict=map_exlin_sig[1]
                #print map_exlin_type

                if map_exlin_type=='IO': #find signal type and name in model
                    #print 'ioioio'
                    reflag,data_sig_list_temp,data_val_list_temp=self.io_check(HILname,modelname_ETAS,modelname_DSPACE,IO_drivename,IO_drivehouzhui,
                                                                        map_exlin_name,map_dev,blockname,m,name_temp,data_val_list,map_exlin_enum_dict,flag_chk,listmessagebox,flgerror) 
                    if reflag ==False:
                        return False,None,None,None
                    #return True,data_sig_list_temp,data_val_list_temp 

                elif map_exlin_type=='CLN': #find signal type and name in model
                    #print 'clnclncl'
                    dbc_pos_info=self.list_postion(map_exlin_name,1)
                    if dbc_pos_info:
                        if dbc_pos_info[0]:
                            can_type=dbc_pos_info[0]
                            message_name=dbc_pos_info[1]

                            reflag,data_sig_list_temp,data_val_list_temp=self.can_check(HILname,modelname_ETAS,modelname_DSPACE,CAN_name,message_name,
                                                                                 map_exlin_name,map_dev,can_type,blockname,m,name_temp,data_val_list,map_exlin_enum_dict,flag_chk,listmessagebox,flgerror)
                            if reflag == False:
                                return False,None,None,None
                            #return True,data_sig_list_temp,data_val_list_temp                                     
                         
                        else:
                            print map_exlin_name+' cannot find in dbc&ldf'
                            messagebox=str(map_exlin_name)+' cannot find in dbc&ldf'
                            listmessagebox.append(messagebox)
                        
                            flgerror=True
                            return False,None,None,None
                            
                            #sys.exit()
                    else:
                        print 'Signal<%s> of Case<%s> cannot find in dbc$ldf'%(map_exlin_name,name_temp)
                        #ui_MainCreate.Ui_MainCreateMw.textBrowser.append('aaaaaaaa')
                        messagebox='Signal<'+str(map_exlin_name)+'> of Case<'+str(name_temp)+'> cannot find in dbc&ldf'
                        listmessagebox.append(messagebox)
                        
                        flgerror=True
                        return False,None,None,None
                        #sys.exit()                                  
                   
                elif map_exlin_type=='BUS': #find signal type and name in model
                    #print 'busbus'
                    dbc_pos_info=self.list_postion(map_exlin_name,0)
                    if dbc_pos_info[0]:
    ##                    pos_temp=can.Chassisbus.getinfo.messagename.index(map_exl_name)
    ##                    canname_temp=can.Chassisbus.getinfo.canname[pos_temp]
    ##                    msgID=can.Chassisbus.getinfo.messageid[pos_temp]
    ##                    msgID_temp=self.hexid(msgID)
    ##                    
    ##                    bus_prio_name='CANModule/ChassisCAN/'+canname_temp+'/'+msgID_temp+'std_'+map_exl_name+'/ManualEnabled'
                        if HILname=='ETAS':
                            bus_prio_name = modelname_ETAS+BUS_name+'En'+dbc_pos_info[0]+'/'+map_exlin_name+'_enable/Value'

                            if bus_prio_name in map_dev:#replace case value which is defind in map_excel##                    
                                data_sig_temp=bus_prio_name
                                data_sig_final=data_sig_temp
                                data_sig_list_temp=[data_sig_final]
                                data_val_list_temp=data_val_list

                                #return True,data_sig_list_temp,data_val_list_temp
                            else:
                                print 'Please check %s in Plant Model'%(bus_prio_name)
                                messagebox='Please check '+str(bus_prio_name)+' in Plant Model'
                                listmessagebox.append(messagebox)
                        
                                flgerror=True
                                return False,None,None,None
                                #sys.exit()

                        elif HILname=='DSPACE':
                            bus_prio_name = modelname_DSPACE+BUS_name+'En'+dbc_pos_info[0]+'/'+map_exlin_name+'_enable/Value'

                            if bus_prio_name in map_dev:#replace case value which is defind in map_excel##                    
                                data_sig_temp=bus_prio_name
                                data_sig_final=data_sig_temp
                                data_sig_list_temp=[data_sig_final]
                                data_val_list_temp=data_val_list

                                #return True,data_sig_list_temp,data_val_list_temp
                            else:
                                print 'Please check %s in Plant Model'%(bus_prio_name)

                                messagebox='Please check '+str(bus_prio_name)+' in Plant Model'
                                listmessagebox.append(messagebox)
                        
                                flgerror=True
                                return False,None,None,None
                                #sys.exit()

                        else:
                            print 'Please Select HIL Type.... '
                            messagebox='Please Select HIL Type.... '
                            listmessagebox.append(messagebox)
                        
                            flgerror=True
                            return False,None,None,None
                            #sys.exit()

                    
                        
                    else:
                        
                        print 'Signal<%s_ManualEnabled> of Case<%s> cannot find in dbc&ldf'%(map_exlin_name,name_temp)
                        #ui_MainCreate.Ui_MainCreateMw.textBrowser.append('aaaaaaaa')

                        messagebox='Signal<'+str(map_exlin_name)+'_ManualEnabled> of Case<'+str(name_temp)+'> cannot find in dbc&ldf'
                        listmessagebox.append(messagebox)
                        
                        flgerror=True
                        return False,None,None,None

                
                elif map_exlin_type=='CAL':
                    #print 'aaa'
                    reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.cal_check(map_exlin_name,blockname,m,name_temp,data_val_list,
                                                                                map_exlin_enum_dict,flag_chk,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror) 

                    if reflag == False:
                        return False,None,None,None

                else:
                    #print 'elsels'
                    print 'Signal<%s> of Case<%s> have  wrong type'%(map_exlin_name,name_temp)
                            #ui_MainCreate.Ui_MainCreateMw.textBrowser.append('aaaaaaaa')

                    messagebox='Signal<'+str(map_exlin_name)+'> of Case<'+str(name_temp)+'> have  wrong type'
                    listmessagebox.append(messagebox)
                    #print 'qqqqqq'    
                    flgerror=True
                    return False,None,None,None
                
            else:
                print data_sig+' cannot find in inmap'
                messagebox=data_sig+' cannot find in inmap'
                listmessagebox.append(messagebox)
                        
                flgerror=True
                return False,None,None,None
                

        else:
            print 'Check Flag have no value!'                
            listmessagebox.append('Check Flag have no value!')
                        
            flgerror=True
            return False,None,None,None

        #return data_sig_list_temp,data_val_list_temp
        return True,data_sig_list_temp,data_val_list_temp,flag_casetype
    
         
    def check_map(self,case_dict,HILname,usermapfpath,modelmapfpath,a2lpath,listmessagebox,flgerror):
        
        #testcase=test_case_prepare()  #excel data
        #testcase_excute=testcase_excute()#one defined can excute
        
        #HILname='DSPACE'

        #map_exl=map_read('E:\\temp\\py\\autotest_ecutest4.5\\map.xls')   #read excel map which we build!!!!temporary
        #print 'HIL Name is '+HILname
        listmessagebox.append('HIL Name is '+str(HILname))

        map_exlin,map_exlout = map_read(usermapfpath,listmessagebox,flgerror)
        #print 'aaaaa'
        map_dev=self.create_maplist(HILname,modelmapfpath,listmessagebox,flgerror)                                         #read device map which device build!!!!!
        #print 'bbbb'
        if map_dev !=None:
            map_dev=unicode(map_dev)

        a2l_mea_dict,a2l_cal_dict = a2l_read(a2lpath,listmessagebox)        
        #print 'ccccc'
        
        list_casedict_key=list(case_dict.keys())
        #print list_casedict_key
        #print len(list_casedict_key)
        for filenum in range(len(list_casedict_key)):
            
            case_list=case_dict[list_casedict_key[filenum]]
        

            #predata = testcase.xlsinfo.testinfo.preinfo.pre_data
            casename=case_list[0]
            casetype_list=len(casename)*[0]#casetype_list: judge have cal&mea or not
            
            predata=case_list[1]
            prechk = case_list[2]
            casedata = case_list[5]
            casechk = case_list[6]
            #print casechk
            posdata = case_list[9]
            poschk = case_list[10]
            #print poschk
            
    ##        case_step_list=[]
    ##
    ##        for loopnum in range(len(testcase.casename)):      
    ######pre_data check_rw#############

            print 'Precondition is checked...'
            listmessagebox.append('Precondition is checked...')
            blockname='PreData'
            
            for i in range(len(predata)):

                name_temp=casename[i]
                data_list=predata[i]
                #data_list_final=[]
                data_sig_list=data_list[0] #signal names in every case
                #data_sig_list_final=[]
                data_val_list=data_list[1] #values acorrding to signal name in every case
                #data_val_list_final=[]
                
                flag_chk=False
                
                for m in range(len(data_sig_list)):
                    
                    data_sig=data_sig_list[m]
                    
                    
                    if data_sig:

                        reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.signal_check(blockname,m,name_temp,data_val_list,data_sig,map_exlin,
                                                                                map_exlout,map_dev,flag_chk,HILname,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror)

                    if reflag == True:   
                        data_sig_list[m]=data_sig_list_temp
                        data_val_list=data_val_list_temp
                        if casetype_list[i] == 0:
                            casetype_list[i]= flag_casetype
                            
                    else:
                        return None
                           


                data_list[0]=data_sig_list
                data_list[1]=data_val_list
                predata[i]=data_list
                #predata_final.append(data_list)
                #print data_list

                #print predata

            #testcase.xlsinfo.testinfo.preinfo.pre_data =  predata
            #return predata
    ######pre_chk check_rw#############

            print 'Precondition check is checked...'
            listmessagebox.append('Precondition check is checked...')
            blockname='PreCheck'
            for i in range(len(prechk)):
                name_temp=casename[i]
                data_list=prechk[i]
                #data_list_final=[]
                data_sig_list=data_list[0] #signal names in every case
                #data_sig_list_final=[]
                data_val_list=data_list[1] #values acorrding to signal name in every case
                #data_val_list_final=[]

                flag_chk=True
                
                for m in range(len(data_sig_list)):
                    
                    data_sig=data_sig_list[m]
                    
                    
                    if data_sig:

                        reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.signal_check(blockname,m,name_temp,data_val_list,data_sig,map_exlin,
                                                                                map_exlout,map_dev,flag_chk,HILname,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror)

                    
                    if reflag == True:   
                        data_sig_list[m]=data_sig_list_temp
                        data_val_list=data_val_list_temp
                        if casetype_list[i] == 0:
                            casetype_list[i]= flag_casetype
                    else:
                        return None

                data_list[0]=data_sig_list
                data_list[1]=data_val_list
                prechk[i]=data_list


            #return prechk

    ######case_data check_rw#############

            print 'Action is checked...'
            listmessagebox.append('Action is checked...')
            blockname='ActionData'
            #print len(casedata)
            for i in range(len(casedata)):
                name_temp=casename[i]
                data_list=casedata[i]
                #data_list_final=[]
                data_sig_list=data_list[0] #signal names in every case
                #data_sig_list_final=[]
                data_val_list=data_list[1] #values acorrding to signal name in every case
                #data_val_list_final=[]

                flag_chk=False
                #print 'aaaa'
                
                for m in range(len(data_sig_list)):
                    
                    data_sig=data_sig_list[m]                    
                    
                    if data_sig:
                        #print 'datasignal is '+str(data_sig)

                        reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.signal_check(blockname,m,name_temp,data_val_list,data_sig,map_exlin,
                                                                                map_exlout,map_dev,flag_chk,HILname,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror)
                        #print reflag
                    
                    if reflag == True:   
                        data_sig_list[m]=data_sig_list_temp
                        data_val_list=data_val_list_temp
                        if casetype_list[i] == 0:
                            casetype_list[i]= flag_casetype
                    else:
                        return None
                    
                data_list[0]=data_sig_list
                data_list[1]=data_val_list
                casedata[i]=data_list

            #return casedata


    ######case_chk check_rw#############

            print 'Action check is checked...'
            listmessagebox.append('Action check is checked...')
            blockname='ActionCheck'
            for i in range(len(casechk)):
                name_temp=casename[i]
                data_list=casechk[i]
                #data_list_final=[]
                data_sig_list=data_list[0] #signal names in every case
                #data_sig_list_final=[]
                data_val_list=data_list[1] #values acorrding to signal name in every case
                #data_val_list_final=[]
    ##            print data_val_list

                flag_chk=True
                
                for m in range(len(data_sig_list)):
                    
                    data_sig=data_sig_list[m]
                    
                    #print 'datasignal is '+str(data_sig)
                    if data_sig:

                        reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.signal_check(blockname,m,name_temp,data_val_list,data_sig,map_exlin,
                                                                                map_exlout,map_dev,flag_chk,HILname,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror)

                    
                    if reflag == True:   
                        data_sig_list[m]=data_sig_list_temp
                        data_val_list=data_val_list_temp
                        if casetype_list[i] == 0:
                            casetype_list[i]= flag_casetype
                    else:
                        return None

                data_list[0]=data_sig_list
                data_list[1]=data_val_list
                casechk[i]=data_list


            #return prechk
                
    ######pos_data check_rw#############

            print 'Poscondition is checked...'
            listmessagebox.append('Poscondition is checked...')
            blockname='PosData'
            for i in range(len(posdata)):
                name_temp=casename[i]
                data_list=posdata[i]
                #data_list_final=[]
                data_sig_list=data_list[0] #signal names in every case
                #data_sig_list_final=[]
                data_val_list=data_list[1] #values acorrding to signal name in every case
                #data_val_list_final=[]

                flag_chk=False
                
                for m in range(len(data_sig_list)):
                    
                    data_sig=data_sig_list[m]
                    
                    
                    if data_sig:

                        reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.signal_check(blockname,m,name_temp,data_val_list,data_sig,map_exlin,
                                                                                map_exlout,map_dev,flag_chk,HILname,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror)

                    
                    if reflag == True:   
                        data_sig_list[m]=data_sig_list_temp
                        data_val_list=data_val_list_temp
                        if casetype_list[i] == 0:
                            casetype_list[i]= flag_casetype
                    else:
                        return None
                    
                data_list[0]=data_sig_list
                data_list[1]=data_val_list
                posdata[i]=data_list

            #return posdata


    ######pos_chk check_rw#############

            print 'Poscondition check is checked...'
            listmessagebox.append('Poscondition check is checked...')
            blockname='PosCheck'
            #print len(poschk)
            for i in range(len(poschk)):
                
                name_temp=casename[i]
                data_list=poschk[i]
                #data_list_final=[]
                data_sig_list=data_list[0] #signal names in every case
                #data_sig_list_final=[]
                data_val_list=data_list[1] #values acorrding to signal name in every case
                #data_val_list_final=[]

                flag_chk=True
                #print len(data_sig_list)
                for m in range(len(data_sig_list)):
                    
                    data_sig=data_sig_list[m]
                    print 'datasignal is '+str(data_sig)                   
                    
                    if data_sig:

                        reflag,data_sig_list_temp,data_val_list_temp,flag_casetype=self.signal_check(blockname,m,name_temp,data_val_list,data_sig,map_exlin,
                                                                                map_exlout,map_dev,flag_chk,HILname,a2l_cal_dict,a2l_mea_dict,listmessagebox,flgerror)

                    
                    if reflag == True:   
                        data_sig_list[m]=data_sig_list_temp
                        data_val_list=data_val_list_temp
                        if casetype_list[i] == 0:
                            casetype_list[i]= flag_casetype
                    else:
                        return None
                           


                data_list[0]=data_sig_list
                data_list[1]=data_val_list
                poschk[i]=data_list

            for num in  range(len(casename)):
                casename[num]=[casename[num],casetype_list[num]]

            case_list[0]=casename
            case_list[1]=predata
            case_list[2]=prechk
            case_list[5]=casedata
            case_list[6]=casechk
            case_list[9]=posdata
            case_list[10]=poschk

            case_dict[list_casedict_key[filenum]]=case_list

        #print case_dict.keys()
        return case_dict

            
        #return prechk


        #return predata,prechk,casedata,casechk,posdata,poschk
    
       
if __name__=='__main__':


    import window_f
    from PakgCreate import *
    
    testinfo=window_f.test_info()
    oldpath=os.getcwd()
    filepath=testinfo.select_dir('testcase')
    casepath = filepath
    os.chdir(filepath)
    filelist = os.listdir(os.getcwd())
    os.chdir(oldpath)
##    
    listmessagebox = []
    flgerror = False

    progressvalue=[]
    
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


##    oldpath=os.getcwd()
##    filepath=testinfo.select_dir('DBC')
##    os.chdir(filepath)
##    filelist = os.listdir(os.getcwd())
##    
####    
##    
##    #testcase=test_case_prepare()
##    filetype='.dbc'    
##    filelist_DBC=testcase.filter_file(filelist,filetype)
##    
##
##    
##    print filelist_DBC
##
##    can_info=dbc_info_get()
##    can=can_info.dbc_read(filelist_DBC)
##
##    os.chdir(oldpath)

    HILname = 'DSPACE'
    usermapfpath = 'E:\\temp\\py\\GUI\\autotest_ecutest4.5_temp\\map.xls'
    modelmapfpath = 'E:\\temp\\py\\GUI\\autotest_ecutest4.5_temp\\maplist.txt'
    a2lpath = 'E:\\temp\\py\\GUI\\autotest_ecutest4.5_temp\\KL0104AC00-L39355.a2l'
    
    check=Check_rw()
    #prechk=check.check_map(testcase,can)
    case_dict=check.check_map(case_dict,HILname,usermapfpath,modelmapfpath,a2lpath,listmessagebox,flgerror)
    pkgcreat=PkgCreate()
    reflag=pkgcreat.PakgCreate(casepath,case_dict,HILname,progressvalue,listmessagebox,flgerror)
    #print case_dict
##    print predata
##    print prechk
##    print casedata
##    print casechk
##    print posdata
##    print poschk
