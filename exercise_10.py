text=input("Enter a string:")
characters=list(text)
splitchar=[]
for i in range(0,len(characters),3):
    three=characters[i:i+3]
    splitchar.append(three)
print(splitchar)