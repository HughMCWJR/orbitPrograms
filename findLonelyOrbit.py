from fractions import Fraction
import math
from xlrd import open_workbook
from xlutils.copy import copy
import orbitsByPeriodRotNum as orbitGetter
import orbitSetGenSlow2
import gcd

if input("Type Y to start with blank Doc, anything else to start with old Doc: ") == "Y":

    rb = open_workbook("blankForPython.xls")

else:

    rb = open_workbook('findLonelyOrbit.xls')
    
wb = copy(rb)

s = wb.get_sheet(0)

def convertToBinary(fraction):

    if (math.log(fraction.denominator + 1, sigma) % 1 >= 0.9999999 or math.log(fraction.denominator+ 1, sigma) % 1 <= 0.0000001):

        numer = fraction.numerator
        denom = fraction.denominator

    else:

        i = 2
        
        while not (math.log((fraction.denominator * i) + 1, sigma) % 1 >= 0.9999999 or math.log((fraction.denominator * i) + 1, sigma) % 1 <= 0.0000001):

            i += 1

        numer = fraction.numerator * i
        denom = fraction.denominator * i

    binaryStr = ""
    tempNumer = numer

    while tempNumer >= sigma:

        binaryStr = str(tempNumer % sigma) + binaryStr

        tempNumer = math.floor(tempNumer / sigma)

    binaryStr = str(tempNumer % sigma) + binaryStr

    while len(binaryStr) != round(math.log(denom + 1, sigma)):

        binaryStr = "0" + binaryStr

    return binaryStr

#Number to multiply by fraction angle
sigma = int(input("Type # for sigma subscript: "))
#count for current period
period = int(input("Period to start search: "))
#next excel cell to write on
cellY = 0
cellX = period - 1

denom = (sigma**period) - 1

while True:

    numer = 1
    
    while numer < (period / 2):

        if gcd.gcd(numer, period) == 1 or numer == 1:

            orbits = orbitGetter.getOrbits(sigma, numer, period)

            for i in range(len(orbits)):

                orbitSet = orbitSetGenSlow2.genOrbitSet(orbits[i], sigma)

                print(len(orbitSet), orbitSet);

                if len(orbitSet) == 1:

                    s.write(cellY, cellX, orbitSet[0])
                    print(orbitSet[0])
                    
                    cellY += 1

        numer += 1
    
    print("Period", period, "done")

    denom = ((denom + 1) * sigma) - 1
    period += 1
    
    cellY = 0
    cellX += 1

    wb.save('findLonelyOrbit.xls')
