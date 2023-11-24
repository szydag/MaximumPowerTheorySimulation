import numpy as np
import matplotlib.pyplot as plt

def calculateCircuitPower(voltage, resistances):
    totalResistance = np.sum(resistances) #seri baglı dirençler için hesaplama
    circuitPower = voltage^2 / totalResistance
    return totalResistance, circuitPower

def grafik_olustur(resistances, voltage):
    direnç_aralığı = np.arange(1, 101, 1)
    guc_listesi = []

    for direnç in direnç_aralığı:
        totalResistance, circuitPower = calculateCircuitPower(voltage, resistances + [direnç])
        guc_listesi.append(circuitPower)

    plt.plot(direnç_aralığı, guc_listesi, label='Devre Gücü')
    plt.xlabel('Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()

def main():
    voltage = 12

    # Kullanıcıdan direnç değerlerini al
    direnç_sayısı = int(input("Kaç adet direnç eklemek istiyorsunuz? "))
    resistances = []
    for i in range(direnç_sayısı):
        direnç_değeri = float(input(f"{i+1}. direnç değerini girin: "))
        resistances.append(direnç_değeri)

    totalResistance, circuitPower = calculateCircuitPower(voltage, resistances)
    print(f"Toplam Devre Direnci: {totalResistance} Ohm")
    print(f"Devre Gücü: {circuitPower} Watt")

    grafik_olustur(resistances, voltage)

if __name__ == "__main__":
    main()
