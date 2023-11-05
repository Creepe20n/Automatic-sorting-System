import FastPy as FP
class Menu:
    def __init__(self,Options):
        self.edit_array = []
    def MainLoop(self):
        while True:
            pass

class EditArray:
    def __init__(self,title,info,array):
        self.title = title
        self.info = info
        self.array = array
    def AddArrayElement(self):
        print(self.info)
        selection = input('Type Element: ')
        self.array.append(selection)
    def RemoveArrayElement(self):
        i = 1
        for x in self.array:
            print(str(i)+')'+str(x))
            i+=1
        selection = input('Select Element: ')
        if not selection.isnumeric():
            print("Error, wrong input")
            return
        selection = int(selection)-1
        if selection < 0 or selection > len(self.array):
            print("Error, Input to high or to low")
            return
        Space()
        self.array = FP.RemoveArrayElement(self.array,self.array[selection])
    def Menu(self):
        while True:
            print('__'+self.title+'__\n'+self.info)
            print('1)Add Element\n2)Remove Element\n3)Save\n')
            selection = input('Select: ')
            Space()
            if selection == '1':
                self.AddArrayElement()
            elif selection == '2':
                self.RemoveArrayElement()
            elif selection == '3':
                return self.array


def Space(lines=20):
    while lines > 0:
        print('\n')
        lines -= 1
