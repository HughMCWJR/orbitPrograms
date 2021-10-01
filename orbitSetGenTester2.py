import orbitsByPeriodRotNum as orbitGetter
import orbitSetGenSlow2 as orbitSetGen
import portraitGen

sigma = int(input("Sigma: "))
rotNumer = int(input("Numer: "))

#rotDenom = sigma - 1
rotDenom = 3

while True:

    print()
    print(sigma)
    print()

    orbits = orbitGetter.getOrbits(sigma, rotNumer, rotDenom)

    layerNums = []
    layerCount = []

    for orbit in orbits:

        print(orbit + " : " + str(len(orbitSetGen.genOrbitSet(orbit, sigma, 2))) + " : " + portraitGen.genPortrait(orbit, sigma))

        if len(orbitSetGen.genOrbitSet(orbit, sigma, 2)) in layerNums:

            layerCount[layerNums.index(len(orbitSetGen.genOrbitSet(orbit, sigma, 2)))] += 1

        else:

            if layerNums == []:

                layerNums.append(len(orbitSetGen.genOrbitSet(orbit, sigma, 2)))
                layerCount.append(1)

            else:

                i = 0

                while len(orbitSetGen.genOrbitSet(orbit, sigma, 2)) > layerNums[i]:

                    i += 1

                    if i == len(layerNums):

                        break

                layerNums.insert(i, len(orbitSetGen.genOrbitSet(orbit, sigma, 2)))
                layerCount.insert(i, 1)

    print(layerNums)
    print(layerCount)

    #sigma += 1
    rotDenom += 1
