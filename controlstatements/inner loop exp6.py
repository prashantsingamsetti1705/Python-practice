# write a pyhton program which will accept the given list of element
n=int(input("enter a number how many word u want"))
if n<=0:
    print("{} dont enter a empty words".format(n))
else:
    print("*"*50)
    lst=[]
    for i in range(0,n):
        lst.append(input("{} value".format(i)))
    else:
        print("list of values")
        print(lst)
        novels=[]
        for word in lst:
            res=True
            for ch in word:
                if ch in word:
                    if ch.lower() in list("aieou"):
                        res=False
                        break
            if res:
                novels.append(word)
        print(novels)


