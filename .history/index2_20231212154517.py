import numpy as np
import matplotlib.pyplot as plt

def calculateCircuitPower(voltage, i, internalResistance):
    circuitPower = voltage*voltage / (i+ internalResistance)
    return circuitPower

def main():
    voltage = 12
    internalResistance = 5
    powerList = [internalResistance*2]
    
    for i in range(internalResistance*2):
        circiutPower = calculateCircuitPower(voltage, i, internalResistance)
        powerList.append(circiutPower)
    
    print(powerList)

if __name__ == "__main__":
    main()