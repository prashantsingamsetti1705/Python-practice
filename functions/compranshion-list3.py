#write apython program which will find the line of the text is even or odd and finds its lenght of word

line=input("enter how many a line of text")
words=line.split()
print("even words")
el=[word+":"+str(len(word)) for word in words if len(word)%2==0]#list compranshion
print(el)
print("odd words")
ol=[word+":"+str(len(word)) for word in words if len(word)%2!=0]#list compranshion
print(ol)
#write a pyhton program which print even number odd number spartly  given in a list
lst=[10,20,55,18,66,44,99,5,10,20,18,16]
print("lst")
print("even number")
el=[val for val in lst if val%2==0]
print(el)
print("odd number")
ol=[val for val in lst if val%2!=0]
print(ol)