dogalkare = 0
toplam = 0
toplamkare = 0
for i in range(1, 101):
    dogalkare += pow(i, 2)
    toplam += i
    toplamkare = pow(toplam, 2)
print(toplamkare, dogalkare, toplamkare-dogalkare)
"""
İlk on doğal sayının karelerinin toplamı,

1 2 + 2 2 + ... + 10 2 = 385
İlk on doğal sayının toplamının karesi,

(1 + 2 + ... + 10) 2 = 55 2 = 3025
Dolayısıyla, ilk on doğal sayının karelerinin toplamı ile toplamın karesi arasındaki fark 3025 - 385 = 2640'tır.

İlk yüz doğal sayının karelerinin toplamı ile toplamın karesi arasındaki farkı bulun.
"""