from math import floor

def calculateFuelReq(mass):
    """Caluclate and returns fuel (int) reqiured for mass (int)"""
    
    return floor(mass/3) - 2


def calculateFuelReqWithFuelCorrectedFor(mass):
    """Caluclate and returns fuel (int) reqiured for mass (int) 
    with the added fuel included in the calculation
    """
    
    fuel = calculateFuelReq(mass)
    totFuel = 0
    while fuel > 0:
        totFuel = totFuel + fuel
        fuel = calculateFuelReq(fuel)

    return totFuel 
    
    

def main():
    """Day 1 of Advent of Code 2019"""
    
    moduleMassFile= open("spacecraft_module_mass.txt", "r")
    moduleMass = [int(x) for x in moduleMassFile.read().split("\n")]
    moduleMassFile.close()

    fuelReqSum = 0
    fuelCorrectedReqSum = 0
    for mass in moduleMass:
        fuelReqSum = fuelReqSum + calculateFuelReq(mass)
        fuelCorrectedReqSum = fuelCorrectedReqSum + calculateFuelReqWithFuelCorrectedFor(mass) 
        
    print(f"Fuel:           {fuelReqSum}")
    print(f"Fuel Corrected: {fuelCorrectedReqSum}")


if __name__ == "__main__":
    main()