import numpy as np
import matplotlib.pyplot as plt

def calculateTotalResistance(resistances):
    totalResistance = np.sum(resistances)
    return totalResistance

def calculateCircuitPower(voltage, resistances):
    totalResistance = calculateTotalResistance(resistances)
    circuitPower = voltage * voltage / totalResistance
    return circuitPower

def createGraphicBar(resistances, voltage, resistancePiece):
    powerList = []

    for i in range(resistancePiece):
        totalResistance = calculateTotalResistance(resistances[:i+1])
        circuitPower = calculateCircuitPower(voltage, resistances[:i+1])
        powerList.append(circuitPower)

    resistance_values = [np.sum(resistances[:i+1]) for i in range(resistancePiece)]

    max_power_index = np.argmax(powerList)
    plt.bar(resistance_values, powerList, width=0.1, label='Devre Gücü')
    plt.scatter(resistance_values[max_power_index], powerList[max_power_index], color='red', label='Max Güç Noktası', s=100)
    plt.xlabel('Toplam Direnç Değeri')
    plt.ylabel('Devre Gücü (Watt)')
    plt.title('Toplam Direnç Değerine Göre Devre Gücü Değişimi')
    plt.legend()
    plt.show()
    
def createGraphicPlot(resistances, voltage, resistancePiece):
    resistance_range = np.arange(0, calculateTotalResistance(resistances), 1)
    powerList = []

    #for resistance in resistance_range:
    #    totalResistance = calculateTotalResistance(resistances)
    #    circuitPower = calculateCircuitPower(voltage, resistances + [resistance])
    #   powerList.append(circuitPower)
    
    

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
    
    graphicType = int(input("Bar grafik olarak görmek için 0 plot grafik olarak görmek için 1 seçiniz."))
    if(graphicType == 0):
        createGraphicBar(resistances, voltage, resistancePiece)
    elif(graphicType == 1):    
        createGraphicPlot(resistances, voltage, resistancePiece)
    else:
        print("Ne yazık ki elimizde başka grafik yok:( )")    
    
if __name__ == "__main__":
    main()
