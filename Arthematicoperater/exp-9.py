#ArithmeticOperatorsEx4.py
#Celsius to Fahrenheit	° F = 9/5 ( ° C) + 32
#Kelvin to Fahrenheit	° F = 9/5 (K - 273.15) + 32
#Celsius to kelvin c+273
# kelvin to celsius k-273.15
#Fahrenheit to Celsiu (f-32) 5/9 F = 9/5 (K - 32) +273.15
#Farhrenheit to kelvin
ct=float(input("Enter the Temp in Celsius:"))
F = (9/5)* ct + 32
print("Celsius in Fahrenheit={}".format(F))
print("---------------------------------------")
kt=float(input("Enter the Temp in Kelvin:"))
F = (9/5)*(kt - 2731.5) + 32
print("Kelvin in Fahrenheit={}".format(F))
print("---------------------------------------")
ck=float(input("Enter the Temp in Celsius:"))
F=ck+273.15
print("Celsius in kelvin={}".format(F))
print("---------------------------------------")
kc=float(input("Enter the Temp in kelvin:"))
F=kc-273.15
print("kelvin in Celsius ={}".format(F))
print("---------------------------------------")
fc=float(input("Enter the Temp in Fahrenheit:"))
F=9/5*(fc- 32) +273.15
print(" Fahrenheit in Celsius ={}".format(F))
print("---------------------------------------")
fk=float(input("Enter the Temp in Fahrenheit:"))
F = 9/5*(fk- 32) +273.15
print(" Fahrenheit in kelvin ={}".format(F))




