import math
import rotCheck

def getOrbits(sigma, rotNumer, period):
   
    orbits = [""]

    digits = "0" * (period - rotNumer) + "1" * rotNumer

    cursor = 0

    if period % rotNumer == 0 and rotNumer != 1:

        print("RotNumer % Period == 0")

    for i in range(period):

        orbits[0] += digits[cursor]

        cursor += rotNumer

        if cursor >= len(digits):

            cursor -= len(digits)

    for i in range(len(orbits[0])):

        if orbits[0][i] == "1":

            newOrbit = orbits[0][:i] + str(int(orbits[0][i]) + 1)

            if i != len(orbits[0]) - 1:

                    newOrbit += orbits[0][i + 1:]

            if rotCheck.checkRot(newOrbit):

                jump = i

                break

    while str(sigma - 1) not in orbits[-1]:

        newOrbits = []

        for orbit in orbits:

            cursor = jump

            lastOrbit = orbit

            for i in range(period):

                newOrbit = lastOrbit[:cursor] + str(int(lastOrbit[cursor]) + 1)

                if cursor != len(lastOrbit) - 1:

                    newOrbit += lastOrbit[cursor + 1:]

                if newOrbit not in newOrbits and newOrbit not in orbits:

                    newOrbits.append(newOrbit)

                cursor += jump

                if cursor >= len(lastOrbit):

                    cursor -= len(lastOrbit)

                lastOrbit = newOrbit

        orbits += newOrbits

    return orbits
                
if __name__ == "__main__":

    d = int(input("Sigma: "))
    q = int(input("Rotational Number Denominator: "))

    orbits = getOrbits(d,int(input("Rotational Number Numerator: ")),q)
            
    working = True

    for orbit in orbits:

        print(orbit)

        if not rotCheck.checkRot(orbit):

            working = False

            print("Non-Rot")

    #if working and len(orbits) == math.comb(q + d - 2, q):

    #   print("Working")

    #else:
    
    #    print("Failed")

    #    print(len(orbits))
