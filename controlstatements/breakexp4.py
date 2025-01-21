#write a python program which will accept a word and decide it vowel or not
word=input("enter any word")
if(len(word)==0):
    print("word should not empty ")
else:
    if word.isspace():
        print("word shuld not be space----try again")
    else:
        res="not vowel word"
        for ch in word:
            if ch.lower()in list("aieou"):
                res="vowel"
        print("{} is {}".format(word,res))






