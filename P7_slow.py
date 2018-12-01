import time

zaman = time.time()
def asalmi(num):
    asal = 0
    if num == 2:
        asal = 1
        return asal
    for i in range(2,num):
       if (num % i) == 0:
           asal = 0
           break
       else:
           asal = 1
    return asal

def kacinciasal(kacinci):
    kac = 0
    for i in range(kacinci**2):
        if asalmi(i) == 1:
            kac += 1
        if kac == kacinci:
            print(f"{kacinci} = {i}")
            break
    return 0
print(kacinciasal(10001))
print(time.time()-zaman)