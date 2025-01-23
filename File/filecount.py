#file count
#write a python proram which will read the data and found the linth of the wor in 4 0r5
try:
    ct=input("enter the file name")
    with open(ct,"r") as rp:
        sd=rp.read()
        wd=sd.split()
        print(len(wd))
        print(len(sd))
        for i in wd:
            if len(i)<=4:
                print(i)
    print("file is verifed")
except FileNotFoundError:
    print("file does not exist")