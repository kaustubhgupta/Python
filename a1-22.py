year=int(input("Enter the year: "))
print('It is leap year ' if ((year%4==0 or year%100!=0) and year%400==0) else "It is not a leap year")
