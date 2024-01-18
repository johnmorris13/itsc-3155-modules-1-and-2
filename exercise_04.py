number=int(input("Enter a number: "))
numberlist=[]
for i in range(number):
    num=float(input(f"Enter number {i+1}:"))
    numberlist.append(num)
print("List: ",numberlist)
print("Average: ",sum(numberlist)/number)
