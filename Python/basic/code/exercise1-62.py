seconds = 200

if seconds>60:
    minutes=seconds // 60
    seconds-=minutes*60
else:
    minutes=0
print(minutes, "min ", seconds, "sec")