import fractions

def genOrbit(orbitPoint, sigma):

    orbit = [orbitPoint]

    orbit.append((orbit[-1] * sigma) % 1)

    while orbit[0] != orbit[-1]:

        orbit.append((orbit[-1] * sigma) % 1)

    orbit.pop()

    return orbit
