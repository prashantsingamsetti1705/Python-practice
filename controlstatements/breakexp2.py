#write a pyhton program for using break statement
s="MISSISSIPI"
print("using for loop")
for ch in s:
    print(ch)
else:
    print("iam from the esle part")
print("iam  using the berak statement")
ctr=0
for ch in s:
    if ch=="I":
        ctr=ctr+1
        if ctr==2:
            break
    print(ch,end="")
else:
    print("iam from the else part")
print("\nOther statements in Program")


