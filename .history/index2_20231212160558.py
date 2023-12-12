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

def main():
    voltage = 12
    internalResistance = 5
    powerList = [internalResistance*2]
    
    for i in range(internalResistance*2):
        resistance = i
        totalResistance = calculateTotalResistance(resistance, internalResistance)
        currentValue = calculateCurrentValue(voltage, totalResistance)
        voltageValue = calculateVoltageValue(currentValue, resistance)
        circiutPower = calculateCircuitPower(currentValue, voltageValue)
        powerList.append(circiutPower)
    
    print(powerList)

if __name__ == "__main__":
    main()