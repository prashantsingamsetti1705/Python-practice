#wirte a python program use to create a folder
#import os ,dir()
#exception------->FileNotFoundError,OSError
import os
try:
    os.mkdir("pytho")#mkdir is to create a single folder
    print("folder created successfully---------->verify")
except FileNotFoundError:
    print("mkdir() you can create aone folder")
except FileExistsError:
    print("file is alreday exist try differt name")
except OSError:
    print("you get an os error check you path")

