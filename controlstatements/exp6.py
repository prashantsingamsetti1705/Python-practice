#write apyhton program which will reverse the word of the program
line=input("enter a line of text :")
if len(line)==0:
    print("enetr a value of text --try again")
else:
    print("-----------------------")
    print("given line of text{}".format(line))
    words=line.split()
    rwl=[]
    for word in words:
            rwl.append(word[::-1])
    else:
        print("reverse of words{}".format(" ".join(rwl)))