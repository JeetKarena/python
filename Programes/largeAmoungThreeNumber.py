num1=int(input("Enter Number One : "))
num2=int(input("Enter Number Two : "))
num3=int(input("Enter Number Three : "))

"""
    mx = (n1 if (n1 > n2 and n1 > n3) else
     (n2 if (n2 > n1 and n2 > n3) else n3))

"""
# By Using Ternary
print(f" {num1} is large " if num1>num2 and num1>num3 else f" {num2} is large " if num2 > num1 and num2 > num3 else f"third  {num3} is large ")