n = int(input("enter number of values :"))
if n <= 0:
    print("{}is is invalid input please enter a +ve".format(n))
else:
    print("--------------------------")
    lst = []
    print("enter a values in the list")
    for i in range(1, n + 1):
        lst.append(float(input("{} enter the value of list".format(i))))
    else:
        print(lst)
        pslist= []
        nslist= []
        ps,ns = 0,0
        for val in lst:
            if val > 0:
                ps = ps + val
                pslist.append(val)
            else:
                ns = ns + val
                nslist.append(val)
        else:
            print("Possitive Elements={}".format(pslist))
            print("Possitive Elements Sum={}".format(ps))
            print("-----------------------------------")
            print("Negative Elements={}".format(nslist))
            print("Negative Elements Sum={}".format(ns))
            print("-----------------------------------")