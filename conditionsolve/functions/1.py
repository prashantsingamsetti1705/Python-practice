# # write a python program for function
# #function it conatin models and packages
# #approach
#
# # def mulop(a,b):
# #     c=a*b
# #     return c
# # #main program
# # res=mulop(10,20)
# # print(res)
#
# def mul(x,y):
#     c=x*y
#     return c
# x=int(input("enter the value of x:"))
# y=int(input("enter the value of y"))
# res=mul(x,y)
# print(res)
#
# #write a python program for simple int
# def simple_int():
#     p=int(input("enter the amount of principle:"))
#     t=int(input("enter the amount of time"))
#     r=int(input("enter the amount of rate"))
#     si=(p*t*r)/100
#     totamt=p+si
#     return p,r,t,si,totamt
# p,r,t,si,totamt=simple_int()
# print(p)
# print(r)
# print(t)
# print(si)
# print(totamt)
# #
#they are pass prameter

def sum(a,b,c=30):
    return a+b+c
s=sum(10,20)
print(s)

#key word
def sum(a,b,c=30):
    return a+b+c
s=sum(b=10,a=20)
print(s)
#varible length arugument
#keyword varible length argumanet
# def sum(a,b,*,d=20)