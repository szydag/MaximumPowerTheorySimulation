import numpy as np
import matplotlib.pyplot as plt

def calculateCircuitPower(voltaj, direncler):
    toplam_direnç = np.sum(direncler) #seri baglı dirençler için hesaplama
    devre_guc = voltaj^2 / toplam_direnç
    return toplam_direnç, devre_guc

def grafik_olustur(direncler, voltaj):
    direnç_aralığı = np.arange(1, 101, 1)
    guc_listesi = []

    for direnç in direnç_aralığı:
        toplam_direnç, devre_guc = calculateCircuitPower(voltaj, direncler + [direnç])
        guc_listesi.append(devre_guc)

    plt.plot(direnç_aralığı, guc_listesi, label='Devre Gücü')
    plt.xlabel('Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()

def main():
    voltaj = 12

    # Kullanıcıdan direnç değerlerini al
    direnç_sayısı = int(input("Kaç adet direnç eklemek istiyorsunuz? "))
    direncler = []
    for i in range(direnç_sayısı):
        direnç_değeri = float(input(f"{i+1}. direnç değerini girin: "))
        direncler.append(direnç_değeri)

    toplam_direnç, devre_guc = calculateCircuitPower(voltaj, direncler)
    print(f"Toplam Devre Direnci: {toplam_direnç} Ohm")
    print(f"Devre Gücü: {devre_guc} Watt")

    grafik_olustur(direncler, voltaj)

if __name__ == "__main__":
    main()
