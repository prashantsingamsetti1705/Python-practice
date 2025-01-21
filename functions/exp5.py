#write a program which will accept line of text and get list of even word length and add length and display word lenght

def findtheword_len(line):
    if len(line)==0:
        print("enter line of the text word-try again:")
    elif line.isspace():
        print("the line text dont space:")
    elif line.isdigit():
        print("the line text dont enter digit:")
    else:
        evendict={}
        odddict={}
        words=line.split()
        for word in words:
            if len(word)%2==0:
                evendict[word]=len(word)
            else:
                odddict[word]=len(word)
        else:
            for w,l in evendict.items():
                print("\t{}--------->{}".format(w,l))
            print("*"*50)
            for w, l in odddict.items():
                print("\t{}--------->{}".format(w, l))


#main program
line=input("enter line of text :")
findtheword_len(line)