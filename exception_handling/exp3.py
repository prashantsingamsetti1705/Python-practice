#Ex3.py
try:
	print("Program Execution started")
	s1=input("\tEnter Value of a:")
	s2=input("\tEnter Value of b:")
	a=int(s1) #----------------------------ValueError
	b=int(s2) #----------------------------ValueError
	c=a/b  #-------------------------------ZeroDivisionError
except ZeroDivisionError as z: # Multi Exception Handling Block
	print(z)
except ValueError as v:
	print(v)
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