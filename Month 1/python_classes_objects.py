       #Create a class
class MyClass:
  x = 5
print(MyClass)

       #Create object
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)   

       #The _init_() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

       #Object methods
class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is"+self.name)
p1=Person("John",36)
p1.myfunc()   

       #The self parameter
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("Hello my name is"+abc.name)
p1=Person("John",36)
p1.myfunc()   

       #Modify object properties
class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is"+self.name)
p1=Person("John",36)
p1.age=40
print(p1.age)

       #Delete object properties
class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is"+self.name)
p1=Person("John",36)
del p1.age
print(p1.age)

       #Delete objects
class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is"+self.name)
p1=Person("John",36)
del p1
print(p1)   

       #The pass statement
class Person:
    pass
       


       