#Syntax-1:       from module name import Variable Names,Function Names, Class Names
from  simpleint import bname,addr
from Aop import addop
from mathinfo import e,pi
from multable import mul
print("------------------------------------")
print("enter the bank name ={}".format(bname))
print("enter the addr ={}".format(addr))
print("------------------------------------")
addop(10,20)
print("------------------------------------")
print("enter the value of e={}".format(e))
print("enter the value of pi={}".format(pi))
print("------------------------------------")
mul(int(input("enter the table u want")))