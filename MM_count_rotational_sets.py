import math

def findNumOrbitSets(q, d, k):

    total = 0

    if d - k - 1 <= (q - 1) * (k - 1):

        L = d - k - 1

    else:

        L = (q - 1) * (k - 1)

    for i in range(L + 1):

        j = 0

        while j <= (k - 1) - ((k-1+i) / q):

            total += ((-1) ** j) * math.comb(d + q - 2, d - k - 1 - i) * math.comb(k - 1, j) * math.comb(q * (k - 1 - j), k - 1 + i)

            j += 1

    return total

if __name__ == "__main__":

    while True:
        q = int(input("q: "))
        d = int(input("d: "))

        for k in range(1, d):
            print(findNumOrbitSets(q,d,k))