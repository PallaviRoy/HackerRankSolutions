class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0
	# Add your code here
    def computeDifference(self):
        min = self.__elements[0]
        max = self.__elements[0]
        maxDiff = 0
        
        for elem in self.__elements:
            if elem < min:
                min = elem
            if elem > max:
                max = elem
        
        maxDiff = min-max
        if (maxDiff<0):
            maxDiff = -maxDiff
        self.maximumDifference = maxDiff


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)