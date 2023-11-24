import numpy as np
import matplotlib.pyplot as plt

def calculateCircuitPower(voltage, resistances):
    totalResistance = np.sum(resistances) #seri baglı direnç için hesaplama
    circuitPower = voltage^2 / totalResistance
    return totalResistance, circuitPower

def createGraphic(resistances, voltage):
    resistance_range = np.arange(1, 101, 1)
    guc_listesi = []

    for resistance in resistance_range:
        totalResistance, circuitPower = calculateCircuitPower(voltage, resistances + [resistance])
        guc_listesi.append(circuitPower)

    plt.plot(resistance_range, guc_listesi, label='Devre Gücü')
    plt.xlabel('resistance Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('resistance Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()

def main():
    voltage = 12

    # Kullanıcıdan resistance değerlerini al
    resistance_sayısı = int(input("Kaç adet resistance eklemek istiyorsunuz? "))
    resistances = []
    for i in range(resistance_sayısı):
        resistance_değeri = float(input(f"{i+1}. resistance değerini girin: "))
        resistances.append(resistance_değeri)

    totalResistance, circuitPower = calculateCircuitPower(voltage, resistances)
    print(f"Toplam Devre Direnci: {totalResistance} Ohm")
    print(f"Devre Gücü: {circuitPower} Watt")

    createGraphic(resistances, voltage)

if __name__ == "__main__":
    main()
