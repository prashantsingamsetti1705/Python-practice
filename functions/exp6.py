#writre  a python program is given line of text  words whose first equal to end last letter is same
def samefisrtletter_lastletter(line):
    if len(line)==0:
        print("dont senter empty space")
    elif line.isspace():
        print("line should not be empty dont enter space")
    elif line.isdigit():
        print("dont enter digit ")
    else:
        words=line.split()
        for word in words:
            if (word[0]
                    ==word[-1]):
                print("first and last letter {}".format(word))
            else:
                print("first and last letter not equal{}".format(word))
#main program
line=input("enter a line of text:")
samefisrtletter_lastletter(line)