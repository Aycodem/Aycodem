#float(65)
x =" coolyeah"
# y = "hello who dey"
print (x[3])
#print(x[1:3]) slicing in pyton
#print([x.split(" ")])
# print( y + x )
# greet="hello how are u python"
# new_greet =greet.replace("python","html")
# print(new_greet)

#a =[1,2,3,4,5]
# a.insert(0,4)
# a.sort()
# max(a)
# min(a)
# len(a)
# b=[3,2,1,4,5,6,7]
#b[0:1] = ["HELLO","HI","good"]
#b.append(8)
#b.extend([8,9,10])
#b.pop()
#x=tuple(b)
#(a,b,c,d,e,f,j)=x

#dictionaries

from collections import OrderedDict
from sre_parse import State

# d ={"apple":"red","orange":"yellow","mango":"green"}
#d["watermelon"]="red"
#d.keys()
#d.items()
#d.values() 
#d.clear()
#d.pop(key)
#del d['apple'] it delete the key "apple"
#d.popitem()
#x=dict([("facebook","blue"),("youtube","red")])
#d.update(x)
# import math
# math.trunc()
# print (math.exp(3)) 

#conditional statement

# if 50<30: print ("yeah 50 is greater")
# elif "hello" == "helo": print("yo,hello")
# elif 20>18 :print("yes it is greather")
# else:print ("nothing to\n show")

# age =26
# x="adult" if age>18 else "child"

# print(x)

# while loop
# n = 0

# while n <=5:
#      n+=1
#      print("value of n is = " , n)
# print("please enter your name")
# number = int(input())
# print(number)

# x=[1,2,3,4,5]

# for i in x:
#     print(i,x)




# a = {"first":1 ,"second":2,"third":3}
# iter_a =iter(a.keys())

# for i in iter_a: print(i)

# print(str(input("input number between range 1 and 20\n")))
# from math import pi

# class Circle():
#      """a Circle instance models a circle with a radius"""

#      def _init_(self,radius=1.0):
#         """initializer with default radius of  1.0"""
#         self.radius = radius #create an instance variable radius

#      def _str_(self):
#         """return a descriptive string for this instance ,invoked by print() and str()"""
#         return "this is circle with radius of {:.2f}",format(self.radius)
 
#      def _repr_(self):
#         """Return a descriptive string that can be used to re-create this instance ,involked by repr()"""
#         return "Circle (radius={})".format(self.radius)

#      def get_area(self):
#         """Return the area of this circle instance """
#         return self.radius * self.radius * pi




# c1=Circle(2.1)
# print(c1)

# class Country:
#     def ShowCountry(self):
#         print("this is india")




# class State:
#     def ShowState(self):
#         print("this is state")

# st= Country()
# st2=State()
# st.ShowCountry()
# st2.ShowState()


#print (f"{40-23} new messages") #this help to print number and strings together

# fucttion in pyton

# def funname():
#     """This is a doc string"""
#     return "hello"

# print(funname())
# import sys

# print(sys.platform)

  

# import os

# print(os.getcwd())
#while loop

# numberofage=0
# while numberofage <= 20:
#     numberofage+=1
#     print("wooh,it still lesser:",numberofage)
 
#creating a new list from an existing one 

# fruits =["mango","apple","orange","banana","watermelon"]

# newlist=[each_fruit for each_fruit in fruits if "e" in each_fruit]

# print(newlist)

""" or"""
  

# fruits =["mango","apple","orange","banana","watermelon"]

# newlist=[]

# for each_fruit in fruits:
#     if "e" in each_fruit:
#         newlist.append(each_fruit)

# print(newlist)


# evennumberlist=[x for x in range(10) if x%2 == 0  ] #creating even number list

# oddnumberlist=[x for x in range(10) if x%2 == 1  ] #creating odd number list

# print(evennumberlist + oddnumberlist)

# obj=["even" if i%2 ==0 else "odd" for i in range(20) ]

# print(obj)



# x = lambda a,b: a+b  #lambda function that have one condition

# print(x(3,4))

""""map,filter,reduce in python"""

# items=[1,2,3,4,5,6,7]

# sqr=lambda x: x**2

# def sqr(x):
#     return x ** 2

# mapnumberlist=list(map(sqr,items))

# print(  mapnumberlist  )           #map in python

# filternumberlist=list(filter(lambda x: x<3 ,items))   #filter in python

# print(filternumberlist)

#from functools import reduce

# items=[1,2,3,4,5,6,7]

# sumoflist= 0

# for num in items:
#     sumoflist+=num
                                       
# print(sumoflist)

"""or"""
                                             #reduce in python
# sumoflist=sum(items)

# print(sumoflist)

"""or"""

# sumoflist= lambda x:sum(x)

# print(sumoflist(items))




# letter=[i for i in [1,2,3,4,5,6]]
# print(letter)
# print("using the enumerate function")

# for index,element in enumerate(letter):
#     print("index\t[" +str(index) + "]","\t"+"values\t",element)


# teama={1: "david", 2: "john", 3: "ruth", 4: "dele"}
# teamb={4: "daid", 5: "jhn", 6: "ruh", 7: "dle"}


# teama.update(teamb)
# print(teama)


# dictthree=teama.copy()
# dictthree.update(teamb)

# print(dictthree)

# dictthree={**teama,**teamb}
# print(dictthree)

