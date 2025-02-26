#Proghram for Creating Date and Time
#DateTimeCreate.py
import datetime
print("-------------Method-1------------------------")
oldt=datetime.datetime(2019,3,19)
newdat=datetime.datetime(2025,3,19)
print("Date1=",oldt)
print("date2=",newdat)
dt=newdat-oldt # here dt is an object <class, datetime.timedelta>
print("Diff({},{})={}".format(newdat,oldt,dt))
print("-------------Method-2------------------------")
date1 = datetime.date(2019, 3, 19)
date2 = datetime.date(2025, 3, 19)
difference = date2 - date1
print("Diff({},{})={}".format(date2,date1,difference))
print("-------------Method-3------------------------")
date_str1 = "2025-03-19"
date_str2 = "2019-03-19"
datetime1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
datetime2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
difference = datetime1 - datetime2
print("Diff({},{})={}".format(date_str1,date_str2,difference))
print("-------------Method-3------------------------")
datetime1 = datetime.datetime(2025, 2, 26, 12, 00, 0)
datetime2 = datetime.datetime(2025, 2, 26, 12, 10, 0)
difference = datetime2 - datetime1
difference_in_seconds = difference.total_seconds()
print("Diff({},{})={}".format(datetime2,datetime1,difference_in_seconds))
