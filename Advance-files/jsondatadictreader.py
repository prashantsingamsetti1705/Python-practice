#write a python program which read the data json file
#load()here json file is ued read json file
import json
try:
    with open("stud1.json","r")as fp:
        record=json.load(fp)
        for k,v in record.items():
            print("{}---------->{}".format(k,v))
except FileNotFoundError:
    print("file does not exist")