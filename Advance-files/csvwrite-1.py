#write a python program to create a csv file add add the data into it
import csv #step-1
with open("emp.csv","a") as fp:
    hname=["eno","ename","esal"]#header
    rw=[[100,"sai",200.0],[200,"raju",300.0],[300,"anil",300.0]]#rows
    #write the names of the header of the file
    rec=csv.writer(fp)#step5
    #write the row  and insert it
    rec.writerow(hname)
    rec.writerows(rw)#step6
    print("CSV File created -----please verify")
