#Program for accepting Numerical Value and find smallest among them anc check for equality
#SimpleIfStmtEx2.py
a,b=float(input("enter a numeric:")),float(input("enter a numerical :"))
if a<b:
    print("min{},{},{}".format(a,b,a))
if b<a:
    print("min{},{},{}".format(b,a,b))
if a==b:
    print("is equal{},{},{}".format(a,b,a))
print("program is completed")