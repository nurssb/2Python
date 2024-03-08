import datetime

date1 = input("Data 1 (yyyy-mm-dd HH:MM:SS): ")
date2 = input("Data 2 (yyyy-mm-dd HH:MM:SS): ")
format = "%Y-%m-%d %H:%M:%S"
date_1 = date1.strftime(format)
date_2 = date2.strftime(format)

result= abs((date_2 - date_1).total_seconds())

print(result)
