# function or lambdafunction
# this are does not contain name excplictly  the function which
# the function which does not conatian any name explicitly
# to per form instatnt operation incentat operation are thoes which are used at that point of view
# and no longer interested in other part of the appliaction
#write a python program for of anonymous
#to define we use the anonymoys functions we use lamabda key word

# varanme=lambda param-list:statement
# lambda is used for nonymous fun
# it is used for store the data input commin form function
# no need use return and directly pvm excecute
#
def sumop(a,b):
    c=a+b
    return c
res=sumop(10,20)
print("sum",res)


addop=lambda a,b:a+b

res=addop(10,2)
print(res)
#write a python program which will accept two numrical value
vl=lambda x,v:a if a>b else b if a<b else " bothare equal"

a,b=float(input()),float(input())
res=vl(a,b)
print(res)
# write a pytho program
v=lambda word:'vowel' if 'a' in word.lower()  or 'e' in word.lower() or 'o' in word.lower()  or  'u' in word.lower()  else 'notvowel'
word=input("")
res=v(word)
print(res)
# list comprashion
# set comprashion
# var=[epersion forvar in obj if test]
lst=[10,20,30]
var=[val**2 for val in lst ]
print(var)