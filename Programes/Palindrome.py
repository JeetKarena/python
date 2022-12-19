# Cheack Weather The Number is Palindrome or Not

num = int(input("Enter Number : "))

# First Aproch
rev = str(num)[::-1]
print(rev)

if num == int(rev):
    print("Given Number is Palindrome !")
else:
    print("Given Number is Not Palindrome !")

# Second Aproch

n, rev = num, 0
while num != 0:
    rev = (rev*10)+(num % 10)
    num = num//10
if n == rev:
    print("Number is Pelindrome !")
else:
    print("Number is Not Pelindrome !")
