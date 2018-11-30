sayi = 0
istenen = 0
while True:
    for i in range(1, 21):
        if sayi%i == 0:
            istenen = sayi
        else:
            istenen = 0
            break
    sayi += 10
    if istenen:
        break
print(istenen)

"""
2520, kalan sayı olmadan 1'den 10'a kadar olan sayıların her birine bölünebilen en küçük sayıdır.

1 ile 20 arasındaki tüm sayılarla eşit olarak bölünebilen en küçük pozitif sayı nedir ?
"""
