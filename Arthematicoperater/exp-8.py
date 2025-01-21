#program for cal the number of days into hours and mintues
from pprint import pprint

d=float(input("enter a no of days:"))
h=float(input("enter no of hours:"))
m=float(input("enter no of minutes:"))
dh=(d*h)
dm=(dh*m)
print("*"*50)
# print("/t/t cal of days(d={}),into hours(h={}),into time(m={}),dh(dh={}),(dm={})".format(d,h,m,dh,dm))
print("*"*50)
pprint("/t/t cal the number of days into hours and minutes dm={}".format(dm))




