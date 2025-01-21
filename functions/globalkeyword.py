#write a python program which using gobal key word
# def update1():
#     global a,b
#     a=a+1
#     b=b+1
# def update2():
#     global a,b
#     a=a*1
#     b=b*2
#
# def update3():
#     c = a +2
#     d = b + 2
# #mainprogram
# a,b=10,20
# print("main before the update1----()-{}-{}".format(a,b))
# update1()
# print("main after the update1----()-{}-{}".format(a,b))
# update2()
# print("main after the update2----()-{}-{}".format(a,b))
# update3()
# print("()-{}-{}".format(a,b))

# a=10
# b=20
# c=30
# d=40
# def _operation():
#     a=100
#     b=200
#     c=300
#     d=400
#     res=a+b+c+d+globals().get("a")+globals()["b"]+globals().get("c")+globals().get("d")
#     print("the gobal values of the keyword globallength{}".format(res))
#     #mainprogram
# _operation()


#GlobalsFunEx3.py
#Program for Demonstrating globals()
#GlobalsFunEx2.py
a=10
b=20 # here 'a', 'b' are called global variables
def g_globals():
    d=globals()
    for k,v in d.items():
        print("{}--------->{}".format(k,v))
    print("{} ".format(d.get("a")))
    print("{} ".format(d.get("b")))

g_globals()