hour,min = input().split()
hour = int(hour)
min = int(min)

if(45<=min):
    min -= 45
elif(min<45):
    # min + 60 - 45
    min = min + 15 
    if(hour == 00):
        hour = 23
    else:
        hour -= 1
print(hour, min)

