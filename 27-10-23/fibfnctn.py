def fib(y):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(y-2):
        z=a+b
        print(z)
        a=b
        b=z
y=int(input("Enter the number of terms:"))
fib(y)
