#write a python program to  calculate the max length of the  word
#using for line
line=input("enetr a line of text:")
if len(line)==0:
    print("enter  line of text")
else:
    if(line.isspace()):
        print("dont enetr any space")
    else:
        dw={}
        words=line.split()
        for word in words:
            dw[word]=len(word)
        else:
            value=dw.values()
            print("largest word length")
            print("--------------------")
            for word,wordlen in dw.items():
                if(wordlen==max(value)):
                    print("{}".format(word))

