#CurrentDateDayInfo.py
from datetime import datetime
td=datetime.now()
print("current date and time")
print(td)
print("-------------------------------------")
print("Day Number of Year=",td.strftime("%j"))
print("Week Number of Year(Sunday Starts)=",td.strftime("%U"))
print("Week Number of Year(Monday Starts)=",td.strftime("%W"))
print("Century=",td.strftime("%C"))
print("Local Version of date =",td.strftime("%x"))
print("Local Version of time=",td.strftime("%X"))
print("-------------------------------------")
print("Week Day(ISO-8601):",td.strftime("%u"))
print("Week Number(ISO-8601):",td.strftime("%V"))

#CurrentDateHourInfo.py
from datetime import datetime
td=datetime.now()
print("current date and time")
print(td)
print("-------------------------------------")
print("Hour in 24 Hours Format:",td.strftime("%H"))
print("Hour in 12 Hours Format:",td.strftime("%I"))
print("Are we in AM / PM:",td.strftime("%p"))
print("Minutes:",td.strftime("%M"))
print("Seconds:",td.strftime("%S"))
print("Micro Seconds:",td.strftime("%f"))