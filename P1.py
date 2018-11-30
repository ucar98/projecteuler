sayi = 1000
toplam = 0
for i in range(1, sayi):
    if i % 3 == 0 or i % 5 == 0:
        toplam += i
print(toplam)

"""
İlk iki satırda tanımlama yaptık.
Hedefe kadar birer birer artın bir döngü içerisinde
Artan sayı 3 veya 5'e bölünürse onu toplam değişkeniyle
her seferinde topladık ve döngü bittiğinde sayi 
değişkeninden küçük 3 ve 5'in katları olan sayıları 
topladık. 
"""