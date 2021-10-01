import orbitsByPeriodRotNum as orbitGetter
import orbitSetGenSlow2 as orbitSetGen
import portraitGen

sigma = int(input("Sigma: "))
rotNumer = int(input("Numer: "))
rotDenom = int(input("Denom: "))

while True:

    print()
    print(sigma)
    print

    orbits = orbitGetter.getOrbits(sigma, rotNumer, rotDenom)

    layerNums = []
    layerCount = []

    for orbit in orbits:

        print(orbit + " : " + str(len(orbitSetGen.genOrbitSet(orbit, sigma, 2))))

        if len(orbitSetGen.genOrbitSet(orbit, sigma, 2)) in layerNums:

            layerCount[layerNums.index(len(orbitSetGen.genOrbitSet(orbit, sigma, 2)))] += 1

        else:

            layerNums.append(len(orbitSetGen.genOrbitSet(orbit, sigma, 2)))
            layerCount.append(1)

    print(layerNums)
    print(layerCount)

    sigma += 1
