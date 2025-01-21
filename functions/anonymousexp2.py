#write a python program which will accept w]the two value and find the biggest of them
big=lambda a,b: a if a>b else b if b>a else"both are equal"
print("two values")
bv=big(float(input()),float(input()))
print("the two big valu=",bv)
#write a python program which will accept the three value and find the biggest of them
big=lambda a,b,c: a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "both are equal"
print("two valus")
bv=big(float(input()),float(input()),float(input()))
print("the two big valu=",bv)


