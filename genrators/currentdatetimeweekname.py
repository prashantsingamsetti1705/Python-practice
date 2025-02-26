#currentdatetimeweekname.py
from datetime import datetime
td=datetime.now()
print("current date and time")
print(td)
print("-"*50)
#get week name in short---use %a
print("short of week name:",td.strftime("%a"))#wed
print("full week name:",td.strftime("%A"))#wednesday
print("-"*50)
print("week number :",td.strftime("%w"))
print("day of the month:",td.strftime("%d"))
