#CurrentDateYearInfo.py
from datetime import datetime
td=datetime.now()
print("current date and time")
print(td)
print("-------------------------------------")
print("Month Name in Full=",td.strftime("%B"))
print("Month Name in Short=",td.strftime("%b"))
print("Month Number=",td.strftime("%m"))
print("Year in Short=",td.strftime("%y"))
print("Year in Full=",td.strftime("%Y"))