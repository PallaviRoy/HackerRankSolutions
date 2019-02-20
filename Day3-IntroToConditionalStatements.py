#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    # is odd, print Weird
    if N%2 !=0:
        print("Weird")
    # is even and in the inclusive range of 2 to 5, print Not Weird
    # is even and in the inclusive range of 6 to 20, print Weird
    # is even and greater than 20, print Not Weird
    else:
        if N in range(2,6):
            print("Not Weird")
        elif N in range(6,21):
            print("Weird")
        elif N > 20:
            print("Not Weird")

