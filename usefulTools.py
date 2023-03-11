# this is set of some useful functions that we use to import to other python files

import random


def miles_to_feet(miles):
    feet = 5280 * miles
    return feet


beatles = ["John Lennon", "PauGeorge Harrison", "Ringo Star"]


def getfileext(filename):
    return filename[filename.index(".") + 1:]


def rollDice(num):
    return random.randint(1, num)
