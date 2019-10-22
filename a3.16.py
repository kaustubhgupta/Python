num=int(input("Enter the number: "))
i=2
state=1
while i<=num//2:
    if num%i==0:
        state=0
        break
    else:
        state=1
    i+=1
print("It is prime" if (state==1 or num==2 or num==3) else "It is not prime")


            
