import datetime

start = datetime.datetime.now()

a = 3
i = 1
x = 0
while a * i < 1000:
    x += a * i
    i += 1

b = 5
i = 1
y = 0
while b * i < 1000:
    y += b * i
    i += 1

end = datetime.datetime.now()

print "Time(ms): " + str(end.microsecond - start.microsecond)
print "Answer:   " + str(x + y)