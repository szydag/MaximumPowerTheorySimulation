import numpy as np
import matplotlib.pyplot as plt

def calculateCircuitPower(voltage, resistances):
    totalResistance = np.sum(resistances) #seri baglı direnç için hesaplama
    circuitPower = voltage*voltage / totalResistance
    return totalResistance, circuitPower

def createGraphic(resistances, voltage):
    resistance_range = np.arange(1, 101, 1)
    powerList = []

    for resistance in resistance_range:
        totalResistance, circuitPower = calculateCircuitPower(voltage, resistances + [resistance])
        powerList.append(circuitPower)

    plt.plot(resistance_range, powerList, label='Devre Gücü')
    plt.xlabel('Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()

def main():
    voltage = int(input("Devrenin gücü kaç volt olsun? "))

    # Kullanıcıdan direnç değerlerini al
    resistancePiece = int(input("Kaç adet direnç eklemek istiyorsunuz? "))
    resistances = []
    for i in range(resistancePiece):
        resistance_value = float(input(f"{i+1}. direnç değerini girin: "))
        resistances.append(resistance_value)

    totalResistance, circuitPower = calculateCircuitPower(voltage, resistances)
    print(f"Toplam Devre Direnci: {totalResistance} Ohm")
    print(f"Devre Gücü: {circuitPower} Watt")

    createGraphic(resistances, voltage)

if __name__ == "__main__":
    main()
