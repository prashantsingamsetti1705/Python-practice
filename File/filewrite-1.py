#write a python program for read and write  the adata on e record to another record
#write(str())

eno=10
en="prashant"
sal=100.0
with open("record.txt","w") as fp:
    fp.write(str(eno)+"\t")
    fp.write(en+"\n")
    fp.write(str(sal)+"\n")
print("the value are enter the new record")




