# Kullanıcıdan bir sayı alarak çift mi tek mi olduğunu kontrol eden Python programı

# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı giriniz: "))

# Negatif sayı kontrolü
if sayi < 0:
    print("Negatif sayı girdiniz!")
# Çift/Tek kontrolü
elif sayi % 2 == 0:
    print("Girdiğiniz sayı çift sayıdır.")
else:
    print("Girdiğiniz sayı tek sayıdır.")
