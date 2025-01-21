#write a program which will aceept two numerical value  a biggest and equality
# by using ternary operator
a=float(input("enter a value of a:"))
b=float(input("eneter  a value of b:"))
c=float(input("eneter a value of c:"))
# result to print 3 biggest number of numerical value
res=a if a<=b and a<c else  b if b<a and b<=c else c if c<=a and c<b else"both are eual"
print("three less vlaue ({} {} is {})={} ".format(a,b,c,res))