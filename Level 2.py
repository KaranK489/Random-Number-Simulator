import numpy as np
import matplotlib.pyplot as plt
from random import randint

def main():

    prizes = [0,0,0,0,0,0]

    allPrizes = False
    counter = 0
    happymeals = []


    while allPrizes == False:
        random = randint(0,5)
        counter+=1

        if (prizes[random] == 0):
            prizes[random] = 1

        if prizes == [1,1,1,1,1,1]:
            if len(happymeals) == 1000:
                allPrizes = True
            else:

                happymeals.append(counter)
                prizes = [0,0,0,0,0,0]
                counter = 0


    plt.hist(happymeals, bins = range(6,60), align="left", color = "aqua")
    plt.title("Number of Happy Meals required to get all prizes")
    plt.xlabel("Amount of times needed to buy happy meals")
    plt.ylabel("Frequency")

    print(happymeals)

    plt.show()



main()