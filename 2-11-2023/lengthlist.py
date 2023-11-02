listword=input("enter the  list of words:").split()
maxlen=len(listword[0])
word=listword[0]
for i in listword:
    if(len(i)>maxlen):
        maxlen=len(i)
        word=i
print("The longest word:")
print(word)
print(len(word))
print("The length of longest word:")
