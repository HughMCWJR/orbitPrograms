import orbitsByPeriodRotNum as orbitGetter
import orbitGenFromPoint as orbitGen
import convertOrbitFractionString as convert
import rotCheck
from fractions import Fraction

def testOrbitSet(orbit1, orbit2):

    partOfSet = True

    if orbit2[0] > orbit1[0]:

        for j in range(len(orbit1) - 1):

            if orbit2[j] > orbit1[j + 1] or orbit2[j + 1] < orbit1[j + 1]:

                partOfSet = False

                break

    elif orbit2[0] < orbit1[0]:

        for j in range(len(orbit1) - 1):

            if orbit1[j] > orbit2[j + 1] or orbit1[j + 1] < orbit2[j + 1]:

                partOfSet = False

                break

    else:

        partOfSet = False

    return partOfSet

if __name__ == "__main__":

    orbit1 = input("Orbit: ")
    orbit2 = input("Orbit: ")

    sigma = 0

    for i in range(len(orbit1)):

        if sigma < int(orbit1[i]):

            sigma = int(orbit1[i])

    for i in range(len(orbit2)):
                
        if sigma < int(orbit2[i]):

            sigma = int(orbit2[i])
            
    sigma += 1

    #print(convert.convertToFraction(orbit1, sigma))
    #print(sorted(orbitGen.genOrbit(convert.convertToFraction(orbit1, sigma), sigma)))

    #print(convert.convertToFraction(orbit2, sigma))
    #print(sorted(orbitGen.genOrbit(convert.convertToFraction(orbit2, sigma), sigma)))
    
    print(testOrbitSet(sorted(orbitGen.genOrbit(convert.convertToFraction(orbit1, sigma), sigma)), sorted(orbitGen.genOrbit(convert.convertToFraction(orbit2, sigma), sigma))));
