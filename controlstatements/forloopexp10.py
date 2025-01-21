#Program for Reading List of Values and Display
#ReadValuesEx1.py
n=int(input("Enter How Many Values u have:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    lst=[] # create an empty list for adding dynamic values
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        
        print("List of Values")
        print(lst)