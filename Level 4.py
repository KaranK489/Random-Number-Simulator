import numpy as np
import matplotlib.pyplot as plt
from random import randint

def main():

    # first is hermit who heard first, second is hermit who told first, rest are others
    hermits = [1, 1, 0, 0, 0, 0]
    counter = 2

    i = 0
    total = []

    while i<1000:

        maxHermits = False

        while maxHermits == False:
            x = randint(1,5)

            if hermits[x]==0:
                hermits[x]=1
                counter+=1

            else:
                maxHermits = True
                hermits = [1, 1, 0, 0, 0, 0]
                total.append(counter)
                counter = 2
        i+=1

    print(total)

    print("The average number of hermits that found out was " + str(np.mean(total)) + " hermits.")

    plt.hist(total, bins=range(2, 8), align="left", color="aqua")
    plt.title("Number of hermits that found out the secret")
    plt.xlabel("Number of hermits that found out")
    plt.ylabel("Frequency")
    plt.show()


main()