       


       #Use a module
import mymodule
mymodule.greeting("Jonathan")

       #Variables in module
import mymodule

a = mymodule.person1["age"]
print(a)   

       #Re-naming a module
import mymodule as mx
a = mx.person1["age"]
print(a)   

       #Built_in modules
import platform
x = platform.system()
print(x)     

       #Using the dir() Function
import platform
x = dir(platform)
print(x)       

       #Import from module
from mymodule import person1
print (person1["age"])       
