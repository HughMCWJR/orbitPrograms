import orbitWiggleMethod as orbitSetGetter
import orbitsByPeriodRotNum as orbits
import orbitGenFromPoint as orbitGen
import convertOrbitFractionString as convert
import orbitSetTest
from xlrd import open_workbook
from xlutils.copy import copy

if input("Type Y to start with blank Doc, anything else to start with old Doc: ") == "Y":

    rb = open_workbook("blankForPython.xls")

else:

    rb = open_workbook('orbitSets.xls')

wb = copy(rb)

s = wb.get_sheet(0)

cellY = 0
cellX = 0

sigma = 2

while True:

    curOrbits = orbits.getOrbits(sigma, 4, 7)

    for orbit in curOrbits:

        orbitSet = orbitSetGetter.getOrbitSet(orbit, sigma)

        complete = True

        for orbitInSet in orbitSet:

            beforeCopy = True

            for i in range(len(orbitSet) - 1):

                if orbitSet[i] == orbitInSet:

                    beforeCopy = False

                if beforeCopy:

                    if not orbitSetTest.testOrbitSet(sorted(orbitGen.genOrbit(orbitInSet, sigma)), sorted(orbitGen.genOrbit(orbitSet[i], sigma))):

                        complete = False
                        break

                else:

                    if not orbitSetTest.testOrbitSet(sorted(orbitGen.genOrbit(orbitInSet, sigma)), sorted(orbitGen.genOrbit(orbitSet[i + 1], sigma))):

                        complete = False
                        break

        s.write(cellY, cellX, sigma)
        cellX += 1

        s.write(cellY, cellX, complete)
        cellX += 1

        print(complete, " : ", convert.convertToStr(orbitSet[0], sigma) )

        for orbitInSet in orbitSet:

            s.write(cellY, cellX, convert.convertToStr(orbitInSet, sigma))
            cellX += 1

        cellY += 1
        cellX = 0
                    
    sigma += 1
    wb.save('orbitSets.xls')
