import portraitGen
import orbitsByPeriodRotNum as orbitGetter
import orbitSetGenSlow2 as orbitSetGen
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("blankForPython.xls")

wb = copy(rb)

s = wb.get_sheet(0)

cellY = 0
cellX = 0

sigma = int(input("Sigma: "))
numer = int(input("Rot Num Numerator: "))
denom = int(input("Rot Num Denominator: "))

orbits = orbitGetter.getOrbits(sigma, numer, denom)

data = {}

for orbit in orbits:

    portrait = portraitGen.genPortrait(orbit, sigma)

    if portrait == "1122":

        print(orbit)

    if portrait in data:

        data[portrait].append(len(orbitSetGen.genOrbitSet(orbit, sigma, 2)))
        
    else:

        data[portrait] = [len(orbitSetGen.genOrbitSet(orbit, sigma, 2))]

for portrait in data:

    s.write(cellY, cellX, portrait)
    cellY += 1

    for numPairs in data[portrait]:

        s.write(cellY, cellX, numPairs)
        cellY += 1
    
    cellX += 1
    cellY = 0

wb.save('portraitPairs.xls')
