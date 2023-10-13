n=(input("enter string that has repeated words:"))
print("the original string is:",n)
b="$"
c=n[0]+n[1:].replace(n[0],b)
print("replaced string is:",[c])
