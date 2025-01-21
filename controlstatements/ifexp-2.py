#write a python program given n value is +ve or -ve or zero
n=float(input("enter a numerical :"))
if n>0:
    print("given numerical is +ve{}".format(n))
if n<0:
    print("given numerical is -ve{}".format(n))
if n==0:
    print("given numerical is zero{}".format(n))
print("program is completed")