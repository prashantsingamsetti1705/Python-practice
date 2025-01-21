#Program for Finding Sum and Average for List of Values--Sol1
#ForLoopEx4.py
lst=[10,20.459,30.44,43]
s=0
print("--------------------------------")
print("List of Values:")
print("--------------------------------")
for val in lst:
    print("\t{}".format(val))
    s=s+val
else:
    print("--------------------------------")
    print("sum={}".format(s))
    print("Average={}".format(round(s/len(lst),2)))
    print("--------------------------------")
