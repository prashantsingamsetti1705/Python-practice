#write a python which will aceept a line of text and get only alphabets
line=input("enter a line of text :")
if len(line)==0:
    print("{}invalid input please".format(line))
else:
    print("--------------------")
    wl=[]
    # words=line.split()
    for word in line:
        wl.append(word)
    else:
        print(wl)
        lst=[]
        for val in wl:
            if not (val.isalpha()):
                lst.append(val)
        else:
            print("".join(lst))
            lst1=[]
            for val in lst:
                if val.isdigit():
                    lst1.append(val)
            else:
                print("".join(lst1))
                lst2=[]
                for val in lst:
                    if not (val.isdigit()):
                        lst2.append(val)
                        print("".join(lst2))







