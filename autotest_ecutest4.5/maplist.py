f=open('E:\\temp\\py\\autotest_ecutest4.3_temp\\MappingFile4.txt')
map_file=f.readlines()
map_list=[]
for map_file_every in map_file:
    map_file_temp = map_file_every.split('=')
    if len(map_file_temp)==2:
        map_list.append(map_file_temp[1].strip())
