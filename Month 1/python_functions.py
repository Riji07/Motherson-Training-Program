       #Creating a function
def my_function():
    print("Hello from a function")   

       #Calling a function
def my_function():
    print("Hello from a function")
my_function()  

       #Arguments
def my_function(fname):
    print(fname+"Refnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")   

       #Number of arguments
def my_function(fname,lname):
    print(fname+lname)
my_function("Emil","Refnes")

       #Arbitrary arguments
def my_function(*kids):
    print("The youngest child is"+kids[2])
my_function("Emil","Tobias","Linus")

       #Keyword Arguments
def my_function(child3,child2,child1):
    print("The youngest child is"+child3)
my_function(child1="Emil",child2="Tobias",child3="Linus")

       #Arbitrary Keyword Arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

       #Default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

       #Passing a list as an argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)   

       #Return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))  

       #The pass statement
def myfunction():
  pass

       #Recursion
       


   

