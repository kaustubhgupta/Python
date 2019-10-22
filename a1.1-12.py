month_days={1:'31',2:'28 Days for non leap year and 29 days for leap year',3:'31',4:'30',5:'31',6:'30',7:'31',8:'31',9:'30',10:'31',11:'30',12:'31'}
num=int(input("Enter tge month bnumber: "))
print("{} days".format(month_days.get(num)))
