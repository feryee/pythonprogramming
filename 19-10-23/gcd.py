a=int(input("enter the 1st num:-"))
b=int(input("enter the 2st num:-"))
i=1
while(i<a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i
    i=i+1
print("THE GCD IS:- ",gcd)
