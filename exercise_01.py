grade=int(input("Enter a grade from 0 to 100: "))
value=''
if grade<0 or grade>100:
    print("Invalid grade")
elif grade<=59:
    value='F'
elif grade<=69:
    value='D'
elif grade<=79:
    value='C'
elif grade<=89:
    value='B'
elif grade<=100:
    value='A'
if value is not '':
    print("Your grade is ",value)
    