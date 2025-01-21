
#Program for Demonstrating the need of Variable Length arguments
#This Program Program will execute as it is
#PureVarLenArgsEx2.py
def  disp(*kvr ): # Here *kvr is called Variable Length parameter and whose type <class,'tuple'>
	if(len(kvr)==0):
		print("empty")
	else:
		for val in kvr:
			print("{}".format(val),end=" ")
		print()
	print("----------------------------------------------")

#Main Program----Family of Similar Function Calls with Variable length args
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40)   # Function Call-2  with  4 Args
disp(10,20,30)   # Function Call-3  with  3 Args
disp(10,20)   # Function Call-4  with  2 Args
disp(10)   # Function Call-5  with  1 Args
disp()   # Function Call-6 with  zero Args
#def pure veribel len
def disp_vl(sno,sname,*prs):
    print("*"*50)
    print("sno{}".format(sno))
    print("sname{}".format(sname))
    print("*" * 50)
    s=0
    for val in prs:
        print("\t val-------->{}".format(val))
        s=s+val
    else:
        print("\tsum---------->{}".format(s))

#main program
disp_vl(100,"prashant",10,20,30,40,50)#functon cal-1 with7-arg
disp_vl(200,"prashant-2",10,20,30)#functon cal-1 with7-arg





