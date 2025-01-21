#write a python program which will aceppt given number is positive or ngeitive
# by using a ternary op
a=float(input("enter value  of a :"))
#res to display result
res="positive"if a>0 else "nagitive" if a<0 else"all are zero"
print("given integer({})={}".format(a,res))
