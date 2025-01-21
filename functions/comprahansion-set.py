#write a pyhton program which print even number odd number spartly  given in a list
lst=[10,20,55,18,66,44,99,5,10,20,18,16]
print("lst")
print("even number")
#syntax var={expersion forloop condition if condtion}
el={val for val in lst if val%2==0}#set comprahansion
print(el)
print("odd number")
ol={val for val in lst if val%2!=0}
print(ol)