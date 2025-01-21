#write a python program using continue
#exp1
s="PYTHON"
print("by using for loop")
for ch in s:
    print(ch)
else:
    print("iam from the else part")
    print("----------------------------")
#my reqriment is to display :pyhon
s="PYTHON"
print("by using for loop")
for ch in s:
    if ch=="T":
        continue
    print(ch,end="")
else:
    print("\n iam from the else part of for loop ")
    print("------------------------------------")
#using while loop:
s="PYTHON"
print("using while loop")
print("-------------------")
i=0
while i<len(s):
    print(s[i])
    i=i+1
else:
    print("iam from the else part")
    print("----------------")
#uing while loop and continue:
s="PYTHON"
print("using while loop")
print("-------------------")
i=0
while i<len(s):
    if s[i]=="T":
        i=i+1
        continue
    print(s[i],end="")
    i=i+1
else:
    print("\n iam from the else part of for loop ")

