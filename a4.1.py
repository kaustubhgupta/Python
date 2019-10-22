a,b=input("Enter the numbers for HCF: ").split()
a=int(a)
b=int(b)
i=0
hcf=0
def hcf(a,b):
    if b<a:
        small=b
    else:
        small=a
    for i in range(1, small+1):
        if((a%i==0)and(b%i==0)):
            hcf=i

    return hcf
print("{} is hcf".format(hcf(a,b)))
    
    
    

    
