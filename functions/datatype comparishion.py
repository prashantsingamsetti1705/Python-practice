#write a python program which will display different type of values in a single function with data type comparishion
#int,float,bool,complex,str,bytes,byte array ,list tuple set frozen set dict none
def displat_datatypes(x):
    if type(x)==int:
        print("{},{}".format(x,type(x)))
    elif type(x)==float:
        print("{},{}".format(x,type(x)))
    elif type(x)==bool:
        print("{},{}".format(x,type(x)))
    elif type(x)==complex:
        print("{},{}".format(x,type(x)))

#main program
print("fundamental data types")
displat_datatypes(10)
displat_datatypes(12.3)
displat_datatypes(True)
displat_datatypes(2+3j)
print("*"*50)