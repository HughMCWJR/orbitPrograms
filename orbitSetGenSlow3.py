import orbitsByPeriodRotNum as orbitGetter
import rotCheck
import orbitGenFromPoint as orbitGen
from fractions import Fraction

def genOrbitSet(inputNum, sigma = 0, desiredLength = 0):

    if sigma == 0:

        for i in range(len(inputNum)):

            if sigma < int(inputNum[i]):

                sigma = int(inputNum[i])

        sigma += 1

    rotNumer = rotCheck.checkRot(inputNum, sigma, True)[1]

    orbits = orbitGetter.getOrbits(sigma, rotNumer, len(inputNum))

    orbit = orbitGen.genOrbit(Fraction(int(inputNum, sigma), sigma**len(inputNum) - 1), sigma)

    ordered = sorted(orbit)

    orbitSetApplicants = [inputNum]

    for i in orbits:

        orbitTest = [Fraction(int(i, sigma), sigma**len(i) - 1)]

        orbitTest.append((orbitTest[-1] * sigma) % 1)

        while orbitTest[0] != orbitTest[-1]:

            orbitTest.append((orbitTest[-1] * sigma) % 1)

        orbitTest.pop()

        orderedTest = sorted(orbitTest)

        if inSet(orderedTest, ordered):

            orbitSetApplicants.append(i)
    
    orbitSets = [[inputNum]]

    if desiredLength == 0:

        desiredLength = sigma - 1

    while len(orbitSets[0]) < desiredLength:

        orbitSets = findSets(orbitSets, orbitSetApplicants, sigma)

    return orbitSets

def inSet(orbit1, orbit2, sigmaConvert = 0):

    if sigmaConvert != 0:

        orbit1 = sorted(orbitGen.genOrbit(Fraction(int(orbit1, sigmaConvert), sigmaConvert**len(orbit1) - 1), sigmaConvert))
        orbit2 = sorted(orbitGen.genOrbit(Fraction(int(orbit2, sigmaConvert), sigmaConvert**len(orbit2) - 1), sigmaConvert))

    partOfSet = True

    if orbit1[0] > orbit2[0]:

        for j in range(len(orbit2) - 1):

            if orbit1[j] > orbit2[j + 1] or orbit1[j + 1] < orbit2[j + 1]:

                partOfSet = False

                break

    elif orbit1[0] < orbit2[0]:

        for j in range(len(orbit2) - 1):

            if orbit2[j] > orbit1[j + 1] or orbit2[j + 1] < orbit1[j + 1]:

                partOfSet = False

                break

    else:

        partOfSet = False

    return partOfSet

def findSets(orbitSets, orbitSetApplicants, sigma):

    tempOrbitSets = []

    for i in range(len(orbitSets)):

        for j in range(len(orbitSetApplicants)):

            tempOrbitSet = orbitSets[i] + [orbitSetApplicants[j]]

            partOfSet = True

            for k in range(len(tempOrbitSet) - 1):

                if not inSet(tempOrbitSet[-1], tempOrbitSet[k], sigma):

                    partOfSet = False

            if partOfSet:

                if not sorted(tempOrbitSet) in tempOrbitSets:

                    tempOrbitSets.append(sorted(tempOrbitSet))

    return tempOrbitSets

if __name__ == "__main__":

    print(genOrbitSet(input("Orbit: "), int(input("Sigma: ")), int(input("Wanted length: "))))
