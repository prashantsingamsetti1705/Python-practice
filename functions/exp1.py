#write a python program which will find factor of given number
def find_factor(n):
    if n<=1:
        print("invalid input")
    for i in range(1,(n//2)+1):
        if n%i==0:
            print("\t{}".format(i))
#main program
n=int(input("enter a value of n:"))
find_factor(n)