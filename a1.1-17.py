from math import *
a,b,c=input("Enter values of A, B & C: ").split()
a=int(a)
b=int(b)
c=int(c)
d=pow(b,2)-4*a*c
if d>=0:
    print("Roots are: {} {}".format(-b+sqrt(d)/2*a ,-b-sqrt(d)/2*a))
else:
    print("Roots are imaginary")
