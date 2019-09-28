from datetime import datetime

# getting current date and time
d = datetime.today()
print('Current date and time: ', d)

# getting current year
print('Current year: ', d.year)

# getting current month
print('Current month: ', d.month)

# getting current day
print('Current day: ', d.day)

# getting current hour
print('Current hour: ', d.hour)

# getting current minutes
print('Current minutes: ', d.minute)

# getting current Seconds
print('Current seconds: ', d.second)

# getting current microsecond
print('Current micro seconds: ', d.microsecond)

print('{:01d}h:{:01d}m'.format(*divmod(0, 60)))

print(f'{107237:,}')

print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
