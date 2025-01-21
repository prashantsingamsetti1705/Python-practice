#writea python program which will accept the palindrome or not
palindrome=lambda w:"{} palindrome".format(w) if w==w[::-1] else"{} is not palindrome ".format(w)
#anonymus function
print("enter your word")
word=palindrome(input())
print(word)
#write a python program which will accept the word and given word is vowel or not
vword=lambda w:"{} vword".format(w) if any(char in "aeiouAEIOU" for char in w) else"{} is not vw ".format(w)
#anonymus function
print("enter your word")
wr=vword(input())
print(wr)