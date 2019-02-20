import math
import os
import random
import re
import sys


print("please enter array ")

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sum = []

lenofhrglass = 3
n = len(arr) - lenofhrglass +1

for i in range (0, n):
    for j in range (0, lenofhrglass + 1):
        total = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+    arr[i+2][j+2]  
        sum.append(total)

sum.sort()

print(sum[-1])