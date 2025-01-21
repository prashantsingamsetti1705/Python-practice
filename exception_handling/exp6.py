#Ex7.py-----Most Imp Code
#This Code Written by KVR on the Date of  07-01-2025
#KVR is a Programmer projected  that after Few Year this code will come for maintainance in 2030 Year
#In 2030 Year , Balaji is Fresh Programmer working on this Code.
try:
	print("Program Execution started")
	s1=input("\tEnter Value of a:")
	s2=input("\tEnter Value of b:")
	a=int(s1) #----------------------------ValueError
	b=int(s2) #----------------------------ValueError
	c=a/b  #-------------------------------ZeroDivisionError
	s="PYTHON"
	print("Val=",s[10])
except BaseException:
	print("oooops, some this went wrong")
else:
	print("-------------else block-----------------")
	print("\ta=",a)
	print("\tb=",b)
	print("\tDiv=",c)
	print("-------------------------------------------")
finally:
	print("---------------------------------------------")
	print("I am from finally block")
	print("---------------------------------------------")