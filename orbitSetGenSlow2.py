import orbitsByPeriodRotNum as orbitGetter
import rotCheck
import orbitGenFromPoint as orbitGen
from fractions import Fraction

def genOrbitSet(inputNum, sigma = 0, desiredLength = 0):

    #print(inputNum)

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

    for i in range(len(orbitSetApplicants) - 1):

        tempOrbitSet = [inputNum, orbitSetApplicants[i + 1]]

        if desiredLength == 0 or desiredLength > 2:

            for j in range(len(orbitSetApplicants) - 2):

                partOfSet = True

                for k in range(len(tempOrbitSet)):

                    if i > j:

                        if not inSet(orbitSetApplicants[j + 1], tempOrbitSet[k], sigma):

                            partOfSet = False

                    else:
                        
                        if not inSet(orbitSetApplicants[j + 2], tempOrbitSet[k], sigma):

                            partOfSet = False

                if partOfSet:

                    if i > j:

                        tempOrbitSet.append(orbitSetApplicants[j + 1])

                    else:

                        tempOrbitSet.append(orbitSetApplicants[j + 2])

        if len(tempOrbitSet) > len(orbitSets[0]) and desiredLength == 0:

            orbitSets = [tempOrbitSet]
            
        elif desiredLength != len(orbitSets[0]) and desiredLength == len(tempOrbitSet):

            orbitSets = [tempOrbitSet]

        elif len(tempOrbitSet) == len(orbitSets[0]):

            orbitSets.append(tempOrbitSet)

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

if __name__ == "__main__":

    print(genOrbitSet(input("Orbit: "), int(input("Sigma: ")), int(input("Wanted length: "))))
