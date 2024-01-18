leave=False
nums=[]
while not leave:
    num=input("Enter a number or QUIT to quit: ")
    if num=="QUIT":
        break
    nums.append(int(num))
evens=[]
for i in nums:
    if i%2==0:
        evens.append(i)
print("All Nums: ",nums)
print("Even Nums: ",evens)

