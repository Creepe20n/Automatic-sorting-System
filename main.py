import os
import FastPy as FP

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



    def MainLoop(self):
        self.StartupCheck()




if __name__ == '__main__':
    MP = MainProgram()
    MP.MainLoop()
