#DynamicCSVFileEx1.py
import csv
noc=int(input("Enter How Many Columns u Have:"))
if(noc<=0):
    print("\t{} Invalid Column Numbers".format(noc))
else:
    colnames=[]
    for i in range(1,noc+1):
        colname=input("Enter {} Column Name:".format(i))
        colnames.append(colname)
    else:
        nor=int(input("Enter How Many Records u Have:"))
        if(nor<=0):
            print("\t{} Invalid Number of Records".format(nor))
        else:
            records=list() # Outer List
            for rno in range(1,nor+1):
                print("-" * 50)
                print("Enter {} Record Details".format(rno))
                print("-" * 50)
                record=[] # Inner List
                for recno in range(0, len(colnames)):
                    val=input("\tEnter {} Value:".format(colnames[recno]))
                    record.append(val)
                print("-" * 50)
                records.append(record)
            else:
                #[['1000', 'Rossum'], ['2000', 'Travis'], ['3000', 'KVR']]
                while(True):
                    filename=input("Enter CSV File Name with an extension .csv:")
                    if(filename.endswith(".csv")):
                        with open(filename,"a") as fp:
                            csvwr=csv.writer(fp)
                            csvwr.writerow(colnames)
                            csvwr.writerows(records)
                            print("CSV File Created Dynamically--verify")
                            break
                    else:
                        print("\tInvalid CSV File Extension--try again")
