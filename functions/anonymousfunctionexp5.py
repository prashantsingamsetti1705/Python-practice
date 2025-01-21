#write a python program for accepting list of values and find max and min by using anonymous function
#write using predefine function max() and min()
def kvrmax(lst):
    maxv=lst[0]
    for val in lst:
        if val>maxv:
            maxv=val
    return maxv
def kvrmin(lst):
    minv=lst[0]
    for val in lst:
        if val<minv:
            minv=val
    return minv
#anony mus function defs
findmax=lambda lst:kvrmax(lst)
findmin=lambda lst:kvrmin(lst)
#main program
#reading values from keyboard by using list comprehenshion
lst=[float(val) for val in input().split(',')]
#calling anonymous funs
maxv=findmax(lst)
minv=findmin(lst)
print("max {} ={}".format(lst,maxv))
print("min {} ={}".format(lst,minv))






