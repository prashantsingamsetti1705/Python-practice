#Program for accepting List if Numebrs and get those numbers whose number length ranges btween 2 to 3
#FilterEx3.py
print("Enter List of Numbers separated by Space:")
numbers=[value for value in input().split()]
print("Given Numbers:",numbers)
# ['1234', '56', '3456', '78', '123', '79', 'Python', 'java', '67']
nums23=list(filter(lambda num:num.isdigit() and len(num) in [2,3] , numbers))
print("Numbers with 2 or 3 in length")
print(nums23)



d={10:"python",20:"java",30:"danjano",40:"ai",50:"mls"}
d2=list(filter(lambda d:len(d) in [2,3],d.values()))
print(d2)