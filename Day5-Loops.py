#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for multiplier in range(1,11):
        stringPrint = str(n) + " x "+ str(multiplier)+ " = "+ str(n*multiplier)
        print(stringPrint)

