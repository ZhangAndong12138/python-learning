# print a time in string

from datetime import date
from datetime import datetime

today = date.today()

year = today.year
month = today.month
day = today.day

print(str(year)+str(month)+str(day)+"\n")

today2 = datetime.now()

print(today2.strftime("%y%m%d%H%M"))
