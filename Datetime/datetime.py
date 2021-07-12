# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:52:54 2020

@author: aishwary
"""

import datetime
# Naive - not enough information about timezone and daylight savings easier to work with
# Aware - have enough information

########### datetime.date ##############
d= datetime.date(2020,3,22)
print(d)
today=datetime.date.today()
print(today.weekday())
print(today.isoweekday())
# weekday monday=0 and sunday=6 for isoweekday monday=1 and sunday=7

tdelta=datetime.timedelta(days=7)
print(today+tdelta)
print(today-tdelta)

# timedelta=date2-date1 (if we add or subtract date we will get time delta)
bday=datetime.date(2020,10,8)
till_bday=bday-today
print(till_bday)
till_bday.days


############## datetime.time ##########
t=datetime.time(12,44,23,10)
print(t)

############## datetime.datetime ##########
dt=datetime.datetime(2020,3,22,12,30,45,100)
print(dt)
print(dt.date())
print(dt.time())
tdelta=datetime.timedelta(hours=12)
print(dt+tdelta)

#datetime now has option of timezone where as today gives os current timezone

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

############ datetime timezone #########
import datetime
import pytz

dt=datetime.datetime(2020,3,22,12,22,45,tzinfo=pytz.UTC)
print(dt)
dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_ist=dt_utcnow.astimezone(tz=pytz.timezone('Asia/Kolkata'))
print(dt_ist)

for tz in pytz.all_timezones:
    print(tz)
    
#### Make naive date time aware
dt_ist=datetime.datetime.now()
dt_est=dt_ist.astimezone(tz=pytz.timezone('US/Eastern'))
print(dt_est)
print(dt_est.isoformat())

print(dt_est.strftime('%B %d, %Y'))

# Format codes are here https://strftime.org/
# strftime - datetime to string
# strptime - string to datetime

#convert string to a datetime 
dt_str='April 24, 2020'
dt=datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)


# Start and end date
import pandas as pd
import datetime
start_date='2020-03-01'
end_date='2020-05-07'

date_list=pd.date_range(start=start_date,end=end_date)

month_list=[]

for i in date_list:
    month=i.strftime('%m')
    if month not in month_list:
        month_list.append(month)

import numpy as np
dl=list(np.arange(1,31,1))
date_list=[]
for i in dl:
    dl1=format(i,'02d')
    date_list.append(dl1)
    
