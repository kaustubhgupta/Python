line=input("Enter the string: ")
pos=0
neg=0
zer=0
char=0
for i in line:
    if (i>'0' and i<='9'):
        pos+=1
    if (i<'0'):
        neg+=1
    if (i=='0'):
        zer+=1
    if ((i>='a' and i<='z') or (i>='A' and i<='Z')):
        char+=1

print("{} positive\n{} negative\n{} zeroes\n{} characters".format(pos,neg,zer,char))
