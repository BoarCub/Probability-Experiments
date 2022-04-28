#-------------------------------------------------------------------------------
# Name:        Pset4Problem2
# Author:      Deepayan Sanyal
# Created:     28/04/2022
# Licence:     MIT License
#-------------------------------------------------------------------------------

import random

"""
Project Description: This program experimentally simulates the number of dog-cat
pairs if there are n dogs, 3n cats, and 2n pairs are created randomly
"""

# Change this to the number of trials you want to simulate
numTrials = 100

# Change this to your desired n-value
n = 30

total = 0

for x in range(numTrials):
    animalList = []
    for y in range(n):
        animalList.append(0)
    for y in range(3*n):
        animalList.append(1)

    randomList = random.sample(animalList, 4*n)

    for i in range(2*n):
        anim1 = randomList[i]
        anim2 = randomList[i+1]
        if ((anim1 == 0 and anim2 == 1) or (anim1 == 1 and anim2 == 0)) :
            total += 1

total = total/numTrials

print(total)
