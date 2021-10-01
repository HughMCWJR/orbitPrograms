import orbitsByPeriodRotNum as orbitGetter
import rotCheck
import orbitGenFromPoint as orbitGen
from fractions import Fraction

inputNum = input("Orbit: ")
sigma = int(input("Sigma: "))

rotNumer = rotCheck.checkRot(inputNum, sigma, True)[1]

orbits = orbitGetter.getOrbits(sigma, rotNumer, len(inputNum))
"""
orbit = [Fraction(int(inputNum, sigma), sigma**len(inputNum) - 1)]

orbit.append((orbit[-1] * sigma) % 1)

while orbit[0] != orbit[-1]:

    orbit.append((orbit[-1] * sigma) % 1)

orbit.pop()
"""

orbit = orbitGen.genOrbit(Fraction(int(inputNum, sigma), sigma**len(inputNum) - 1), sigma)

ordered = sorted(orbit)

for i in orbits:

    partOfSet = True

    orbitTest = [Fraction(int(i, sigma), sigma**len(i) - 1)]

    orbitTest.append((orbitTest[-1] * sigma) % 1)

    while orbitTest[0] != orbitTest[-1]:

        orbitTest.append((orbitTest[-1] * sigma) % 1)

    orbitTest.pop()

    orderedTest = sorted(orbitTest)

    if orderedTest[0] > ordered[0]:

        for j in range(len(ordered) - 1):

            if orderedTest[j] > ordered[j + 1] or orderedTest[j + 1] < ordered[j + 1]:

                partOfSet = False

                break

    elif orderedTest[0] < ordered[0]:

        for j in range(len(ordered) - 1):

            if ordered[j] > orderedTest[j + 1] or ordered[j + 1] < orderedTest[j + 1]:

                partOfSet = False

                break

    else:

        partOfSet = False

    if partOfSet:

        print(i)

    
