# -*- coding: utf-8 -*-
import os,sys
import window_f


##class a2l_info:
##    def __init__(self):
##        self.a2l_measurement=dict()
####        self.a2l_mename = []        #measurement variable name
####        self.a2l_metype = []        #measurement variable type
####        self.a2l_mead = []          #measurement variable address
##        self.a2l_calibration=dict()
####        self.a2l_caname=[]          #calibration variable name
####        self.a2l_catype = []        #calibration variable type
####        self.a2l_caad = []          #calibration variable address
##        self.a2l_carecname=[]       #calibration variable record name
##        self.a2l_carectype=[]       #calibration variable record type        

def a2l_read(a2lpath,listmessagebox):

    a2l_measurement=dict()
    a2l_calibration=dict()
    a2l_carecname=[]
    a2l_carectype=[]

    #a2l_detail=a2l_info()
    
    #testinfo=window_f.test_info()
    #oldpath=os.getcwd()
    #a2lpath=testinfo.select_file('A2L','a2l')

    if a2lpath!='':
        pass
    else:
        print 'No a2l choice'
        sys.exit()   
        
    try:
        dbc_content=open(a2lpath,'r')            
        row_content_by_lines = dbc_content.readlines()
        listnum=0        

        while  listnum != len(row_content_by_lines)-1:
            line=row_content_by_lines[listnum]
            if line.find('    /begin MEASUREMENT')==0:
                
                line_temp_list=line.split()
                a2l_mename_temp=line_temp_list[2].strip()
                listnum=listnum+1

                line_next=row_content_by_lines[listnum]
                line_next_temp_list=line_next.split()
                a2l_metype_temp=line_next_temp_list[0].strip()
                listnum=listnum+1

                line_next=row_content_by_lines[listnum]
                line_next_temp_list=line_next.split()
                a2l_mead_temp=line_next_temp_list[1].strip()
                listnum=listnum+1
                
                a2l_measurement[a2l_mename_temp]={'type':a2l_metype_temp,'address':a2l_mead_temp}
##                a2l_detail.a2l_mename.append(a2l_mename_temp)
##                a2l_detail.a2l_metype.append(a2l_metype_temp)
##                a2l_detail.a2l_mead.append(a2l_mead_temp)
            elif line.find('    /begin CHARACTERISTIC')==0:
                line_temp_list=line.split()
                a2l_caname_temp=line_temp_list[2].strip()
                listnum=listnum+1

                line_next=row_content_by_lines[listnum]
                line_next_temp_list=line_next.split()
                a2l_catype_temp=line_next_temp_list[2].strip()
                a2l_caad_temp=line_next_temp_list[1].strip()
                listnum=listnum+1

                a2l_calibration[a2l_caname_temp]={'type':a2l_catype_temp,'address':a2l_caad_temp}
##                a2l_detail.a2l_caname.append(a2l_caname_temp)
##                a2l_detail.a2l_catype.append(a2l_catype_temp)
##                a2l_detail.a2l_caad.append(a2l_caad_temp)
            elif line.find('    /begin RECORD_LAYOUT')==0:
                line_temp_list=line.split()
                a2l_carename_temp=line_temp_list[2].strip()
                listnum=listnum+1

                line_next=row_content_by_lines[listnum]
                line_next_temp_list=line_next.split()
                a2l_caretype_temp=line_next_temp_list[2].strip()
                listnum=listnum+1

                a2l_carecname.append(a2l_carename_temp)
                a2l_carectype.append(a2l_caretype_temp)
                
            else:
                listnum=listnum+1

        for var in a2l_calibration.keys():
            
          for n in range(len(a2l_carecname)):
              if a2l_calibration[var]['type']==a2l_carecname[n]:
                  a2l_calibration[var]['type']=a2l_carectype[n]
                  break                      
                  
    except:
        print 'There is some wrong'
        sys.exit()
            
            
    return a2l_measurement,a2l_calibration

if __name__=='__main__':
    listmessagebox=[]
   
    can1,can2=a2l_read('E:\\VCUsofeware\\39355\\KL0104AC00-L39355.a2l',listmessagebox)
