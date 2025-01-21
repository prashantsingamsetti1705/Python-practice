#write a python program which will the local var and gobal var
# exp1
def learn_ai():
    sub1="ai"#local var
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub1,lang))
def learn_ml():
    sub2 = "ml"
    print("ml the devlop lang is used study more{}--->by lang of{}".format(sub2, lang))
def learn_ds():
    sub3 = "ds"
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub3, lang))
#mainprogram
lang="python"#gobal var
learn_ai()
learn_ml()
learn_ds()
print("*"*50)
# exp2
lang2="python"#gobal var
def learn_ai():
    sub1="ai"#local var
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub1,lang2))
def learn_ml():
    sub2 = "ml"
    print("ml the devlop lang is used study more{}--->by lang of{}".format(sub2, lang2))
def learn_ds():
    sub3 = "ds"
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub3, lang2))
#mainprogram
learn_ai()
learn_ml()
learn_ds()
print("*"*50)
# exp3
def learn_ai():
    sub1="ai"#local var
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub1,lang3))
lang3 = "python"  # gobal var
def learn_ml():
    sub2 = "ml"
    print("ml the devlop lang is used study more{}--->by lang of{}".format(sub2, lang3))
def learn_ds():
    sub3 = "ds"
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub3, lang3))
#mainprogram
learn_ai()
learn_ml()
learn_ds()

# exp3
def learn_ai():
    sub1="ai"#local var
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub1,lang4))
    # print(sub2,sub3)#it is local varabel to other fuction
def learn_ml():
    sub2 = "ml"
    print("ml the devlop lang is used study more{}--->by lang of{}".format(sub2, lang4))
    # print(sub1, sub3)  # it is local varabel to other fuction
def learn_ds():
    sub3 = "ds"
    print("ai the devlop lang is used study more{}--->by lang of{}".format(sub3, lang4))
    # print(sub2, sub1)  # it is local varabel to other fuction
#mainprogram
lang4="python"
learn_ai()
learn_ml()
learn_ds()
# lang4="python"--->NameError: name 'lang4' is not defined. Did you mean: 'lang'?