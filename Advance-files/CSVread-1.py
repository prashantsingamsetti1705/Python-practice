#write a python program which read the csv file contanat data
import csv
with open("C:\\Users\\prash\\OneDrive\\Desktop\\HTML\\eno,name,sal.csv","r") as fp:
    csvdr=csv.reader(fp)
    for record in csvdr:
        for val in record:
            print(val,end="\t\t")
        print()