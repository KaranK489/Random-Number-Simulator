import numpy as np
import matplotlib.pyplot as plt
from random import randint

def main():

    keepRunning = True
    counter = 0
    samebirthdays = 0


    while keepRunning == True:
        counter+=1
        i = 0
        match = False
        birthday = np.random.randint(1, 366, 30)

        birthdayarray = np.bincount(birthday)


        while i<30 and match == False:
            if birthdayarray[i]>1:
                samebirthdays+=1
                match = True
            i+=1

            for x in birthdayarray:
                if x>1:
                    match = True

            if match == True:
                samebirthdays+=1

            if counter == 1000:
                keepRunning = False




    print("There are " + str(samebirthdays) + " classes where 2 or more students have the same exact birthday.")

    print("There are " + str(1000-samebirthdays) + " classes where no one has the same birthday.")


main()