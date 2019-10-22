num1=int(input("Enter first number(num1): "))
num2=int(input("Enter second number(num2): "))
num3=int(input("Enter second number(num3): "))
print("All are equal" if (num1==num2 and num1==num3) else "num1 is greatest" if (num1>num2 and num1>num3) else "num2 is greatest" if (num2>num1 and num2>num3) else "num3 is greatest") 
# using nested if-else ternary opertaor
