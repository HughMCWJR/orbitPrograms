from fractions import Fraction
import math

def convertToStr(fraction, sigma):

    numDigits = 1

    numer = fraction.numerator
    denom = fraction.denominator

    while denom < sigma ** numDigits - 1:

        numer += fraction.numerator
        denom += fraction.denominator

    while denom + 1 != sigma ** numDigits:

        numDigits += 1

        while denom < sigma ** numDigits - 1:

            numer += fraction.numerator
            denom += fraction.denominator

    string = ""

    for i in range(numDigits):

        digit = 0

        while numer >= sigma ** (numDigits - i - 1):

            digit += 1
            numer -= sigma ** (numDigits - i - 1)

        string += str(digit)

    return string

def convertToFraction(inputNum, sigma = 0):

    if sigma == 0:

        for i in range(len(inputNum)):

            if sigma < int(inputNum[i]):

                sigma = int(inputNum[i])

        sigma += 1

    return Fraction(int(inputNum, sigma), sigma**len(inputNum) - 1)

if __name__ == "__main__":

    print(convertToFraction(input(), int(input())))
