s = 1
for x in range(1, 21):
    if s % x > 0:
        for y in range(1, 21):
            if (s*y) % x == 0:
                s *= y
                break
print(s)

"""
2520, kalan sayı olmadan 1'den 10'a kadar olan sayıların her birine bölünebilen en küçük sayıdır.

1 ile 20 arasındaki tüm sayılarla eşit olarak bölünebilen en küçük pozitif sayı nedir ?
"""
