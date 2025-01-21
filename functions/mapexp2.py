#wirte a python program which used to print list of valus and find its  sq,sqrt,cubes
#Program accepting List of Numerical values and find their Squares and Square Root
#MapEx2.py
from ntpath import split

print("Enter List of Values Specrated Space:")
tpl=tuple(map(float, input().split()))
print(tpl,type(tpl))
#Find Squares by using map with Anonymous Functions
sqrvals=list(map(lambda n:n**2,tpl))
#Find Square roots by using map with Anonymous Functions
sqrtvals=tuple(map(lambda n: n**0.5,tpl))
#Find Squares by using map with Anonymous Functions
cubevals=tuple(map(lambda n:n**3,tpl))
print("*"*50)
print("GivenValues\t\tSquare Values\t\tSquare Roots\t\tcube")
print("*"*50)
for gv,srv,srtv,cv in zip(tpl,sqrvals,sqrtvals,cubevals):
    print("\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(gv,srv,round(srtv,2),cv))
print("*"*50)

#write a python program which used reverse the word
lst=list(map(str,input().split()))
rs=list(map(lambda n:n[::-1],lst))
print(rs)