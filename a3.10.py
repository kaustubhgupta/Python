n=int(input("Enter the number: "))
l=0
while n!=0:
    b=n%10
    n=n//10
    l+=1
print("{} Digits".format(l))
