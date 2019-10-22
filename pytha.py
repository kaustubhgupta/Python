def other(n):

    if(n & 1):

        if(n==1):            
            print(-1)
        else:
            b=(n*n-1)//2
            c=(n*n+1)//2
            print("one side=" ,b," other =",c)
    else:
        if(n==2):
            print(-1)
        else:
            b=(n*n)//4 -1
            c=(n*n)//4 +1
            print("one side=" ,b," other =",c)


a=int(input())
other(a)
            
