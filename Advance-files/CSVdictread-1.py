#write a python program which read the csv file contanat data
import csv
with open("C:\\Users\\prash\\OneDrive\\Desktop\\HTML\\eno,name,sal.csv","r") as fp:
    csvdr=csv.DictReader(fp)
    for record in csvdr:
        for k,v in record .items():
            print("{}--------->{}".format(k,v))
        print("*"*50)
