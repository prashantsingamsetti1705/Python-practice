#write a program which will aceept two numerical value  a biggest and equality
# by using ternary operator
a,b=float(input("enter a value of a:")), float(input("enter a value of b:"))
res= a if a<b else b if b<a else "both are equal"
print("less value ({} is {})={}".format(a,b,res))