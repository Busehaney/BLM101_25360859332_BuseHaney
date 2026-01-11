# Sanal Mantık Devresi Simülatörü

## Öğrenci Bilgileri
* *Ad Soyad:* Buse Haney
* *Numara:* 25360859332
* *Ders:* Bilgisayar Mühendisliğine Giriş (BLM101)

## Proje Konusu
Python ile Sanal Mantık Devresi Simülatörü Tasarımı. Kullanıcının temel mantık kapılarını kullanarak hesaplama yapmasını ve 3 değişkenli karmaşık mantık devrelerinin doğruluk tablolarını oluşturmasını sağlayan program.

---

## Proje Açıklaması (Dokümantasyon)

### 1. Proje Hakkında
Bu proje, Bilgisayar Mühendisliği'ne Giriş dersi kapsamında geliştirilmiş bir simülasyon aracıdır. Program, kullanıcıların temel mantık kapılarını (AND, OR, XOR, NOT) kullanarak mantıksal hesaplamalar yapmasına ve 3 değişkenli karmaşık mantık devrelerinin (Örn: A AND (B OR C)) doğruluk tablolarını oluşturmasına olanak tanır.

### 2. Kullanılan Teknolojiler
Proje tamamen *Python* programlama dili kullanılarak geliştirilmiştir. Harici bir kütüphane kullanılmamış, dilin standart fonksiyonlarından yararlanılmıştır.
* *Standart Fonksiyonlar:* input(), print(), int(), .upper().
* *Kontrol Yapıları:* if-elif-else blokları.
* *Döngüler:* İç içe for döngüleri (doğruluk tablosu için).

### 3. Algoritma Mantığı
Program iki ana modda çalışır:
* *Tek Kapılı Hesaplama:* Kullanıcının seçtiği kapıya (AND, OR, XOR, NOT) göre işlem yapar. NOT kapısı seçildiğinde algoritma otomatik olarak tek giriş moduna geçer.
* *Doğruluk Tablosu:* 3 farklı girişin (A, B, C) alabileceği tüm ihtimalleri ($2^3=8$ durum) taramak için iç içe geçmiş 3 for döngüsü kullanılır. İşlem önceliğini sağlamak için parantez içi önce hesaplanır, çıkan sonuç diğer değişkenle işleme sokulur.

### 4. Kurulum ve Çalıştırma
1. kodlar klasöründeki mantikdevresi.py dosyasını indirin.
2. Terminal veya komut satırında dosyanın olduğu dizine gelin.
3. Şu komutu yazın: python mantikdevresi.py
