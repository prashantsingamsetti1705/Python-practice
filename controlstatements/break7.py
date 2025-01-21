#write a python to generate a palindrome
w=int(input("enter how many number of words u want :"))
if w<=0:
    print("invalid input".format(w))
else:
    print("--------------------")
    lst=[]
    print("enter a list of values ")
    for i in range (1,w+1):
        lst.append(input("enter{}value:".format(i)))
    else:
        print(lst)
        plst=list()
        for i in lst:
            if i==i[::-1]:
                plst.append(i)
            if plst:
                print("{} is a plaindrome".format(plst))
            else:
                print("not a plaindrome")

