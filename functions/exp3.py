#write a python program which will print n-perfect number ands it is accepted by key bord and it should be+ve
# # Function to check if a number is perfect
def perfect_number(n):
    if n<=0:
        print("{}is in valid input".format(n))
    else:
        c=0
        n1=1
        while c<n:
            s=0
            for i in range(1,n1):
                if n1%i==0:
                    s=s+i
            if s==n1:
                print("it is perfect number{}".format(n1))
                c=c+1
            n1=n1+1
#main program
n=int(input("enter value of n:"))
perfect_number(n)


