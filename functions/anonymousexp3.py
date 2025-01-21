#wrte a python program which accept a number and decide prime number or not
prime = lambda n: n if n > 1 and all(n % i != 0 for i in range(2, n))else"not prime"
print("enter the value :")
pr=prime(int(input()))
print("prime=",pr)
