#write a python program of movie ticket pricing
age=22
day="wednesday"
price=12 if  age >=18 else 8

print(price)
#write a python in diff program
age=int(input("enter the age:"))
day=input("enter the day:")
price=int(input("enter the price:"))
if day=="wed" and age >=18:
    print("the discount is 12$",price-12)
else:
    print("the discount is 8$")