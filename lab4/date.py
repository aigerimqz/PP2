import datetime
#ex 1
# curdate = datetime.date.today()
# sub = curdate - datetime.timedelta(days=5)
# print(sub)


#ex 2
# keshe = datetime.date.today() - datetime.timedelta(days=1)
# bugin = datetime.date.today()
# erten = datetime.date.today() + datetime.timedelta(days=1)

# print("yesterday:", keshe)
# print("today", bugin)
# print("tomorrow:", erten)


#ex 3
# curtime = datetime.datetime.now()
# dropped = curtime.replace(microsecond=0)
# print(curtime)
# print(dropped)


#ex 4
firstdate = datetime.date.today()
seconddate = datetime.date(2005, 11, 1)
delta = abs(firstdate - seconddate)
print(delta.total_seconds())


