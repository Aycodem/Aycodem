class Myclass:
    x=5
class1=Myclass()
print(class1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("john",35)
print(p1.name)
print(p1.age)

#delete with (del p1.age )

# pass can help bypass error in code
# class suspend_code:
#     pass


#Inheritance in python

# class student():
#     name = "tim"
#     age = 34
#     gender="male"

# class person(student):
#     pass


# p1= person()

# print(p1.name)