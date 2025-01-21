#writea python program which will print the sum of the program
def sumop():
    a=float(input("enter value of a:"))
    b=float(input("enter value of b:"))
    #doing process
    c=a+b
    return  a,b,c
#main program
k,v,res=sumop()
#display the result
print("sum of ({},{})={}".format(k,v,res))
#single line assing ment print
print("sum value of a{}".format(k))
print("sum value of b{}".format(v))
print("sum value of res{}".format(res))
