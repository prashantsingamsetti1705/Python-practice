w=int(input("enter how many number of words u want :"))
if w<=0:
    print("invalid input".format(w))
else:
    print("--------------------")
    lst=[]
    print("enter a list of values ")
    for i in range (1,w+1):
        lst.append(float(input("enter {}value :".format(i))))
    else:
        print(lst)
        plst=list()
        for val in lst:
            if val not in plst:
                plst.append(val)
        else:
            print("unique elements")
            print(plst)
