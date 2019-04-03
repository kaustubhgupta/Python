def verdit(m1,m2,m3,m4=6000):
    "Calculating if you can buy a smartphone or not"
    total=m1+m2+m3
    if total>m4:
        print("Congracts! you can buy a smartphone!")
    else:
        print("Sorry, You need to wait a little more!")
    return

a=int(input("Enter the money saved from gifts:"))
b=int(input("Enter the money saved from pocket money:"))
c=int(input("Enter the money saved from other sources:"))
verdit(a,b,c,5000)
#it means that if we do not provide a value while calling a function, it will take the defaulr value in the function, Also these defalut and arugumnet values are typed at the end 
