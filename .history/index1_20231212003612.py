import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistances, internalResistance):
    totalResistance = np.sum(resistances) + internalResistance
    return totalResistance

def calculateCircuitPower(voltage, resistance):
    circuitPower = voltage * voltage / resistance
    return circuitPower

def calculateResistanceRange(resistances, internalResistance):
    resistance_range = np.arange(0, calculateTotalResistance(resistances, internalResistance) + 1, 1)
    return resistance_range

def calculateGraphicValues(resistances, internalResistance, voltage, resistance_range):
    powerList = []

    for resistance in resistance_range:
        totalResistance = calculateTotalResistance(resistances + [resistance], internalResistance)
        circuitPower = calculateCircuitPower(voltage, totalResistance)
        powerList.append(circuitPower)
        return powerList

def createGraphicPlot(resistance_range, powerList):
    
    plt.plot(resistance_range, powerList, label='Devre Gücü')
    max_power_index = np.argmax(powerList)
    plt.scatter(resistance_range[max_power_index], powerList[max_power_index], color='red', label='Max Güç Noktası', s=100)

    plt.xlabel('Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()

def main():
    voltage = 12
    internalResistance = 5
    resistances = [15] 
    resistance_range = calculateResistanceRange(resistances, internalResistance)
    powerList = calculateGraphicValues(resistances, internalResistance, voltage, resistance_range)
    createGraphicPlot(resistance_range, powerList)

if __name__ == "__main__":
    main()
