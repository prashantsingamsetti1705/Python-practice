#generate 12 Calendar for an Year
#InnerLoopEx7.py
import calendar
year=int(input("enetr an year:"))
if year<=0:
    print("Invalid year:")
else:
    print("*"*50)
    for i in range (1,13):
        print(calendar.month(year,i))
    print("-"*50)