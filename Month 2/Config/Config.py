from configparser import ConfigParser
config=ConfigParser()
config.read("Path.ini")
path=config["Default"]["Path"]
text=open(path,"r")
file=text.read()
print(file)
Counter = 0
Lines =file.split("\n")
for i in Lines:
    if i:
        Counter += 1
print("This is the number of lines in the file")
print(Counter)


