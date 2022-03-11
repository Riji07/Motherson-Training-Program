import argparse
from fileinput import filename

# parser=argparse.ArgumentParser()

# print(p['ile_name'])


# def read_txt(name):
#     g = open(name,'r')
#     # readline 

    # for line in g:
    #     output =line.tile()
    #     return output


# if __name__ == "__main__":
#     parser.add_argument("--ile_name",type= type = argparse.FileType('r'),required=True)
#     p = p = vars(parser.parse_args())
#     text = read_txt(p['ile_name'])
#     print(text)


# if __name__=='__main__':
#     parser=argparse.ArgumentParser()
#     parser.add_argument('num1',help="Number 1",type=int)
#     parser.add_argument('num2',help="Number 2",type=int)
#     parser.add_argument('operation',help="provide operator")
#     args=parser.parse_args()
#     print(args)
#     result=None
#     if args.operation=='+':
#         result=args.num1+args.num2 
#     print(result)


# parser = argparse.ArgumentParser()
# parser.add_argument('filename', type=argparse.FileType('r'))
# args=parser.parse_args() 
# for line in args.filename:
#     output = line.title()
#     line=output.split()
#     print(output)
# print(args.filename.readline())





# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print(args.square**2)







# parser = argparse.ArgumentParser()
# parser.add_argument('filename', type=argparse.FileType('r'))
# args=parser.parse_args() 
# number_of_words = 0
# for lines in args.filename:
# 	data = args.filename.read()
# 	lines = data.split()
# 	number_of_words += len(lines)
# print(number_of_words)
















parser = argparse.ArgumentParser()
parser.add_argument('filename', type=argparse.FileType('r'))
args=parser.parse_args() 
x=re.search("#(\s|^)([a-z0-9-_]+)#i",args.filename)
print(x)
print(args.filename.readline())



