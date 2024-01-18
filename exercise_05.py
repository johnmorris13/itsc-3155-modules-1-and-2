list1= [int(input("Enter a number for the first list: ")) for i in range(5)]
list2= [int(input("Enter a number for the second list: ")) for i in range(5)]
print("First List: ",list1)
print("Second List: ",list2)
common=list(set(list1)&set(list2))
print("Common List: ",common)