import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistance, internalResistance):
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


def createGraphicPlot(resistanceList, powerList, maxPowerResistance, maxPower):
    plt.plot(resistanceList, powerList, label='Güç')
    plt.scatter(maxPowerResistance, maxPower, color='red', label=f'Max Güç\n({maxPowerResistance}, {maxPower})')
    
    plt.xlabel('Direnç (Resistance)')
    plt.ylabel('Güç (Power)')
    plt.title('Direnç ve Güç İlişkisi')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    voltage = int(input("Devrenin gücünü giriniz: "))
    internalResistance = int(input("Devrenin iç direncini giriniz: "))
    powerList = []
    resistanceList = []

    for resistance in range(internalResistance * 2):
        totalResistance = calculateTotalResistance(resistance, internalResistance)
        currentValue = calculateCurrentValue(voltage, totalResistance)
        voltageValue = calculateVoltageValue(currentValue, resistance)
        circuitPower = calculateCircuitPower(currentValue, voltageValue)
        resistanceList.append(resistance)
        powerList.append(circuitPower)

    maxPower = max(powerList)
    maxPowerIndex = powerList.index(maxPower)
    maxPowerResistance = resistanceList[maxPowerIndex]

    createGraphicPlot(resistanceList, powerList, maxPowerResistance, maxPower)

if __name__ == "__main__":
    main()
