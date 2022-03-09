seconds=5000

if seconds>=3600:
    hours=seconds//3600
    seconds-=hours*3600
else:
    hours=0
if seconds>=60:
    minutes=seconds//60
    seconds-=minutes*60
else:
    minutes=0
print(hours, "hr ", minutes, "min ", seconds, "sec")