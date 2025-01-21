#program for a+b whole square
a=float(input("enter a value:"))
b=float(input("enter a value:"))
# c=(a+b)**2
c=a**2+2*(a*b)+b**2
print("*"*50)
print("/t/t whole sqr={},={},={}".format(a,b,c))
print("*"*50)
#or different way
c=(a+b)*(a+b)
print("*"*50)
print("/t/t whole sqr={},={},={}".format(a,b,c))
print("*"*50)