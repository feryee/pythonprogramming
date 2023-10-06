n=int(input("enter the  limit:"))
b=[]
v="over"
for i in range(0,n):
    a=int(input("enter the elements:"))
    if a<99:
        b.append(a)

    else:
        b.append(v)
print(b)
    
