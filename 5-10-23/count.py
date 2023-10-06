list=["ferin","shaana","amina","saraa"]
count=0
a=input("enter the letter to find:-")
for i in list:
    for x in i:
        if x=='a':
            count=count+1
print("The occurrence of 'a' is :",count)
