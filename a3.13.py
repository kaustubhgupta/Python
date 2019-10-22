n=int(input("Enter the number: "))
temp=0
i=0
l=list()
while n!=0:
    temp=n%10
    n=n//10
    l.insert(i,temp)
    i+=1
l.reverse()
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)
i=0
for i in l:
    print(i,end="")
    

    

    

