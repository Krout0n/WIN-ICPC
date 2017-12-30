import datetime

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

while True:
    m,d = [int(i) for i in input().split()]
    if not(m or d):
        break
    print(weekdays[datetime.date(2004, m, d).weekday()])
