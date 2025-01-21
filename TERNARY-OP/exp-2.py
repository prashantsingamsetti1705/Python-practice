#write a program which will aceept two numerical value  a biggest and equality
# by using ternary operator
a,b= float(input("enter a value of a:")),float(input("enter a value of b:"))
# res= a if a>b else b if b>a else "both are equal"
res= a if a>b and a>=b else b if b>a and b>=a else" both are equal"

print("big value ({} , {})={}".format(a,b,res))
# a,b=float(input("Enter Value of a:")),float(input("Enter Value of b:"))
# res= a if a>b else b if b>a else "Both Values are Equal"
# print("Big({},{})={}".format(a,b,res))
