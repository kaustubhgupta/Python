num=int(input("Enter the number:"))
for x in range(2,num):
    if num%x==0:
        print("{} is not prime".format(num))
        break
else:
    print("{} is prime".format(num))
        
