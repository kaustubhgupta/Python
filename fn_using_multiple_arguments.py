def verdit(m1,m2,m3):
    "Calculating if you can buy a smartphone or not"
    total=m1+m2+m3
    if total>6000:
        print("Congracts! you can buy a smartphone!")
    else:
        print("Sorry, You need to wait a little more!")
    return

a=int(input("Enter the money saved from gifts:"))
b=int(input("Enter the money saved from pocket money:"))
c=int(input("Enter the money saved from other sources:"))
verdit(a,b,c)
