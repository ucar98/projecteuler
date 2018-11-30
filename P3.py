sayi = 600851475143
bolen = 2
while sayi > 1:
    if sayi % bolen == 0:
        sayi = sayi / bolen
    else:
        bolen += 1
print(bolen)

""" 
P3: 13195'in başlıca asal bölenleri 5, 7, 13 ve 29'dur.

600851475143 sayısının en büyük asal böleni nedir?
Çözüm:
Hedef sayıyı katlarına bölerek en büyük asal sayıyı buluyoruz. .
"""