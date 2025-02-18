#write a python program which is used to genrate the square off the numbers
#here this the model aporoch is different @ is used to call the decorator
def sqv(pras):#---->decoaror cal oouter function
    def operation():
        a=pras()
        res=a**2
        return a,res
    return operation  #out of the inner function  of indentation
@sqv #outer function call
def getval():#--->inner function
    a=int(input("eneter the a number whcih u want to develop asuare if a number :"))
    return a
#main program
a,sqv=getval()
print("sauare of the number{}--{}".format(a,sqv))




