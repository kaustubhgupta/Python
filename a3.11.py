n=int(input("Enter the number: "))
f=0
l=n%10
while n!=0:
    f=n%10
    n=n//10
print("First Digit: {}\nSecond Digit: {}".format(f,l))
    

