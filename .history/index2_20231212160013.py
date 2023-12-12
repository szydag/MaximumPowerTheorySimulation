import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistance , internalResistance):
    totalResistance = resistance + internalResistance
    return totalResistance

def calculateCurrentValue(voltage, totalResistance):
    currentValue = voltage / totalResistance
    return currentValue

def calculateCircuitPower(voltage, totalResistance):
    circuitPower = voltage*voltage / totalResistance
    return circuitPower

def main():
    voltage = 12
    internalResistance = 5
    powerList = [internalResistance*2]
    
    for i in range(internalResistance*2):
        totalResistance = calculateTotalResistance(i, internalResistance)
        circiutPower = calculateCircuitPower(voltage, totalResistance)
        powerList.append(circiutPower)
    
    print(powerList)

if __name__ == "__main__":
    main()