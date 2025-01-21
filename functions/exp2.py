#write pyhton program which will accpet a value a decid it is perfect number or not
# def pf_num(n):
#     if n<=0:
#         print("invalid input")
#     else:
#         lst=[]
#         s=0
#         for i in range(1,(n//2)+1):
#             lst.append(i)
#             if n%i==0:
#                 s=s+i
#         print(lst)
#         if s==n:
#             print("{} is perfect number ".format(n))
#         else:
#             print("{} is not pertfect".format(n))

#mainprogram
# n=int(input("enter value of n:"))
# pf_num(n)

#write pyhton program which will accpet a value a decid it is perfect number or not
def pf_num(n):
    for i in range(1,n+1):
        s=0
        for j in range(1,(i//2)+1):
            if i%j==0:
                s=s+j
        else:
            if s==i:
                print("{} is perfect number ".format(i))
            # else:
            #     print("{} is not pertfect".format(i))

#mainprogram
# n=int(input("enter value of n:"))
pf_num(1000)
