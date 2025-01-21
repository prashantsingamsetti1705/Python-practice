#write a python program to generate even number with i N
# using while loop
n=int(input("enter a how many range you want to generate of of even number: "))
if n<=0:
    print("{}is a invalid input".format(n))
else:
    print("*"*50)
    i=2
    while i<=n:
        print(i)
        i=i+2
    else:
        print("*"*50)
print("{}is a completed".format(n))