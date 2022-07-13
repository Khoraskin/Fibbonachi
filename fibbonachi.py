n, num1, num2 = int(input()), 0, 1
for i in range(1,n+1):
    num3 = num2
    num2 = num3 + num1
    num1 = num3
    print(num3, end = " ")
