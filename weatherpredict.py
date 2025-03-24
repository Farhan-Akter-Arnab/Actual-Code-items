weather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,7):
    if (weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if (sunny > rainy):
    print("Sunny weather")
else:
    print("Rainy weather")
weather2 = (1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0)
sunny2 = 0
rainy2 = 0
for i in range(0,30):
    if (weather2[i] == 1):
        sunny2 += 1
    else:
        rainy += 1
if (rainy2 > sunny2):
    print("Rainy weather")
else:
    print("Sunny weather")