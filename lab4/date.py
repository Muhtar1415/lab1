#task1
import datetime
date_time=datetime.datetime.today()
current_time=date_time-datetime.timedelta(5)
print(current_time)

#task2
from datetime import date,  timedelta, datetime

date1=datetime.now()-timedelta(1)
yesterday=date1.strftime("%d-%m-%Y")
print("Yesterday: ", yesterday)

date2=datetime.now()
today=date2.strftime("%d-%m-%Y")
print("Today: ", today)

date3=datetime.now()+timedelta(1)
tomorrow=date3.strftime("%d-%m-%Y")
print("Tomorrow: ", tomorrow)

#task3
from datetime import date,  timedelta, datetime
time=datetime.now()
milisec=time.strftime("%Y-%m-%d, %H:%M:%S")
print(milisec)

#task4
from datetime import date,  timedelta, datetime
date1=datetime.now()-timedelta(1)
date2=datetime.now()+timedelta(1)

time1=datetime.timestamp(date1)
time2=datetime.timestamp(date2)
dif=time2-time1
print(dif)