import os
import FastPy as FP

class MainProgram:
    def __init__(self):
        #Path
        self.file_name = 'AsS.sav'
        self.user_path = os.path.expanduser("~")
        self.savefile_path = os.path.join(self.user_path, self.file_name)
        self.SortPath = []

    def StartupCheck(self):
        #Look for File
        if not os.path.exists(self.savefile_path):
            self.SortPath = FP.CreateSaveFile(self.savefile_path)

    def MainLoop(self):
        self.StartupCheck()
        while True:
            print('__Main_Menu__\n')



if __name__ == '__main__':
    MP = MainProgram()
    MP.MainLoop()
