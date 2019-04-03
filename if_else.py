price=int(input('Enter the price of donut:$ '))
qty=int(input('Enter the quantity of donuts purchased: '))
total=price*qty


if total>1000:
    print('You are applicable for Discount')
    discount=(total*10)/100
    total-=discount
    print("Discounted price:{}".format(total))
else:
    print("No discount")
    print("Total price:{}".format(total))
