import os
#import tkinter as tk
def Load(path):
    data = []
    for x in open(path,'r'):
        x = x.replace('\n','')
        if x != '':
            data.append(x)
    return data
def CreateSaveFile(path):
    base_file_format = []
    sort_paths = []
    #load data into paths
    open(path,"x")
    sort_paths = EditArray(sort_paths,'Add_paths','Add path you want to sort like: C:\\Users\\user\\Downloads')
    base_file_format = EditArray(base_file_format,'Add_file_extension',info='Add file Types you want to sort like: pdf,png and so on')
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

def Save(path,Data):
    TempFile = open(path,'w')
    for x in Data:
        TempFile.write(str(x)+'\n')
    TempFile.close()
def EditArray(array,title='List_Menu',info=''):
    while True:
        print(f'{info}\n__{title}__\n1)Add Element\n2)Remove Element\n3)Save')
        selection = input('select: ')
        #Check options
        if selection == '1':
            print('Add Element:')
            selection = input('Element name: ')
            array = AvoidDoubleElements(array,selection)
        elif selection == '2' and len(array)>0:
            print('Remove Element:')
            i = 0
            for x in array:
                i+=1
                print(str(i)+') '+str(x))
            selection = input('Select element: ')
            #Check for valid number
            if not selection.isnumeric():
                continue
            if int(selection)-1 > len(array) or int(selection)-1 < 0:
                continue
            array = RemoveArrayElement(array,array[int(selection)])
        else:
            break
    return array

def Space(lines = 20):
    while lines > 0:
        print('\n')
        lines-=1

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
def SelectArrayElement(array,has_title = False):
    i = 1
    for x in array:
        if not has_title:
            print(f'{i}){x}')
        else:
            print(f'{i}){x.title}')
        i+=1
    selection = input('Select Element: ')
    if not selection.isnumeric():
        print("Error, wrong input")
        return -1
    selection = int(selection)-1
    if selection < 0 or selection > len(array):
        print("Error, Input to high or to low")
        return -1
    return selection