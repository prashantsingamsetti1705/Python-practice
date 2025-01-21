#for loop in for loop
#simple program
# for i in range(1,6):
#     print("*"*50)
#     print("iam from outer loopi=",i)
#     for j in range(1,3):
#         print("*"*50)
#         print("\t\ti am from inner for loop j=",j)
#while loop in while loop
#simple program
i=1
while i<=5:
    print("*"*50)
    print("iam from outer loopi=",i)
    j=1
    while j <= 3:

        print("iam from outer loop j=", j)
        j=j+1
    else:
        i=i+1
        print("iam from the outer loop ")
else:
    print("iam from the inner loop")

#exp for loop in while loop
i=5
while(i>=1):
    print("*"*50)
    print("outer loop:value of i=",i)
    for j in range(3,0,-1):
        print("inner loop:valuej=",j)
    else:
        i=-1
        print("\tout -off  inner loop")
        print("-"*50)
else:
    print("out-off outer loop")
    print("*"*50)
#exp while loop in for lop
for i in range(1,6):
    print("*"*50)
    print("outer loop: value of i=",i)
    j=3
    while(j>=1):
        print("\t\tinner loop:value j=",j)
        j=j-1
    else:
        print("\tout-off inner loop")
        print("*"*50)
else:
    print("out-off outer loop")
    print("*"*50)