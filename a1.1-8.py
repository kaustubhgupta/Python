char=input("Enter any alphabet: ")
vow=['a','e','i','o','u','A','E','I','U','O']
chk=0
for i in range(len(vow)):
    ch=vow[i]
    if char is ch:
        chk=1
        break
    
print("It is vowel" if chk==1 else "It is not a vowel")
