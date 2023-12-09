import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistances, internalResistance):
    totalResistance = np.sum(resistances) 
    totalResistance += internalResistance
    return totalResistance

def calculateCircuitPower(voltage, resistances, internalResistance):
    totalResistance = calculateTotalResistance(resistances, internalResistance)
    circuitPower = voltage * voltage / totalResistance
    return circuitPower
    
def createGraphicPlot(resistances, voltage, resistancePiece, internalResistance):
    resistance_range = np.arange(0, calculateTotalResistance(resistances), 1)
    powerList = []

    for resistance in resistance_range:
       totalResistance = calculateTotalResistance(resistances, internalResistance)
       circuitPower = calculateCircuitPower(voltage, resistances + [resistance])
       powerList.append(circuitPower)
    
    

    plt.plot(resistance_range, powerList, label='Devre Gücü')
    max_power_index = np.argmax(powerList)
    resistance_values = [np.sum(resistances[:i+1]) for i in range(resistancePiece)]
    plt.scatter(resistance_values[max_power_index], powerList[max_power_index], color='red', label='Max Güç Noktası', s=100) # belirlenen güç noktasını işaretlemek için

    plt.xlabel('Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()    

def main():
    voltage = int(input("Devrenin gücünü giriniz: "))
    internalResistance = int(input("Devrenin iç direncini giriniz: "))
    resistancePiece = int(input("Kaç adet direnç eklemek istiyorsunuz? "))
    resistances = []
    for i in range(resistancePiece):
        resistance_value = float(input(f"{i+1}. direnç değerini girin: "))
        resistances.append(resistance_value)

    totalResistance = calculateTotalResistance(resistances, internalResistance)
    circuitPower = calculateCircuitPower(voltage, resistances, internalResistance)
    print(f"Toplam Devre Direnci: {totalResistance} Ohm")
    print(f"Devre Gücü: {circuitPower} Watt")
    
    createGraphicPlot(resistances, voltage, resistancePiece)
    
if __name__ == "__main__":
    main()
