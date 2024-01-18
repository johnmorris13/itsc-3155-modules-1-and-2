def letter_number(str):
    letters={}
    str=str.lower()
    str=str.replace(" ","")
    for x in str:
        if x in letters:
            letters[x]+=1
        else: letters[x]=1
    return letters
str=input("Enter a string: ")
print(letter_number(str))