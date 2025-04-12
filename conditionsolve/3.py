# write a python program factorail of number using while loop
# number =5
# fact=1
# while number > 0:
#     fact=fact*number
#     number=number-1
# print("the factorial number is",fact)
# while True:
#      n=int(input("enetr a number:"))
#      if 1<= n <=10:
#         print("thanks")
#         break
#      else:
#         print("inavlid number")

# write python program which is used devied it self
number=29
p=True
if number>1:
    for i in range(2,number):
        if number % i ==0:
            p=False
            break
print(p)
