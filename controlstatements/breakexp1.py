#write a python program for demonstrsting the need of break statement for loop
s="PYTHON"
print("by using for loop")
for ch in s:
    print(ch)
#my requirement isto displaymonly pvm with out using and sclicing
print("by using the break statement ")
for ch in s:
    if(ch=="O"):
        break
    print(ch,end="")
else:
    print("iam from else part of the loop")
print()
print("other statements in program")
s="PYTHON"
#usine whileloop
s="PYTHON"
print("while loop")
i=0
while i<len(s):
    print(s[i])
    i=i+1
else:
    print("iam from the else part of for loop")
    print("----------------")
print("using the break statement")
i=0
while i<len(s):
    if s[i]=="O":
        break
    print(s[i],end="")
    i = i + 1
else:
    print("iam from the else part")
print()
print("other statements in program")