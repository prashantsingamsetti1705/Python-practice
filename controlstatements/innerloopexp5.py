#write a python program which will aceept the list of numerical value and genrate there multiplication tabel
n=int(input("enter how many number you want to mul of table:"))
if n<=0:
    print("invalid input{}".format(n))
else:
    print("*"*50)
    lst=[]
    for i in range(1,n+1):
        lst.append(int(input("{}number of value in a list".format(i))))
    else:
        print(lst)
        for value in lst:
            if value<=0:
                print("is a in valid input{}".format(value))
            print("{} mul tabel".format(value))
            for i in range(1,11):
                print("\t\t {}x{}={} " .format(value,i,value*i))

