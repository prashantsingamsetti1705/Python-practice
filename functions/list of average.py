#writea python program which will print sum of list and average of the list
def read_values():
    n=int(input("enter a value of how values in a list:"))
    if n<=0:
        return "inavalid input"
    else:
        lst=[]
        for val in range(1,n+1):
            lst.append(int(input("enter a values:".format(val))))
        return lst
def sum_values():
    lst=read_values()
    if len(lst)==0:
        print("lst cant not be find sum of average")
    else:
        print("-----------------------")
        s=0
        for val in lst:
            s=s+val
        else:
            print("--------------")
            print("sum{}".format(s))
            print("average{}".format(s/len(lst)))
#main program
sum_values()

