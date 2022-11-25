num1=int(input("Enter Number One : "))
num2=int(input("Enter Number Two : "))

print(f"Number One is {num1} and Two is {num2} ")

"""
By Using temp variable

temp=num1
num1=num2
num2=temp 

"""
# By Using ExOr 
num1=num1^num2
num2=num2^num1
num1=num1^num2

print(f"Number One is {num1} and Two is {num2} ")