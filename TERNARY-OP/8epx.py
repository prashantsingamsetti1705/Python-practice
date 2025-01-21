#write a python program which will aceppt given alphabet is vowel or conctant
# by using a ternary op
a=input("enter a alphabets")
# res is used to display
res="vowels" if a in  list("AEIVOUaeivou") else"constatant"
print("given alphabet {} is {}".format(a,res))
