# in python programing we have 3 type spicle functions
#there are are filter and map and reduce
#filter is used to
#filter (function,itarbleobj)
#progarm for filetr
# def pv(n):
#     if n>0:
#         return True
#     else:
#         return False
# lst=[int(val) for val in input().split()]
# s=list(filter(pv,lst))
# print(s)

lst=[int(val) for val in input().split()]
p=list(map(lambda sal:sal+sal*20/100 ,lst))
print(p)
#program for demonstrating the map
def hike(sal):
    return (sal+sal*50/100)
old=[10,2,5,6,4]
obj=list(map(hike,old))
print(obj)
#write a python program on reduce