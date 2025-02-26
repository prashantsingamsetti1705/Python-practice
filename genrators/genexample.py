#example program on generators
def gen():
    yield "python"
    yield "django"
    yield "anil"

#main program
cr=gen()
print("type of the gen",type(cr))
print(next(cr))
print(next(cr))
for val in cr:
    print(val)