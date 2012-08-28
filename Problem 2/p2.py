import datetime

start = datetime.datetime.now()

limit = 4000000

end = datetime.datetime.now()

print "Time(ms): " + str(end.microsecond - start.microsecond)
print "Answer:   " + str(limit)