#write a python program which will generate firt n-prime number with in given range n
n=int(input("enetr how many number u want for prime number"))
if n<=1:
    print("{} is a invalid input:".format(n))
else:
    nop=0
    for num in range(2,n+1):
        res=True
        for i in range(2,num):
            if num%i==0:
                res=False
                break
        if res:
            print("\t\t{}".format(num))
            nop=nop+1
    else:
        print("-------------------------------")
        print("number of prime within {}={}".format(n,nop))
# # write a python program which will generate firt n-prime number
#     n = int(input("Enter the How many Range values primes will de displayed:"))
#     if (n <= 1):
#         print("Invalid input")
#     else:
#         print("The first {} prime numbers are".format(n))
#         prime = 0
#         num = 2
#         while prime < n:
#             res = True
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     res = False
#                     break
#             if res:
#                 print(num)
#                 prime += 1
#             num += 1
#     print("-" * 50)



