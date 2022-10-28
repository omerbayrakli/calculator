import random
import time


def topla(liste):
    print("Sayilarin toplami: ")
    return sum(liste)


def sayilari_goster(liste):
    print("Generate edilen sayilar: ")
    return liste


def buyukten_kucuge(liste):
    print("Buyukten kucuge hali: ")
    return liste.sort(reverse=True)


def kucukten_buyuge(liste):
    print("SayÃ„Â±lar: ")
    print(liste)
    liste.sort()
    print("KÃƒÂ¼ÃƒÂ§ÃƒÂ¼kten bÃƒÂ¼yÃƒÂ¼Ã„ÂŸe hali: ")
    print(liste)


def ortalama(liste):
    toplam = sum(liste)
    uzunluk = len(liste)
    average = toplam / uzunluk
    print("SayÃ„Â±larÃ„Â±n ortalamasi: ")
    print(average)


while True:

    sayi = int(input("Kac sayi uretmek istiyorsun: "))
    son_Deger = int(input("son limit kac olsun: "))

    ## FOR LOOP ##
    number_list = []
    for _ in range(sayi):
        number_list.append(random.randint(0, son_Deger))
    ########

    ##! List Comprehension ##

    number_list = [random.randint(0, son_Deger) for _ in range(sayi)]

    #########################

    print(
        """HÃ„Â°ZMETLERÃ„Â°MÃ„Â°Z \n[1] SAYILARI GOSTER \n[2] SAYILARI TOPLA \n[3] KUCUKTEN BUYUGE SIRALA \n[4] BUYUKTEN KUCUGE SIRALA \n[5] SAYILARIN ORTALAMASINI BUL \n[0] UYGULAMADAN CIK"""
    )

    secilen_deger = int(input("Hangi iÃ…ÂŸlemi yapmak istiyorsun: "))


    if secilen_deger == 1:
        sonuc = sayilari_goster(number_list)

    elif secilen_deger == 2:
        sonuc = topla(number_list)

    elif secilen_deger == 3:
        sonuc = kucukten_buyuge(number_list)

    elif secilen_deger == 4:
        sonuc = buyukten_kucuge(number_list)

    elif secilen_deger == 5:
        sayilari_goster(number_list)
        sonuc = ortalama(number_list)

    elif secilen_deger == 0:
        print("Programdan ÃƒÂ§Ã„Â±kÃ„Â±lÃ„Â±yor..")
        time.sleep(2)
        print("Programdan ÃƒÂ§Ã„Â±kÃ„Â±ldÃ„Â±.")
        break

    print(sonuc)
