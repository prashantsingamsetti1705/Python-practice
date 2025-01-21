#program for generating mulmtables for 1 to n where n is +ve
#inner loop ex6
n=int(input("enter how many mul tables u want:"))
if n<=0:
    print("{} is a invalid".format(n))
else:
    for num in range (1,n+1):
        print("*"*50)
        print("mul tabel for:{}".format(num))
        print("-"*50)
        for i in range(1,11):
            print("\t{}x{}={}".format(num,i,num*i))
        else:
            print("-"*50)
