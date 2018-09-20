age = int(input('Please enter your age:'))

if age > 21:
    print('yes, you can.')
    
else:
    print ('sorry, you cannot.')

import time
time.time()
1437746094.5735958

days = ut / (60 * 60 * 24)
hour = days % int(days) * 24
min  = hour % int(hour) * 60
sec  = min % int(min) * 60

print(f"Days: {int(days)}\nTime: {int(hour)}:{int(min)}:{int(sec)}")