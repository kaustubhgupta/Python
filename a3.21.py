num=int(input("Enter the number for factorial: "))
b=1
while num!=0:
    b=b*num
    num-=1
print("Factorial is {}".format(b))
