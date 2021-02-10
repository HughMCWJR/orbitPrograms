from fractions import Fraction
import math

"""
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

        binaryStr = binaryStr + str(tempNumer % sigma)

        tempNumer = math.floor(tempNumer / sigma)

    binaryStr = binaryStr + str(tempNumer % sigma)

    while len(binaryStr) != round(math.log(denom + 1, sigma)):

        binaryStr = "0" + binaryStr

    return binaryStr
"""

def checkRot(inputNum, sigma = 0, returnRotNumer = False):

    if sigma == 0:

        for i in range(len(inputNum)):

            if sigma < int(inputNum[i]):

                sigma = int(inputNum[i])

        sigma += 1

    num = Fraction(int(inputNum, sigma), sigma**len(inputNum) - 1)

    orbit = [num]

    orbit.append((orbit[-1] * sigma) % 1)

    while orbit[0] != orbit[-1]:

         orbit.append((orbit[-1] * sigma) % 1)

    orbit.pop()

    if returnRotNumer:

        ordered = sorted(orbit)

        while orbit[0] != ordered[0]:

            for i in range(len(orbit) - 1):

                orbit[i] = orbit[i + 1]

            orbit[-1] = ordered[0]

        rotNumer = 1

        while orbit[1] != ordered[rotNumer]:

            rotNumer += 1

            if rotNumer == len(orbit):

                break

    if len(orbit) == 1 or len(orbit) == 2 or len(orbit) == 3:

        rot = True

    else:

        ordered = sorted(orbit)

        rot = False

        if ordered[0] + (1 / sigma) > ordered[-1]:

            rot = True

        else:

            totalExterior = 0

            for i in range(len(ordered)):

                if (ordered[i] - ordered[i - 1]) % 1 > 1 / sigma:

                    totalExterior += math.floor(((ordered[i] - ordered[i - 1]) % 1) * sigma)

                    if totalExterior >= sigma - 1:

                        rot = True

                        break

    if returnRotNumer:

        if rot:

            return [rot, rotNumer]

        else:
          
            return [rot]

    else:

        return rot

if __name__ == "__main__":

    print(checkRot(input("Input Num: ")));
