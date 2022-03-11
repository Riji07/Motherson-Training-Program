
#de summation():
#a = int(input("enter first number: "))
#b = int(input("enter second number: "))
#sum = a + b
#print("sum:", sum)

#summation()



#a = int(input("enter first number: "))
#b = int(input("enter second number: "))
#d=(a,b)
#e=dict([('a',a),('b',b)])
#if a>b:
    #print(list(d))
#elif b>a:
    #print(e)   


#def add_num(a,b):
    #sum=a+b;
    #return sum;
#num1=int(input("input the number one: "))
#num2=int(input("input the number two :"))
#print("The sum is",add_num(num1,num2))





# def my_function(a,b):
#     x=a>b;
#     return x;
# num1=int(input("input the number one: "))
# num2=int(input("input the number two :"))
# d=(num1,num2)
# e=dict([('a',num1),('b',num2)])
# if num1>num2:
#     print(list(d))
# elif num2>num1:
#     print(e) 
# print(my_function(num1,num2))







#a=int(input('enter first term'))
#d=int(input('enter common difference'))
#n=int(input('enter number of terms'))
#m=1
#while(m<=n):
    #tm=a+(m-1)*d
    #print(tm)
    #m=m+1
#total=(n*(2*a+(n-1)*d))/2
#print("The sum of AP Series=",total)   



#import os
#def makdir(name):
    #os.mkdir(name)
#makdir('Slot')
 





def print_arithmetic_progression(a, d, n):
    current_value = a

    for i in range(0, n):
        print(current_value, end=' ')
        current_value = current_value + d
a = int(input('Enter the start number: '))
d = int(input('Enter the common difference: '))
n = int(input('Enter total numbers to print: '))
print_arithmetic_progression(a, d, n)

def sumofAP(a, n, d):
    total = (n * (2 * a + (n - 1) * d)) / 2
    return total
a = int(input("Enter First Number: "))
n = int(input("Enter the Total Numbers: "))
d = int(input("Enter the Common Difference : "))
total = sumofAP(a, n, d)
print(total)