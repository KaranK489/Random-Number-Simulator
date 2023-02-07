import numpy as np
import matplotlib.pyplot as plt

def main():

    # 2 dice sum

    low = 1
    high = 7

    d1 = np.random.randint(low, high, 1000)
    d2 = np.random.randint(low, high, 1000)

    s1 = d1+d2


    print("Sums of dice rolls:")
    print(s1)

    countRolls = np.bincount(s1)
    countRolls = np.delete(countRolls, 0)
    countRolls = np.delete(countRolls, 0)

    print( )
    print("Amount of sums per number, from 2-12:")
    print(countRolls)

    plt.hist(s1, bins = range(2,14), align="left", color = "aqua")
    plt.title("Sum of Dice Rolls")
    plt.xlabel("Sums")
    plt.ylabel("Frequency")

    plt.show()

    # 2 dice averages

    print()
    print("Averages of numbers:")

    s2 = s1/2
    print(s2)

    plt.hist(s2, bins = range(1,8), align ="left", color = "aqua")
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

    while (i<1000):
        if s1[i] > mean - stand and s1[i] < stand + mean:
            counter+=1
        i+=1


    print(str(counter/10) + "% of the values are within 1 standard deviation of the mean")








main()