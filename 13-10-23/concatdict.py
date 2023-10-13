a={1:10,2:20}
b={3:30,4:50}
print("The first dict is:")
print(a)
print("The second dict :")
print(b)
c={}
for d in (a,b):
    c.update(d)
print("The concatenated dictionary is :")
print(c)
