class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    firstName = None
    lastName = None
    idNumber = None
    scores = []
    def __init__(self, fName, lName, Id, studentscores):
        Person.__init__(self, fName, lName, Id)
        self.scores = studentscores
    
    def calculate(self):
        totalscores = 0
        for i in range (0,len(self.scores)):
            totalscores += + self.scores[i]
        average = totalscores/len(self.scores)

        if (average<=100 and average>=90):
            return "O"
        elif (average<90 and average>=80):
            return "E"
        elif (average<80 and average>=70):
            return "A"
        elif (average<70 and average>=55):
            return "P"
        elif (average<55 and average>=40):
            return "D"
        elif (average<40):
            return "T"

print("please enter inputs")
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())