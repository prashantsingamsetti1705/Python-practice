#write a python program to print roman number to normal number
# Python program to convert Roman
rn=input("enter a roman number u wamt to generate normal number")
if len(rn)==0:
    print("invalid input{}".format(rn))
else:
    if(rn.islower()):
        print("{} is invalid input".format(rn))
    else:
        nv=0
        for i in range(len(rn)):
            if rn[i]=="I":
                cv=1
            elif rn[i]=="V":
                cv=5
            elif rn[i]=="X":
                cv=10
            elif rn[i]=="L":
                cv=50
            elif rn[i]=="C":
                cv=100
            elif rn[i]=="D":
                cv=500
            elif rn[i]=="M":
                cv=1000
            else:
                cv=0
            if i+1<len(rn):
                if(rn[i]=="I" and rn[i+1] in "VX") or (rn[i]=="X" and rn[i+1] in "LC") or (rn[i]=="C" and rn[i+1] in "DM"):
                    nv=nv-cv
                else:
                    nv=nv+cv
            else:
                nv=nv+cv
        print("{}this value is{}:".format(rn.upper(),nv))
#using dict
roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

rn = input("Enter a Roman numeral you want to convert to a normal number: ")
if len(rn) == 0:
    print("Invalid input: {}".format(rn))
else:
    if rn.islower():
        print("{} is invalid input".format(rn))
    else:
        nv = 0
        for i in range(len(rn)):
            cv = roman_dict.get(rn[i], 0)

            if i + 1 < len(rn):
                if (rn[i] == "I" and rn[i + 1] in "VX") or (rn[i] == "X" and rn[i + 1] in "LC") or (
                        rn[i] == "C" and rn[i + 1] in "DM"):
                    nv = nv - cv
                else:
                    nv = nv + cv
            else:
                nv = nv + cv

        print("{} has the value: {}".format(rn, nv))