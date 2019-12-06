import datetime
print(datetime.datetime.now().day)

x=datetime.datetime(2020,5,5)
print(x)

print(x.strftime("%b"))

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%c"))
print(x.strftime("%R"))


