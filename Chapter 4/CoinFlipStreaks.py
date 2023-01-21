#random.choice(['H','T'])
import random
numStreaks = 0
Streaks = 0
for experimentNo in range(10000):
    lst = []
    for i in range(100):
        a = random.choice(['H','T'])
        lst.append(a)
    for i in range(1,100):
        if lst[i] == lst[i-1]:
            Streaks += 1
        else :
            Streaks = 0
        if Streaks == 6 :
            numStreaks += 1
chance = numStreaks/100
print(f'The Chance of a streak happening is {chance}')