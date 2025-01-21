#here multable is the name of the module name
def mul(n):#it is function name
    if n<0:
        print("{} is invalid input".format(n))
    else:
        print("multable for {}".format(n))
        print("*" * 50)
        for i in range(1,11):
            print("\t{}X{}={}".format(n,i,n*i))
        print("*"*50)