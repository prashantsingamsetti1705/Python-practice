#Program for accepting line of Text and get those words which contains at least one one Vowel
# FilterEx6.py
def isvowel(word):
    res=not(set(word.lower()).isdisjoint((set("aeiou"))))
    return  res
#Main Program
line=input("Enter Line of Text:") # Sky is Blue
words=line.split() # words=[Sky, is , blue]
vwords=list(filter(isvowel,words))
print("Vowel Words=",vwords)

#method2 using anynonmus function
line=input("Enter Line of Text:") # Sky is Blue
words=line.split() # words=[Sky, is , blue]
vwords=list(filter(lambda word: not(set(word.lower()).isdisjoint(set("aeiou"))),words))
print("Vowel Words=",vwords)

