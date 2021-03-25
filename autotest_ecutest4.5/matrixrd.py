# -*- coding: utf-8 -*-
import sqlite3,os,time

class MatrixInfo:
      def CanMatrixDb(self,dbclist,listmessageboxfile,listmessageboxinsert):
            nodname=''
            msgname=''
            msgid=''
            signame=''

            try:
                  filecan = open('CanType.ini')
                  cantype_list = filecan.readlines()
                  for num in range(len(cantype_list)):
                        cantype_list[num] = cantype_list[num].replace('\n','')

                  print cantype_list
                  #listmessageboxfile.append(cantype_list)

                  #tablecan_list = []
                  #tablelin_list = []

                  if len(dbclist)==0:                  
                        print 'There is no Matrix file, Please check ......'
                        messagebox = 'There is no Matrix file, Please check ......'
                        listmessageboxinsert.append(messagebox)
                        return None
                  else:
                        npath=os.getcwd()
                        if os.path.exists(npath+'\\Matrix.db'):
                              os.remove(npath+'\\Matrix.db')

                        conn = sqlite3.connect(npath+'\\Matrix.db')
                        cursor = conn.cursor()                  

                        for dbcnum in range(len(dbclist)):                      
                              
                              dbc_file_name = dbclist[dbcnum]
                              templist = dbclist[dbcnum].split(".")
                              #print templist

                              

                              if templist[-1] == 'dbc':

                                    for cantype in cantype_list:
                                          if cantype in dbc_file_name:
                                                tablcanname = cantype
                                                print tablcanname
                                                listmessageboxfile.append(tablcanname)
                                                
                                                break
                                          else:
                                                tablcanname = 'CAN_'+str(dbcnum)

                                    #tablcanname = 'CAN_'+str(dbcnum)
                                    #tablecan_list.append(tablcanname)
                                    excu = 'create TABLE '+tablcanname+' (nodename TEXT NOT NULL,messagename TEXT NOT NULL,'+\
                                     'messageid TEXT NOT NULL,signalname TEXT NOT NULL,CONSTRAINT xh primary key(signalname))'
                                    print excu
                                    listmessageboxfile.append(excu)
                                    cursor.execute(excu)                             
                              
                                    dbc_content=open(dbc_file_name,'r')            
                                    row_content_by_lines = dbc_content.readlines()
                                    listnum=0

                                    while  listnum != len(row_content_by_lines)-1:
                                          line=row_content_by_lines[listnum]
                                          if line.find('BO_')==0:
                                              line_temp_list=line.split()
                                              msgname=line_temp_list[2].strip(':')
                                              msgid=hex(int(line_temp_list[1]))
                                              nodname=line_temp_list[4].strip('\n')
                                              listnum=listnum+1
                                              line=row_content_by_lines[listnum]
                                              #signal_list=[]

                                              while line.find(' SG_')==0:
                                                  signame = line[5:line.index(':')-1]
                                                  list_wrtdb=[nodname,msgname,msgid,signame]
                                                  excu = self.InsertDb(tablcanname,list_wrtdb)
                                                  print excu
                                                  listmessageboxinsert.append(excu)
                                                  cursor.execute(excu)
                                                  conn.commit()
                                                  time.sleep(0.5)
                                                  listnum=listnum+1
                                                  line=row_content_by_lines[listnum]

                                          else:
                                                listnum=listnum+1
                              elif templist[-1] == 'ldf':

                                    for cantype in cantype_list:
                                          if cantype in dbc_file_name:
                                                tablinname = cantype
                                                print tablinname
                                                listmessageboxfile.append(tablinname)                                                
                                                break
                                          else:
                                                tablinname = 'LIN_'+str(dbcnum)

                                    #tablinname = 'LIN_'+str(dbcnum)
                                    #tablelin_list.append(tablinname)
                                    excu = 'create TABLE '+tablinname+' (messagename TEXT NOT NULL,signalname TEXT NOT NULL,CONSTRAINT xh primary key(signalname))'
                                    print excu
                                    listmessageboxfile.append(excu)
                                    cursor.execute(excu)

                                    dbc_content=open(dbc_file_name,'r')            
                                    row_content_by_lines = dbc_content.readlines()
                                    listnum=0
                                    
                                    flag_strart=0
                                    while  listnum != len(row_content_by_lines)-1:
                                          line=row_content_by_lines[listnum]                              

                                          if line.find('Frames')==0:
                                              flag_strart=1
                                              
                                          if flag_strart==1:                        
                                              listnum=listnum+1
                                              line=row_content_by_lines[listnum]
                                              
                                              if line.find('}')!=-1:
                                                  flag_strart=0
                                              elif line.find(':') and line.find('{'):
                                                  line_temp_list=line.split()
                                                  msgname=line_temp_list[0].strip(':')
                                                  #print message_name
                                                  listnum=listnum+1
                                                  line=row_content_by_lines[listnum]
                                                  signal_list=[]

                                                  while line.find('}')==-1:
                                                      signame = line[4:line.index(',')]

                                                      list_wrtdb=[msgname,signame]
                                                      excu = self.InsertDb(tablinname,list_wrtdb)
                                                      print excu
                                                      listmessageboxinsert.append(excu)
                                                      cursor.execute(excu)
                                                      conn.commit()
                                                      time.sleep(0.5)
                                                      
                                                      listnum=listnum+1
                                                      line=row_content_by_lines[listnum]
                                          else:
                                              listnum=listnum+1

                              else:
                                    print dbc_file_name+' is wrong !!!'
                                    messagebox = dbc_file_name+' is wrong !!!'
                                    listmessageboxinsert.append(messagebox)

                        cursor.close()
                        conn.close()
                        #return (tablecan_list,tablelin_list)
                        return True
            except:
                  return False


      def InsertDb(self,tablname,insert_list):

            reinsert = 'INSERT INTO '+tablname+' VALUES('
            for num in range(len(insert_list)):
                  if num == 0:
                        reinsert = reinsert+"'"+str(insert_list[num])+"'"
                  else:
                        reinsert = reinsert+','+"'"+str(insert_list[num])+"'"

            reinsert = reinsert+')'
            return reinsert

if __name__=='__main__':
      dbclist=['E:\\testcase\\DBC\\1.9\\KC-2HB ECU DBC V1.9_VCU_PTCAN_20171031_release.dbc','E:\\testcase\\DBC\\1.9\\KC-2HB(7DCTH) ECU DBC V1.9.2_VCU_HybridCAN_20180523_release.dbc','E:\\testcase\\DBC\\1.9\\KC-2 LIN4 LDF_V1.7_20170410_Release.ldf']
      listmessagebox=[]
      dbcrd = MatrixInfo()
      dbcrd.CanMatrixDb(dbclist,listmessagebox)
      
      
