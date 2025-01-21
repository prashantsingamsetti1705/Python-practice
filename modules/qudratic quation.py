# Function to find roots of a quadratic equation
import cmath

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
d = cmath.sqrt(b ** 2 - 4 * a * c)
def root():
    s1 = (-b + d) / (2 * a)
    s2 = (-b - d) / (2 * a)
    print("The roots of the quadratic equation are: {} and {}".format(s1, s2))
root()


