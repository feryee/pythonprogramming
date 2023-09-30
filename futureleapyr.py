print(" start year")
C=int(input("enter current year:"))
print("Last year")
L=int(input("enter last year:"))
for year in range(C,L):
    if(year%4==0)and(0!=year%100):
        print(year)
        
