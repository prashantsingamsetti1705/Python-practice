# write a pyhton program which will generate a 0dd number reverse order
#using while loop
n=input("Enter How Many Numbers u want generate:")
if(n.isdigit()):
    num=int(n)
    if(num==0):
        print("{} is invalid Input:".format(num))
    else:
        if num%2==0:
            num=num-1
        print("Numbers from {} to 1".format(num))
        i=num # Initlization
        while(i>=1):
            print(i)
            i=i-2
        else:
            print("--------------------------------")
else:
    print("{} is Invalid Input".format(n))