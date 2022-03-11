x=5
t="John"
print(x)
print(t)
x=4 #x is type int
x="Sally" #x is type str
print(x) #creating variables
x=str(3) #x will be "3"
t=int(3) #t will be 3
u=float(3) #u will be 3.0 
print(x)
print(t)
print(u) #casting
q=5
w="John"
print(type(q))
print(type(w)) #get the type
e="John"
# # is the same as
e='John'
print(e) #single or double quotes
r=4
R="Sally"
#R will not overwrite r
print(r)
print(R) #case-sensitive
myvar="John"
my_var="John"
_my_var="John"
print(myvar)
print(my_var)
print(_my_var) #variable names
myVariableName="Joh" #multi words variable names
print(myVariableName) #Camel case
MyVariableName="Jane"
print(MyVariableName) #Pascal case
my_variable_name="Jopp"
print(my_variable_name) #Snake case
m=n=b="Orange"
print(m)
print(n)
print(b) #one value to multiple variables
x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z) #many values to multiple variables
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z) #unpack a collection
x="awesome"
print("Python is"+ x) #output variables
x="Python is"
y="awesome"
z=x+y
print(z)
x=5
y=10
print(x+y)
x="awesome"
def myfunc():
     print("Python is"+x)
myfunc()    #global variables
x="awesome"
def myfunc():
     x="superb"
     print("Python is"+x)
myfunc()
print("Python is"+x)    
def myfunc():
     global x
     x="superb"
myfunc()
print("Python is"+x) #global keyword
x="awesome"
def myfunc():
    global x
    x="superb"
myfunc()

print("Python is"+x)    
print(myfunc.__doc__)
