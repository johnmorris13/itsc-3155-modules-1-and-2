one=input("Enter a string: ")
two=input("Enter another string: ")
result=False
if one.endswith(two) or two.endswith(one):
    result=True
print(result)