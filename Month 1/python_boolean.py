       #boolean values
print(10>9)
print(10==9)
print(10<9)

a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")
       #boolean values

       #evaluate values and variables
print(bool("Hello"))
print(bool(15))

x="Hello"
y=15
print(bool(x))
print(bool(y))

       #most values are true
print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))
       #most values are true

       #some values are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def _len_(self):
        return 0
myobj=myclass()
print(bool(myobj))

       #functions can return a boolean
def myFunction():
    return True
print(myFunction())

def myFunction():
    return True
if myFunction():
    print("YES")
else:
    print("NO")

x=200
print(isinstance(x,int))




