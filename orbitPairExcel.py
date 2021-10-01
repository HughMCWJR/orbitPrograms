import orbitSetGenSlow2 as orbitSetGen
import orbitsByPeriodRotNum as orbitGetter
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

for orbit in orbits:

    s.write(cellY, cellX, orbit)
    cellY += 2

    orbitPairs = orbitSetGen.genOrbitSet(orbit, sigma, 2)

    for pair in orbitPairs:

        if pair[0] == orbit:

            s.write(cellY, cellX, pair[1])
            cellY += 1

        else:

            s.write(cellY, cellX, pair[0])
            cellY += 1            
    
    cellX += 1
    cellY = 0

wb.save('sigma' + str(sigma) + 'RotNum' + str(numer) + '.' + str(denom) + '.xls')
    
