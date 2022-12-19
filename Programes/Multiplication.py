# Multiplication Table Upto N

n = int(input("Enter Number : "))

for i in range(1, n+1):
    for j in range(1, 10+1):
        print('{0:1d}   * {1:3d}  =  {2:2d}'.format(i, j, i*j))
    else:
        print()
