import os
import ComandMenuBuilder as CMB
#File Management
def Load(path):
    data = []
    for x in open(path,'r'):
        x = x.replace('\n','')
        if x != '':
            data.append(x)
    return data
def Save(path,Data):
    TempFile = open(path,'w')
    for x in Data:
        TempFile.write(str(x)+'\n')
    TempFile.close()
def CreateSaveFile(path):
    base_file_format = []
    sort_paths = []
    #load data into paths
    open(path,"x")
    sort_paths = CMB.EditArray(array=sort_paths,title='Add_paths',info='Add path you want to sort like: C:\\Users\\user\\Downloads').Menu()
    base_file_format = CMB.EditArray(array= base_file_format,title= 'Add_file_extension',info='Add file Types you want to sort like: pdf,png and so on').Menu()
    sort_paths = CheckValidPath(sort_paths)
    #Create data list for saving
    data = []
    data.extend(sort_paths)
    data.extend(base_file_format)
    Save(path,data)
def CheckValidPath(paths):
    valid_paths = []
    for x in paths:
        if os.path.exists(x):
            valid_paths.append(x)
    return valid_paths
#Array Management
def RemoveArrayElement(array,element):
    new_array = []
    for x in array:
        if not x == element:
            new_array.append(x)
    return new_array
def AvoidDoubleElements(array,element):
    for x in array:
        if x == element:
            return array
    array.append(element)
    return array