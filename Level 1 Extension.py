import numpy as np
import matplotlib.pyplot as plt


def main():
    # 2 dice sum

    low = 1
    high = 7

    dice = int(input("How many die do you want to roll?"))
    trials = int(input("How many trials do you want for each dice?"))

    s1 = np.random.randint(0,1,trials)


    counter = 0

    while counter<dice:

        d1 = np.random.randint(low, high, trials)

        s1 = s1 + d1

        counter+=1

    print("Sums of dice rolls:")
    print(s1)

    countRolls = np.bincount(s1)
    a = 0

    while a<dice:
        countRolls = np.delete(countRolls, a)
        a+=1

    print()
    print("Amount of sums per number, from " + str(dice) + "-" + str(dice*6) + ":")
    print(countRolls)

    plt.hist(s1, bins=range(dice, dice*7), align="left", color="aqua")
    plt.title("Sum of Dice Rolls")
    plt.xlabel("Sums")
    plt.ylabel("Frequency")

    plt.show()

    # 2 dice averages

    print()
    print("Averages of numbers:")

    s2 = s1 / 2
    print(s2)

    plt.hist(s2, bins=range(int(dice/2), int(dice*4)), align="left", color="aqua")
    plt.title("Averages of Dice Rolls")
    plt.xlabel("Averages")
    plt.ylabel("Frequency")
    plt.show()

    # Standard Deviation

    stand = np.std(s1)
    mean = np.mean(s1)

    i = 0
    counter = 0

    print()
    print("The standard deviation is " + str(stand))
    print("The mean is " + str(mean))

    while (i < trials):
        if s1[i] > mean - stand and s1[i] < stand + mean:
            counter += 1
        i += 1

    print(str(counter / int(trials/100)) + "% of the values are within 1 standard deviation of the mean")


main()