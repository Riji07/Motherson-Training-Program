import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-f",type=argparse.FileType())
args=parser.parse_args(["-f","hello.txt"])
print (type(args.f))
print (args.f.read())
