num=int(input("Enter number upto which you want series: "))
a=0
b=1
i=0
if num==1:
    print(a)
else:
    while i<num:
        print(a,end=" , ")
        c=a+b
        a=b
        b=c
        i+=1
