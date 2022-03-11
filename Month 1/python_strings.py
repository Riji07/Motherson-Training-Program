       #strings
print("Hello")
print('Hello')       
       #strings

       #assign string to a variable
a="Hello"
print(a)
       #assign string to a variable

       #multiline strings
a="""jdhbjsdbcjbjbdcjashdcb,
jdcvdhcbjasbckjabj,
usdyvcjasvcjsb
jdhcbjasbckjjs."""
print(a)       

a='''ucausbcjbjascbau,
iudbkabksajdbks,
ksbkasjbksajndkjsdnj
uabkasjndksdnkadjn.'''
print(a)
       #multiline strings

       #strings are arrays
a="Hello,World!"
print(a[1])
       #strings are arrays

       #looping through a string
for x in "banana":
    print(x)
       #looping through a string

       #string length     
a="hello world"
print(len(a))
       #string length 

       #check string
txt="The best things in the world are trees"
print("trees" in txt)

txt="The best things in the world are trees"
if "trees" in txt:
    print("Yes,'trees' is present.")
       #check string

       #check if NOT
txt="The best things in the world are trees"
print("expensive" not in txt)

txt="The best things in the world are trees"
if "expensive" not in txt:
    print("No,'expensive' is NOT present.")
       #check if not  

       #slicing
b="hello world"
print(b[2:5])
       #slicing

       #slice from the start
b="Hello world"
print(b[:5])
       #slice from the start

       #slice to the end
b="Hello world"
print(b[2:])
       #slice to the end

       #negative indexing
b="Hello world"
print(b[-5:-2])
       #negative indexing

       #Upper case
a="hello world"
print(a.upper())
       #upper case

       #lower case
a="HELLO WORLD"
print(a.lower())
       #lower case

       #remove whitespace
a=" Hello World "
print(a.strip()) #returns "Hello World"
       #remove whitespace

       #replace string
a="Hello world"
print(a.replace("H","J"))
       #replace string

       #split string
a="Hello, World"
print(a.split(",")) #returns ['Hello', 'World']
       #split string    

       #string concatenation
a="Hello"
b="World"
c=a+b
print(c)

a="Hello"
b="World"
c=a+" "+b
print(c)
       #string concatenation

       #string format
age=36
txt="My name is John, and i am{}"
print(txt.format(age))

quantity=3
itemno=567
price=49.95
myorder="I want{} pieces of item{} for{} dollars."
print(myorder.format(quantity,itemno,price))

quantity=3
itemno=567
price=49.95
myorder="I want to pay{2} dollars for {0} pieces of item{1}."
print(myorder.format(quantity,itemno,price))
       #string format

       #escape character
txt="We are the so-called \"Vikings\" from the north."
print(txt)       



