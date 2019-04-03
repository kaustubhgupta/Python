day=0
sq=0
total=0
print('Enter number of quats each day')

while day<=6:
    day=day+1
    sq=int(input('Enter the number of quats on {} day '.format(day)))
    total+=sq
avg=total/day
print('Average sqats is {} per day'.format(avg))
