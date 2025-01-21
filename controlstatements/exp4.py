#write a python program which will accept a line text and find its
#word length in line:
line=input("enter a line of text:")
if len(line)==0:
    print("enter a line of text ---try again ")
else:
    if line.isspace():
        print("dont enter space ---try again:")
    else:
        words=line.split()
        print("given line{}".format(len))
        for word in words :
            print("/t/t{}------->{}".format(word,len(word)))
#logic2
line=input("enter a line of text:")
if len(line)==0:
    print("enter a line of text ---try again ")
else:
    dw={}
    if line.isspace():
        print("dont enter space---->try again:")
    else:
        words=line.split()
        print("given line{}".format(len))
        for word in words:
            dw[word]=len(words)
        else:
            for w,wl in dw.items():
                print("/t/t{}---->{}".format(w,wl))
