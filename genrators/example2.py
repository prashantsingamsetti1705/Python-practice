#Program Demonstrating Generator
#GenEx3.py
def kvrrange(start,stop=0,step=1):
	if(start>stop):
		stop=start
		start=0
	while(start<=stop):
			yield start
			start=start+step

#Main Program
print("-----------------------------------------")
r=kvrrange(100,111,2)
for v in r:
	print(v)
print("-----------------------------------------")
r=kvrrange(10,16)
for v in r:
	print(v)
print("-----------------------------------------")
r=kvrrange(5)
for v in r:
	print(v)
print("-----------------------------------------")