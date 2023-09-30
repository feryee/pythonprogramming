print("Enter three numbers")
a=int(input("enter the 1st number:-"))
b=int(input("enter the 2nd number:-"))
c=int(input("enter the 3rd number:-"))
if a>b and a>c:
    print("The greatest number is",a)
elif b>c:
    print(b,"is greater")
else:
    print("The greatest is",c)
