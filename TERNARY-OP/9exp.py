#write a python program which will aceppt given alphabet is vowel or notvowels
# by using a ternary op
a=input("enter a word :")
# res is used to display
res="vowels" if a [2] in list("aeiou") else"not vowels"
print("given alphabet {} is {}".format(a,res))