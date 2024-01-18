str=input("Enter a string: ")
upper=''
restofstr=''
for x in str:
    if x.isupper():
        upper+=x
    elif not x.isspace():
        restofstr+=x
print_str=restofstr+upper
print(print_str)