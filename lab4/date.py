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
# firstdate = datetime.date.today()
# seconddate = datetime.date(2005, 11, 1)
firstdate = map(int, input("Write the first date (YYYY-MM-DD): ").split("-"))
seconddate = map(int, input("Write the second date (YYYY-MM-DD): ").split("-"))
y, m, d = [int(i) for i in firstdate]
y2, m2, d2 = [int(j) for j in seconddate]
delta = abs(datetime.date(y, m, d) - datetime.date(y2, m2, d2))
print(delta.total_seconds())


