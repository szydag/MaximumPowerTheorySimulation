import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistance, internalResistance):
    totalResistance = resistance + internalResistance
    return totalResistance

def calculateCircuitPower(voltage, resistance):
    circuitPower = voltage* voltage / resistance
    return circuitPower

def createGraphicPlot(powers):
    resistance_range = np.arange(0, calculateTotalResistance(resistances, internalResistance), 1)
    powerList = []

    for resistance in resistance_range:
       totalResistance = calculateTotalResistance(resistances, internalResistance)
       circuitPower = calculateCircuitPower(voltage, resistances + [resistance], internalResistance)
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
    voltage = 12
    internalResistance = 5
    resistance = 15
    powers = []
    for i in range(resistance):
        i = calculateTotalResistance(i, internalResistance)
        circuitPower = calculateCircuitPower(voltage, i)
        powers.append(circuitPower)
    
    createGraphicPlot(powers)
    
if __name__ == "__main__":
    main()
