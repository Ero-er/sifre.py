import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_sayi = int(input("sifrenizin uzunluğunu giriniz:"))
sifre = ""
for i in range(sifre_sayisi):
    sifre = sifre + random.choice(karakterler)
print("olusturulansifre", sifre)

    
