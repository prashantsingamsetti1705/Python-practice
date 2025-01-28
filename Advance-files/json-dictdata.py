#write a python json to convert the dict to json file converter
#loads () ---- use to convert the json to dict
import json
js='{"name":"para","id":200,"cit":"hyd"}'
print(js)
print(type(js))
emp_dict=json.loads(js)
print(emp_dict)
print("*"*50)
for k,v in emp_dict.items():
    print("{}---------->{}".format(k,v))
print("*"*50)

