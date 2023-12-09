import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistances):
    totalResistance = np.sum(resistances)
    return totalResistance

def calculateCircuitPower(voltage, resistances):
    totalResistance = calculateTotalResistance(resistances)
    circuitPower = voltage * voltage / (totalResistance + internalResistance)
    return circuitPower
    
def createGraphicPlot(resistances, voltage, resistancePiece):
    resistance_range = np.arange(0, calculateTotalResistance(resistances) + internalResistance, 1)
    powerList = []

    for resistance in resistance_range:
        circuitPower = calculateCircuitPower(voltage, [internalResistance] + resistances + [resistance])
        powerList.append(circuitPower)

    plt.plot(resistance_range, powerList, label='Devre Gücü')
    max_power_index = np.argmax(powerList)
    resistance_values = [internalResistance + np.sum(resistances[:i+1]) for i in range(resistancePiece)]
    plt.scatter(resistance_values[max_power_index], powerList[max_power_index], color='red', label='Max Güç Noktası', s=100)

    plt.xlabel('Toplam Direnç Değeri (Ohm)')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Toplam Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()

def main():
    global internalResistance
    voltage = int(input("Devrenin gücünü giriniz: "))
    internalResistance = int(input("Devrenin iç direncini giriniz: "))
    resistancePiece = int(input("Kaç adet direnç eklemek istiyorsunuz? "))
    resistances = []
    for i in range(resistancePiece):
        resistance_value = float(input(f"{i+1}. direnç değerini girin: "))
        resistances.append(resistance_value)

    totalResistance = calculateTotalResistance(resistances)
    circuitPower = calculateCircuitPower(voltage, resistances)
    print(f"Toplam Devre Direnci: {totalResistance} Ohm")
    print(f"Devre Gücü: {circuitPower} Watt")
    
    createGraphicPlot(resistances, voltage, resistancePiece)

if __name__ == "__main__":
    main()
