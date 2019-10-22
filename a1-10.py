days=int(input('Enter number of days: '))
# Approch one
year=0
week=0
day=0
year=days//365
week=(days%365)//7
day=(days%365)%7
print('Number of {} days = {} year, {} week and {} days'.format(days,year,week,day))
#approch two
# directly converting the number of days into numnber of year and week.
