nums=[]
oncenums=[]
for x in range(10):
    n=int(input(f"Enter number {x+1}: "))
    nums.append(n)
for i in nums:
    if nums.count(i)==1:
        oncenums.append(i)
print("Original List: ",nums)
print("Nums that appear once: ",oncenums)