import datetime

yestorday = datetime.datetime.now() - datetime.timedelta(days=1)
today=datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

print(yestorday)
print(today)
print(tomorrow)