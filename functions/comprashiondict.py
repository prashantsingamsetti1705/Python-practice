#write a program which will print the square of the given number
lst=[10,22,33,44,55,77,14,12,88,99]
print(lst)
srd={val:val**2 for val in lst}
print("given\t\tsquare")
for s,sv in srd.items():
    print("{}\t\t\t{}".format(s,sv))

lst=[10,22,33,44,55,77,14,12,88,99]
print(lst)
srd={val:val**0.5 for val in lst}
print("given\t\tsquareroot")
for s,sv in srd.items():
    print("{}\t\t\t{}".format(s,sv))
