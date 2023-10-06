n=input("enter the line:")
c=input("Enter the word to count:")
d=n.split()
count=0
for i in d:
    if i==c:
        count=count+1
print("The number of",i,"is",count)
    
