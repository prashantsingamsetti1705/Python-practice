nn=int(input("Enter a Number to convert into Eqv Roamn Number:")) # nn=2902
if(nn<=0):
    print("{} is invalid invalid".format(nn))
else:
    #Conversion Process code
    while(nn>=1000):
        print("M",end="")
        nn=nn-1000
    if(nn>=900):
        print("CM",end="")
        nn=nn-900
    if(nn>=500):
        print("D",end="")
        nn=nn-500
    if(nn>=400):
        print("CD", end="")
        nn = nn - 400
    while(nn>=100):
        print("C", end="")
        nn = nn - 100
    if(nn>=90):
        print("XC",end="")
        nn=nn-90
    if (nn >= 50):
        print("L", end="")
        nn = nn - 50
    if (nn >= 40):
        print("XL", end="")
        nn = nn - 40
    while(nn>=10):
        print("X",end="")
        nn=nn-10
    if(nn>=9):
        print("IX",end="")
        nn=nn-9
    if (nn >= 5):
        print("V", end="")
        nn = nn - 5
    if (nn >= 4):
        print("IV", end="")
        nn = nn - 4
    while (nn >= 1):
        print("I", end="")
        nn = nn - 1
