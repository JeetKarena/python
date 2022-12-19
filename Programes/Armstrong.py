num = int(input("Enter Number : "))
n = num
rev = 0

while num != 0:
    if len(str(n)) >= 4:
        rev += pow(num % 10, len(str(n)))
    else:
        rev += pow(num % 10, 3)
    num = num//10
if rev == n:
    print("Given Number is Armstrong")
else:
    print("Given Number is not Armstrong")
