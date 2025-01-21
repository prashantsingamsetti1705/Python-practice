n=int(input("enter how many number u want"))
if n<=0:
    print("you had enter a wrong please try again")
else:
    lst=[]
    print("enter a list of words")
    for i in range(1,n+1):
        lst.append(input("enter{}value".format(i)))
    else:
        print("given elments of list")
        print(lst)
        vlst=[]
        for word in lst:
            if not any (ch in list("aeiouAEIOU")for ch in word):
                vlst.append(word)
            else:
                print("not vowel elements of list")
                print(vlst)