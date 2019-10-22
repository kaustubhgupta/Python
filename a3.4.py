num=int(input("Enter number: "))
i=0
while i!=num:
    if i%2==0:
        i+=1
        continue    
    else:
        print(i+1)
        i+=1
        
