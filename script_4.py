sum=0
for x in range(5):
    while True:
        num=input(f"Enter int {x+1}: ")
        if num.isdigit():
            sum+=int(num)
            break
        else: print("Invalid. Please enter an int.")
print("Your sum is ",sum,".")