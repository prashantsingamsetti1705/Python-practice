#writea pythonprogram which will copythe image into to another file
#file copy
# try:
#     mg=input("the file name in which imag is prasent")
#     with open(mg,"rb") as rp:
#         dst=input("enter destination file name")
#         with open(dst,"ab") as fp:
#             sd=rp.read()
#             fp.write(sd)
#             print("file is verified")
# except FileNotFoundError:
#     print("source does not exist error")

#file count
#write a python proram which will read the data and found the linth of the wor in 4 0r5
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