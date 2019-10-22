amount=int(input("Enter the amount: "))
twok=amount//2000
amount=amount-twok*2000
five_hundred=amount//500
amount=amount-five_hundred*500
hundred=amount//100
amount=amount-hundred*100
fifty=amount//50
amount=amount-fifty*50
twe=amount//20
amount=amount-twe*20
ten=amount//10
amount-=ten*10
one=amount%10
print("{} 2k notes,{} five hundred notes,{} hundred notes,{} fiftys notes,{} twentys notes,{} tens notes, {} one rupees".format(twok,five_hundred,hundred,fifty,twe,ten,one))
