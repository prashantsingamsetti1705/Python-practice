#program for cal to number of years into months and days
y=float(input("enter no of years:"))
m=float(input("enter no of months:"))
d=float(input("enter a no of days:"))
ym=(y*m)
md=(ym*d)
print("*"*50)
print("/t/t cal of days(d={}),into years(y={}),into months(t={}),(ym={}),(md={})".format(d,y,m,ym,md))

print("cal the no days few years and months={}".format(md))