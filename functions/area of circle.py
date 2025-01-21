#write a python program which will calculate the are of the circel
#programm hint area=3.14*r**2
def arera_circle():
    r=float(input("eneter value of radius:"))
    if r<=0:
        return "inavlid input"
    else:
        ac=3.14*r**2
        return r,ac
#arae of sq
def arera_sq():
    s=float(input("eneter value of side:"))
    if s<=0:
        return "inavlid input"
    else:
        asq=s**2
        return s,asq
#area of rectangle hint alb=l*b
def area_rec():
    l=float(input("enter a value of lenght:"))
    b=float(input("enter a value of breath"))
    if l<=0 or b<=0:
        return "invalid input"
    else:
        arec=l*b
        return l,b,arec
#area of rectangle hint alb=1/2*(l*b)
def area_tri():
    l=float(input("enter a value of lenght:"))
    b=float(input("enter a value of breath"))
    if l<=0 or b<=0:
        return "invalid input"
    else:
        atri=1/2*l*b
        return l,b,atri
#main program
print("arae of arae of circle")
print("*"*50)
r,res=arera_circle()
print("area of circle({})={}".format(r,res))
#main of sq
print("arae of sqr")
print("*"*50)
r,res=arera_sq()
print("area of sq{}={}".format(r,res))
#maqin of rec
print("area of rec")
print("*"*50)
r,a,res=area_rec()
print("area of rec{},{}={}".format(r,a,res))
#maqin of triangle
print("area of tri")
print("*"*50)
r,a,res=area_tri()
print("area of tri{},{}={}".format(r,a,res))


