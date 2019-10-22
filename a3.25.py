from math import *
num=int(input("Enter the number to check for armstrong: "))
lt=num
b=0
su=0
while num!=0:
    b=num%10
    num=num//10
    su+=pow(b,3)
print("It is armstrong number" if lt==su else "It is not armstrong number")
