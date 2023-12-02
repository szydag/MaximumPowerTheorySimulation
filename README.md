# Maksimum Güç Teoremi Simülasyonu

## Giriş: 
Bu rapor, Temel Elektronik dersi kapsamında yapılan 1. vize ödevi olan "Maksimum Güç Teoremi Simülasyonu" hakkındadır. Ödevin amacı sabit voltaj ve farklı direnç değerleriyle oluşturulmuş elektrik devresindeki güç kaybını gözlemlemek ve sonuçları grafik olarak görselleştirmektir. Simülasyon işlemi Python dili kullanılarak gerçekleştirilmektedir.


## Elektrik Devresi Modeli:
Elektrik devresi modeli kullanıcının belirlediği sabit bir voltaj değeri, direnç sayısı ve direnç değerleri ile oluşturulmuştur. Dirençler adım adım ve seri bir biçimde devreye eklenir.


## Güç ve Toplam Direnç Hesaplamaları:
Elektrik devresi üzerindeki toplam güç kaybını hesaplamak için P = V^2 / R (P: güç, V: voltaj, R: direnç) formülü kullanılmıştır. Kullanıcının belirlediği direnç değerleri devreye tek tek ve her adımda toplam direnç değeri ve güç değeri hesaplanmaktadır. Kaydedilen toplam direnç değerleri ve güç değerleri birer listede tutulmaktadır. Bu listeler simülasyonun devamı olan grafik çizim işleminde kullanılacaktır.
Başlangıçta kullanıcıdan kaç adet direnç değeri girmek istediği öğrenilmektedir ve her girilen direnç değeri toplam dirence adım adım eklenmiştir. Örneğin kullanıcı 4 adet direnç girmiş ve bunlar sırası ile 5, 16, 23 ve 2 olsun. Sistemdeki güç kaybı sabit voltaj ile 4 farklı nokta için hesaplanacaktır. Bu adımlarda toplam direnç sırası ile 5, 21, 44 ve 46 olacaktır.


## Maksimum Güç Noktası:
Hesaplanan güç değerlerini kaydetmek için kullanılan güç listesindeki maksimim değer ve bu maksimum gücü elde ettiğimiz direnç değeri belirlenmektedir.


## Grafikler:
Hesaplama sonuçlarının görselleştirilmesinde kullanılacak grafik seçimi kullanıcıya bırakılmıştır. Grafikler oluşturulurken x-ekseninde direnç değerleri, y-ekseninde güç kaybı gösterilmektedir. Kırmızı işaret maximum güç noktasını temsil etmektedir. Grafiklerin çizimi için Python kütüphanelerinden matplotlib.pyplot kullanılmıştır. Elektrik devresi değerleri (Resim1.1)’ de gösterildiği şekilde kullanıcıdan alınmaktadır.


 
(Resim1.1)
![Ekran görüntüsü 2023-11-26 013922](https://github.com/szydag/MaximumPowerTheorySimulation/assets/96542141/9ed46b75-fcf9-4c9f-a31d-74c6c514f739)




Bar Grafiği Örneği: 
![Ekran görüntüsü 2023-11-26 013715](https://github.com/szydag/MaximumPowerTheorySimulation/assets/96542141/37b871ad-232e-4bb1-89ba-a6ab0a872a15)

 

Plot Grafiği Örneği:
![Ekran görüntüsü 2023-11-26 014259](https://github.com/szydag/MaximumPowerTheorySimulation/assets/96542141/5c643b3b-1b92-481b-a0de-8c00f734efa0)


