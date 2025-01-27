#write a pytho program to readthe the csv file in the data
import csv
with open("emp.csv","r") as rp:
    rec=csv.reader(rp)
    for record in rec:
        for val in record:
            print(val,end="\t\t")
        print()
print("-"*50)