#write a python program which will accept the value and add to list find the runner up in a list.
def secore():
    n=int(input("enter value of ruuner in a list n:"))
    if n<0:
        return "invalid input"
    else:
        lst=[]
        for val in range(1,n+1):
            lst.append(int(input("enter a value:".format(val))))
        return lst
def runner_up():
    lst=secore()
    if len(lst)==0:
        print("invalid input")
    else:
        lst1=sorted(set(lst))
        print("runner upp{},{}".format(lst1,lst1[-2]))
#main program
runner_up()