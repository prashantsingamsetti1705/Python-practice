#write a python a python program dict to jon file
#dump()
d={"name":"prash","id":100,"city":"hyd"}
print(d,type(d))
#covrt the dict in to json
#Convert Dict Data into JSON Data  (str data)--- we use
js=str(d)
print(js,type(js))

#wite a python program which convert the dict into json
import json
#dict for mat
emp_dict={"en":"prashat","eno":100,"esal":20.0}
print("*"*50)
with open("stud1.json","w") as fp:
    rec=json.dump(emp_dict,fp)
    print("file ctrated sucess fully---->verify")