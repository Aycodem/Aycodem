
"""turtle graphics"""

# import turtle

# ay_turtle=turtle.Turtle()
# ay_turtle.speed(50)

# def squarefuc():
#     ay_turtle.forward(100)
#     ay_turtle.right(90)
#     ay_turtle.forward(100)
#     ay_turtle.right(90)
#     ay_turtle.forward(100)
#     ay_turtle.right(90) 
#     ay_turtle.forward(100)




# def circlefuc():
#   ay_turtle.circle(150)
   
    

# # circlefuc()

# # turtlefuc()

# for count in range(30 ):
#     circlefuc()
"""calender module"""

import calendar


# print(calendar.weekheader(3)) #this print all week in three letter format


# print(calendar.firstweekday()) #this print the index of first week day 

# print(calendar.month(2002 ,3,3)) #this print the month specified in the argument


# print (calendar.monthcalendar(2022,8)) #this print the result of a month in a list format

# print(calendar.calendar(10000)) #this is print the calendar of a year

# print(calendar.weekday(2023,8,31) )

# name1={"kazi","aron","cleverp"}
# name2={"kadi","eron","cleverpd"}


# newname=name1.union(name2)

# at_both_name=name1.intersection(name2)
# diff=name1.difference(name2)

# print(newname)

import datetime
from gettext import install
from itertools import count
from unittest.mock import sentinel

# today=datetime.date.today()
# print(today)

# birthday=datetime.date(1999,11,26) 
# print(birthday)

# day_since_birth=(today-birthday).days

# print(day_since_birth)

# tdelta=datetime.timedelta(days=10)
# print(today + tdelta)

# print (today.weekday()) 

# print(datetime.time(7,2,20,15))   #monday=0 ,sunday=6  

#date.time.date(y,m,d)
#date.time.time(h,m,s,ms)
#date.time.datetime(y,m,d,h,m,s,ms)


# hour_delta=datetime.timedelta(hours=10)    #add 10hours to current day 

# print(datetime.datetime.now()+ hour_delta)

# #go pip install pandas ,pytz,requests for the down code to work
# import pytz

# datetime_today=datetime.datetime.now(tz= pytz.UTC)

# datetime_pacific=datetime_today.astimezone(pytz.timezone("US/Pacific"))
# # print(datetime_pacific)
# # for tz in pytz.all_timezones:
# #     print(tz)

# #strings formatting with dates
# #2019-03-09 -> march 3,2019

# print(datetime_pacific.strftime("%B %d,%Y"))

# #march 09 ,2019 ->datetime(2019,3,9)
# #strptime (p=parsing)
# date_time_thing=datetime.datetime.strptime("March 09, 2019","%B %d, %Y")
# print(repr(date_time_thing))



# How to install maya for date_time_module   

#pipenv install maya

#how to automate stuff with python go for info


# list1=[1,2,3,4,5]
# list2=["one","two","three","four","five"]     #before zipping two list together it must be of the same length
                                                  
# zipped=list(zip(list1,list2))

# unzipped =list(zip(*zipped))

# print(zipped)
# print (unzipped)

items =["apples","banana","orange"]
counts=[3,4,5]
prices=[50,100,200]

sentences=[]

for (item,cont,price) in zip(items,counts,prices):
     item,cont,price=str(item),str(cont),str(price)
     sentence="i bought "+ cont +" "+ item +"'s at " + price +" naira each."
     sentences.append(sentence)


print(sentences)