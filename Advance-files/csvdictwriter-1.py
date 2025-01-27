#write a python program which uesd to creata a csv file
import csv
with open("stu.csv","a") as fp:
    h1=["sno","sname","marks"]
    rw=[{"sno":1,"sname":"prash","marks":200},{"sno":32,"sname":"sai","marks":"6.38"},{"sno":1,"sname":"raju","marks":20}]
    rec=csv.DictWriter(fp,fieldnames=h1)
    rec.writeheader()
    rec.writerows(rw)
    print("file verified succes fully")