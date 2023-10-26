list=[10,22,50,25,40,14]
print("orginal list:-")
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("list after removing even number:")
print(list)
