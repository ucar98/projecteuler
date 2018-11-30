sayi = []
for x in range(1000):
    for y in range(999, 1, -1):
        t = x*y
        if str(t) == str(t)[::-1]:
            sayi.append(t)

sayi.sort()
print(sayi[-1])
"""
S4: Palindromik bir sayı her iki yolu da aynı şekilde okur.
İki 2 haneli sayıdan üretilen en büyük palindrom 9009 = 91 × 99'dur.

İki 3 haneli sayının ürününden yapılan en büyük palindromu bulun.
Çözüm: İç içe iki döngü içerisindeki sayıları çarpıyoruz. palindromik olanları
bir listeye aktarıyoruz. Bu listeyi sıralayıp en sondaki (en büyük) olanı
ekrana yazdırıyoruz."""



