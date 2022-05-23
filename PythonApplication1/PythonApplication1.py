
ucret = 0 
liste = [] 
sozluk={} 
t=5 
insan=0 
tsozluk={} 
tiyatro=0 
sinema=0 
import sqlite3 
veritabanı=sqlite3.connect('Kayitlar.db') 
imlec=veritabanı.cursor() 
Tablo=""" 
CREATE TABLE IF NOT EXISTS Musteriler (ad,soyad,kat,ucret) 
""" 

imlec.execute(Tablo)

veritabanı.commit()
class ad:
    ad=""
    soyad=""

while t==5: 
    print("sinema 25tl, tiyatro 20tl, mısıt 12tl, kola 6tl, su 3tl, soda 5tl, meyve suyu 4tl") 
    nesne=ad()
    nesne.ad=input("ad giriniz: ") 
    nesne.soyad =input("soyad giriniz: ") 
    no=input("koltuk numarası yazınız: ") 
    sc=1 
    while (sc==1): 
        try:

            secim=int(input("sinema icin(1), tiyatro icin (2) tuslayiniz : "))
            sc==2
        except ValueError as hata:
            print("Hata. Tekrar deneyiniz")
        tt=secim 
        if secim==1: 
            ucret=ucret + 25 
            sinema=sinema+1 
            sc=2 
            kat="sinema" 
        elif secim==2: 
            ucret=ucret + 20 
            tiyatro=tiyatro+1 
            sc=2 
            kat="tiyatro" 
        else: 
            print("/") 
    while (secim=="1"):     
         
        if (secim=="1"): 
 
            liste=liste+["sinema"] 
             
            secim2=input("icecek istermisiniz(e/h) : ") 
            if secim2=="e" or secim2=="E": 
                soru=input("kola icin (1),su icin (2),soda icin (3), meyve suyu icin (4) veya bu adimlari gecmek icin (5) basiniz : ") 
                if soru=="1": 
                    liste=liste+["kola"] 
                    ucret=ucret + 6 
                elif soru=="2": 
                    liste=liste+["su"] 
                    ucret=ucret + 3 
                elif soru=="3": 
                    liste=liste+["soda"] 
                    ucret=ucret + 5 
                elif soru=="4": 
                    liste=liste+["meyve suyu"] 
                    ucret=ucret + 4 
                elif soru=="5": 
                    secim=6 
                else: 
                    print("lütfen 1-4 arasında tuslama yapiniz!!") 
            elif secim2=="h" or secim2=="H": 
                secim=6 
        else: 
            print("/") 
        ucretString=str(ucret) 
        ts="Sinema" + ucretString 
        t=6 
    while (secim=="2"): 
 
         
        if secim=="2": 
            liste=liste+["Tiyatro"] 
            secim2 = input("icecek istermisiniz(e/h) : ") 
            if secim2=="e" or secim2=="E":
                kb=1
                while (kb==1):
                    try:
                        soru=input("kola icin (1),su icin (2),soda icin (3), meyve suyu icin (4) veya bu adimlari gecmek icin (5) basiniz : ") 
                        kb=2
                    except ValueError as hata:
                        print("hata")
                if soru=="1": 
                        liste=liste+["kola"] 
                        ucret=ucret+6 
                elif soru=="2": 
                        liste=liste+["su"] 
                        ucret=ucret+3 
                elif soru=="3": 
                        liste=liste+["soda"] 
                        ucret=ucret+5 
                elif soru=="4": 
                        liste=liste+["meyve suyu"] 
                        ucret=ucret+4 
                elif soru=="5": 
                        secim=6 
                else: 
                        print("lütfen 1-4 arasında tuslama yapiniz!!") 
            elif secim2=="h" or secim2=="H": 
                 secim=6 
            else: 
                 print("/") 
            ucretString=str(ucret) 
 
            ts="Tiyatro" + " " + ucretString + "TL" 
            t=6 
    insan=insan+1 
    tsozluk={"Katılım": 
             { "Tiyatro":tiyatro, 
              "Sinema":sinema, 
              "Toplam Katılım":insan 
                 } 
                } 
   
adsoyad=nesne.ad + " " + nesne.soyad 
sozluk.setdefault(adsoyad,ts) 
print(tsozluk) 
print(sozluk)
print(ucret)
