import FastPy as FP
class Menu:
    def __init__(self,Options):
        self.Options = Options
    def MainLoop(self):
        Space()
        while True:
            selection = SelectArrayElement(self.Options,True)
            # Check for Error
            if selection < 0:
                return
            #Finish Task
            Space()
            self.Options[selection].Menu()

class EditArray:
    def __init__(self,title,info,array):
        self.title = title
        self.info = info
        self.array = array
    def AddArrayElement(self):
        print(self.info)
        selection = input('Type Element: ')
        self.array = FP.AvoidDoubleElements(self.array,selection)
    def RemoveArrayElement(self):
        selection = SelectArrayElement(self.array)
        #Check for Error
        if selection < 0:
            return
        #Finish Task
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
def SelectArrayElement(array, has_title=False):
     # Visualize array
    i = 1
    for x in array:
        if not has_title:
            print(f'{i}){x}')
        else:
            print(f'{i}){x.title}')
        i += 1
    selection = input('Select Element: ')
    # Check if input is valid
    if not selection.isnumeric():
            print("Error, wrong input")
            return -1
    selection = int(selection) - 1
    if selection < 0 or selection > len(array):
        print("Error, Input to high or to low")
        return -1
    return selection


def Space(lines=20):
    while lines > 0:
        print('\n')
        lines -= 1
