deger1 = 1
deger2 = 2
deger3 = deger1 + deger2
toplam = 0
while deger1 < 4000000:
    print(deger1, end=" ")
    deger1 = deger2
    deger2 = deger3
    deger3 = deger1 + deger2
    if deger1 %2 == 0:
        toplam += deger1

print()
print(toplam)

"""
#P2: Fibonacci dizisindeki her yeni terim, önceki iki terimi ekleyerek oluşturulur.
1 ve 2 ile başlayarak, ilk 10 terim şöyle olacaktır:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Değerleri dört milyonu geçmeyen Fibonacci dizisindeki terimleri dikkate alarak,
ikiye tam bölünen terimlerin toplamını bulun.

Çözüm:
Üç farklı değer yazdık çünkü fibonacci dizisi eski iki öğenin toplanıp
yeni öğeye aktarılmasıyla gerçekleşiyordu. Bu yüzden bizde 3 farklı öğeye
ihtiyaç duyduk.
""" 
