import os
from os import environ
import datetime

print(os.environ['USERNAME'].strip())
print(datetime.datetime.today().strftime('%Y%m%d'))
sys_date = datetime.datetime.today().strftime('%Y%m%d')
print(environ.get('files_date', sys_date))

row_data = [1]
print(type(row_data))
