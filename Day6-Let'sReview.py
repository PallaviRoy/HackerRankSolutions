# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
ListOfStrings = []

for loop in range(0,T):
    ListOfStrings.append(input())

for string in ListOfStrings:
    for even in range(0, len(string), 2):
        print(string[even], end='')
    
    print(" ", end='')

    for odd in range(1, len(string), 2):
        print(string[odd], end='')
    print()

