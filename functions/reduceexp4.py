
#Program for implementing the following Problem
#FilterMapReduceEx.py
#Accept the salaries of Different Employees ranges between 0 to 1000
#Get the salaries ranges from 0 to 500 and give 10 % hike
#Get the salaries ranges from 501 to 1000 and give 20 % hike
#Find the Total Salary before hike and after hike whose  salaries ranges from 0 to 500
#Find the Total Salary before hike and after hike whose  salaries ranges from 501 to 1000
import functools
oldsal=list([float(sal) for sal in input("Enter List of Salaries:").split()   if float(sal) in range(0,1001) ] )
print("-------------------------------------------------------------------------------")
print("Given Salaries:")
print(oldsal)
print("-------------------------------------------------------------------------------")
#Get the salaries ranges from 0 to 500 and give 10 % hike
sal0_500=list(filter(lambda sal: 0<=sal<=500, oldsal))
hikesal0_500=list(map(lambda sal:sal+sal*(10/100),sal0_500))
print("*"*50)
print("Salaries ranges 0 -500\tHike Salaries ranges 0 -500")
print("*"*50)
for osl,hsl in zip(sal0_500,hikesal0_500):
	print("\t{}\t\t\t{}".format(osl,hsl))
print("*"*50)
#Find the Total Salary before hike and after hike whose  salaries ranges from 0 to 500
totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2, sal0_500)
hiketotsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2, hikesal0_500)
print(" Total:{}\t\t\t{}".format(totsal0_500,hiketotsal0_500))
print("*"*50)
#Get the salaries ranges from 501 to 1000 and give 20 % hike
sal501_1000=list(filter(lambda sal: sal in range(501,1001), oldsal))
hikesal501_1000=list(map(lambda sal:sal+sal*(20/100),sal501_1000))
print("*"*50)
print("Salaries ranges 501-1000\tHike Salaries ranges 501 -1000")
print("*"*50)
for osl,hsl in zip(sal501_1000,hikesal501_1000):
		print("\t{}\t\t\t{}".format(osl,hsl))
print("*"*50)
totsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
tothikesal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal501_1000)
print(" Total:{}\t\t\t{}".format(totsal501_1000,tothikesal501_1000))
print("*"*50)
print("Grand Totals:{}\t\t\t{}".format(totsal0_500+totsal501_1000,hiketotsal0_500+tothikesal501_1000))
print("*"*50)


