
#İki giriş değerini ve bir kapıyı işleme sokar.
def mantik1(kapi,sayi1,sayi2=0):

    kapi=kapi.upper()

    if(kapi=="AND"):
        sonuc=sayi1 and sayi2
    
    elif(kapi=="OR"):
        sonuc=sayi1 or sayi2

    elif(kapi=="XOR"):
        if(sayi1==sayi2):
            sonuc=0
        else:
            sonuc=1
    elif(kapi=="NOT"):
        if(sayi1==0):
            sonuc=1
        elif(sayi1==1):
            sonuc=0
    else:
        return "Gecersiz kapi adi"

    return(sonuc)

#Mantik1 fonksiyonunu da kullanarak 3 sayi ve iki kapıyı işleme sokar.
def mantik2(kapi1,kapi2,sayi1,sayi2,sayi3):
    kapi1=kapi1.upper()
    kapi2=kapi2.upper()

    parantez_ici_sonuc=mantik1(kapi2,sayi2,sayi3) #İşlem önceliği sebebiyle önce parantez içini hesaplar.
    genel_sonuc=mantik1(kapi1,parantez_ici_sonuc,sayi1) #Parantez içinde çıkan sonuçla birlikte parantez dışındaki sayıyı işleme sokar.

    return genel_sonuc

#Döngülerle birlikte  her ihtimali sırasıyla deneyip mantik2 fonksiyonunu da kullanıp bütün sonucları ekrana yazdırır.
def dogruluk_tablosu(k1,k2):
    for a in[0,1]:
        for b in[0,1]:
            for c in[0,1]:

                sonuc=mantik2(k1,k2,a,b,c)
                print(sonuc)


print("Sanal Mantik Devresi Simülatörüne Hoşgeldiniz")
print("----------------------------------------------")
print("1-Tek Kapili Hesaplama")
print("2-Dogruluk Tablosu Hesaplama\n")

#Kullanıcıya seçenek sunup iki işlemden birisini seçmesini sağlar.
secim=int(input("Uygulamak istediginiz islemin numarasini girin: "))

#Kullanıcıdan bir kapı ve iki giriş değeri ister ve bu değerleri işleme sokar.
if (secim==1):
    print("\n--Tek Kapili Hesaplama--")
    kapi=input("Bir kapi seciniz(AND,OR,XOR,NOT): ")
 
    kapi=kapi.upper()
    sayi2=0
    if(kapi=="NOT"):#Not kapısında sadece bir değer kullanıldığı için kullanıcı not kapısını seçerse sadece bir kapı girmesini sağlayan koşul.
        sayi1=int(input("Bir sayi giriniz(0,1): "))
    else:
        sayi1=int(input("1. sayiyi giriniz(0,1): "))
        sayi2=int(input("2. sayiyi giriniz(0,1): "))

    sonuc=mantik1(kapi,sayi1,sayi2)
    print("Sonuc: ",sonuc)

#Kullanıcıdan iki kapı girmesini ister ve bütün değerleri sırasıyla bu iki kapıyla işleme sokup bütün ihtimalleri ekrana yazdırır.
elif(secim==2):
    print("\n--Dogruluk Tablosu Hesaplama--")
    kapi1=input("1. kapiyi seciniz(AND,OR,XOR): ")
    kapi2=input("2. kapiyi seciniz(AND,OR,XOR): ")

    dogruluk_tablosu(kapi1,kapi2)

#Kullanıcı olmayan bir işlem seçerse uyarı verir.
else:
    print("Gecersiz bir numara girdiniz lutfen 1 veya 2 seciniz")

  