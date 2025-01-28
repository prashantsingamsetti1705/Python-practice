#dict reader for the file
import csv
with open("raju.csv","r") as rp:
    dcsvr=csv.DictReader(rp)
    for record in dcsvr:
        for k,v in record.items():
            print("\t\t{}--------->{}".format(k,v))
        print("*"*50)