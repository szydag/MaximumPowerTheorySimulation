import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistance , internalResistance):
    totalResistance = resistance + internalResistance
    return totalResistance

def calculateCurrentValue(voltage, totalResistance):
    currentValue = voltage / totalResistance
    return currentValue

def calculateVoltageValue(currentValue, resistance):
    voltageValue = currentValue * resistance
    return voltageValue

def calculateCircuitPower(currentValue, voltageValue):
    circuitPower = currentValue * voltageValue
    return circuitPower

def createGraphicPlot(resistanceList, powerList):
    plt.plot(resistanceList, powerList)
    plt.xlabel('Direnç (Resistance)')
    plt.ylabel('Güç (Power)')
    plt.title('Direnç ve Güç İlişkisi')
    plt.grid(True)
    plt.show()

def main():
    voltage = 12
    internalResistance = 5
    powerList = []
    resistanceList = []
    
    for resistance in range(internalResistance*2):
        totalResistance = calculateTotalResistance(resistance, internalResistance)
        currentValue = calculateCurrentValue(voltage, totalResistance)
        voltageValue = calculateVoltageValue(currentValue, resistance)
        circiutPower = calculateCircuitPower(currentValue, voltageValue)
        resistanceList.append(resistance)
        powerList.append(circiutPower)
    
    print(powerList)

if __name__ == "__main__":
    main()