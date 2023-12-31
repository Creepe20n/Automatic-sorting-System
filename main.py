import os
import FastPy as FP
import ComandMenuBuilder as CMB
class MainProgram:
    def __init__(self):
        #Path
        self.file_name = 'AsS.sav'
        self.user_path = os.path.expanduser("~")
        self.savefile_path = os.path.join(self.user_path, self.file_name)
        self.SortPath = []
        self.file_extension = []

    def StartupCheck(self):
        #Look for File
        if not os.path.exists(self.savefile_path):
            FP.CreateSaveFile(self.savefile_path)
        #Load Data and sort it in Array
        data = FP.Load(self.savefile_path)
        for x in data:
            if not os.path.exists(x):
                self.file_extension.append(x)
                continue
            self.SortPath.append(x)

    def MainMenu(self):
        A1 = CMB.EditArray(array = self.SortPath,title="SortPath",info="Path")
        A2 = CMB.MethodOption(title ="method",method= lambda:i("d"))
        Opt = [A1,A2]
        Menu = CMB.Menu(Opt,exit_opt=True)
        Menu.MainLoop()
    def MainLoop(self):
        self.StartupCheck()
        while True:
            try:
                self.MainMenu()
            except Exception as e:
                print(e)
def i(d):
    print(d)
    A1 = CMB.EditArray(array =[],title="SortPath",info="Path")
    Opt = [A1]
    Menu = CMB.Menu(Opt,title="i")
    Menu.MainLoop()

if __name__ == '__main__':
    MP = MainProgram()
    MP.MainLoop()
