# -*- coding: utf-8 -*-
import os,sys
import xlrd

def map_read(filepath,listmessagebox,error):
    wk = xlrd.open_workbook(filepath)
    sheetin = wk.sheet_by_index(0)

    sheetout = wk.sheet_by_index(1)

    map_read_dictin = map_dict_create(sheetin,listmessagebox,error)
    map_read_dictout = map_dict_create(sheetout,listmessagebox,error)

    return map_read_dictin,map_read_dictout
    
##    sheet.merged_cells

def map_dict_create(sheet,listmessagebox,error):
    
    row_num=sheet.nrows
    map_read_dict={}
    loopnum=1

    row_read_temp=[]
    row_enum_temp={}
    
    
    while loopnum < row_num:
        
        rowvalue=sheet.row_values(loopnum)
        #print rowvalue
        if rowvalue[0]=='' and rowvalue[3]=='':
           print 'space'
           listmessagebox.append('sapce')
           error=True
           return
           #sys.exit()
        
        elif rowvalue[0] != '':
            if row_read_temp != [] :
                row_read_temp.append(row_enum_temp)
                map_read_dict[row_read_temp1]=row_read_temp
                row_read_temp=[]
                row_enum_temp={}

                row_read_temp1=rowvalue[0]
                row_read_temp.append((rowvalue[1],rowvalue[2]))
                row_enum_temp[rowvalue[3]]=rowvalue[4]
                loopnum+=1
                
            else:            
                row_read_temp1=rowvalue[0]
                row_read_temp.append((rowvalue[1],rowvalue[2]))
                row_enum_temp[rowvalue[3]]=rowvalue[4]
                loopnum+=1
        else:
            row_enum_temp[rowvalue[3]]=rowvalue[4]
            loopnum+=1
            
    return map_read_dict

if __name__=='__main__':
    listmessagebox=[]
    error=False
    map_read_dictin,map_read_dictout=map_read('E:\\temp\\py\\GUI\\autotest_ecutest4.5\\usermap.xls',listmessagebox,error)
    #print map_read_list[0]
    #print map_read_list[1]
    
        
            
            
            
            
            
        
        
