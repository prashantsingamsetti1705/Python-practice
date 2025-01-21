#write a python program will accept value and decide palindrome or not
value=input("enter a value:")
if value==value[::-1]:
    print("given  value is a palindrome{}".format(value,value))
if value!=value[::-1]:
    print("given value  is a not a palindrome{}".format(value,value))
