import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistances):
    totalResistance = np.sum(resistances)  # seri bağlı direnç için hesaplama
    return totalResistance

def calculateCircuitPower(voltage, resistances):
    totalResistance = calculateTotalResistance(resistances)
    circuitPower = voltage * voltage / totalResistance
    return circuitPower

def createGraphicBar(resistances, voltage, resistancePiece):
    powerList = []

    for i in range(resistancePiece):
        circuitPower = calculateCircuitPower(voltage, resistances[:i+1])
        powerList.append(circuitPower)

    resistance_values = [np.sum(resistances[:i+1]) for i in range(resistancePiece)]

    plt.bar(resistance_values, powerList, width=0.1, label='Devre Gücü')
    a, b, c = np.polyfit(resistance_values, powerList, 2)
    parabola_x = np.linspace(min(resistance_values), max(resistance_values), 100)
    parabola_y = a * parabola_x**2 + b * parabola_x + c
    plt.plot(parabola_x, parabola_y, color='red', label='Parabolik Eğri')

    plt.xlabel('Toplam Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Toplam Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()
    
def createGraphicPlot(resistances, voltage, resistancePiece):
    powerList = []
    resistance_range = np.arange(0, calculateTotalResistance(resistances), 10)
    for i in range(resistancePiece):
        circuitPower = calculateCircuitPower(voltage, resistances[:i+1])
        powerList.append(circuitPower)

    plt.plot(resistance_range, powerList, label='Devre Gücü')
    plt.xlabel('Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()
    
def main():
    voltage = int(input("Devrenin gücü kaç volt olsun? "))
    resistancePiece = int(input("Kaç adet direnç eklemek istiyorsunuz? "))
    resistances = []
    for i in range(resistancePiece):
        resistance_value = float(input(f"{i+1}. direnç değerini girin: "))
        resistances.append(resistance_value)

    totalResistance = calculateTotalResistance(resistances)
    circuitPower = calculateCircuitPower(voltage, resistances)
    print(f"Toplam Devre Direnci: {totalResistance} Ohm")
    print(f"Devre Gücü: {circuitPower} Watt")

    createGraphic(resistances, voltage, resistancePiece)

if __name__ == "__main__":
    main()
