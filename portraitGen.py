import math
import orbitGenFromPoint as orbitGen
from fractions import Fraction

def genPortrait(inputNum, sigma = 0):

    if sigma == 0:

        for i in range(len(inputNum)):

            if sigma < int(inputNum[i]):

                sigma = int(inputNum[i])

        sigma += 1

    
    orbit = orbitGen.genOrbit(Fraction(int(inputNum, sigma), sigma**len(inputNum) - 1), sigma)

    ordered = sorted(orbit)

    portrait = ""

    for i in range(len(orbit)):

        if i + 1 == len(orbit):

            numChords = math.floor(((ordered[0] + 1) - ordered[i]) / (1 / sigma))

            if numChords != 0:
                
                portrait += str(numChords)

        else:

            numChords = math.floor((ordered[i + 1] - ordered[i]) / (1 / sigma))

            if numChords != 0:
                
                portrait += str(numChords)

    # Put portrait in standard form (smallest value)
    smallest = portrait
    curPortrait = portrait

    for i in range(len(portrait) - 1):

        curPortrait = curPortrait[1:] + curPortrait[0]

        if int(curPortrait) < int(smallest):

            smallest = curPortrait

    return smallest

if __name__ == "__main__":

    print(genPortrait(input("Orbit: "), int(input("Sigma: "))))
