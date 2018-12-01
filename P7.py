import time

s = time.time()

def asalmi(x):
    y = 2
    while y**2 <= x:
        if x%y == 0:
            return 0
        y += 1
    return 1

asal = 2
sayac = 0
while sayac < 10001:
    if asalmi(asal) == 1:
        print(asal)
        sayac += 1
    asal += 1

print(time.time() - s)