#write a program which will aceept value palindrome or not
# by using ternary operator
a=input("enter a palindrom:")
res="palindrome"if a==a[::-1] else "not a palindrome"
print("{} is a {}".format(a,res))



