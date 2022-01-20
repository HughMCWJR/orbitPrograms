import math

def findNumOrbitSets (q, d, k):

    total = 0

    if d - k - 1 <= (q - 1) * (k - 1):

        L = d - 2

    else:

        L = q * (k - 1)

    for i in range(L + 1):

        j = 0

        while j <= (k - 1):

            total += ((-1) ** j) * math.comb(d + q - 2, d - 2 - i) * math.comb(k - 1, j) * math.comb(q * (k - 1 - j), i)

            j += 1

    return total

if __name__ == "__main__":

    while True:
        q = int(input("q: "))
        d = int(input("d: "))

        for k in range(1, d):
            print(findNumOrbitSets(q,d,k))
