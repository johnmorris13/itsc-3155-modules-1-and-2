def get_unique_list(userslist):
    unique=[]
    for x in userslist:
        if x not in unique:
            unique.append(x)
    return unique
my_list=[1,2,3,2,1,4]
unique_list=get_unique_list(my_list)
print(unique_list)