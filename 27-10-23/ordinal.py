Factorial

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter a number:"))
print("The factorial of",n,"is" ,factorial(n))

lambda

a=int(input("Enter the side of the square \n"))
area = lambda b:b*b
print("area of square",area(a))

a=int(input("Enter the length of the rectangle"))
b=int(input("Enter the breadth of the rectangle"))
area=lambda l,b:l*b
print("Area of the rectangle is",area(a,b))

a=int(input("Enter the height of the triangle \n"))
b=int(input("Enter the breadth of the triangle \n"))
area=lambda h,b:h*b
print("Area of triangle is",area(a,b))

Fibonnacci using function
def fib(j):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(j-2):
        z=a+b
        print(z)
        a=b
        b=z
j=int(input("Enter the number of terms:"))
fib(j)


Pyramid
j=int(input("Enter the number of terms:"))
 
def pyramid(j):
    for i in range(1,j+1):
        for n in range(1,i+1):
            print(n*i,end=" ")
        print("\n") 
pyramid(j)
Ordinal
a = input("Enter the word \n")
for i in a:
    print(ord(i),"\n")
