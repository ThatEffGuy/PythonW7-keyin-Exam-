"""
You will be prompted to your name and exam mark.
The exam has two parts
    examMark     - max  of 100 marks
    praticalMark - max of 50 marks
"""

def getData():
    #enter name
    name = input("Please Enter Your Name : ")
    while name =="":
        print("You must enter a name!")
        name = input("Please Enter Your Name : ")
    #end while
    #enter exam mark
    examMark = int(input("Enter Exam Mark (0 - 100) :"))
    while examMark < 0 or examMark>100:
        print("Invalid mark. Must between 1 and 100")
        examMark = int(input("Enter Exam Mark (0 - 100) :"))
    #end while
    #enter practical Mark
    practicalMark = int(input("Enter Practical Mark (0 - 50) :"))
    while practicalMark < 0 or practicalMark>50:
        print("Invalid mark. Must between 0 and 50")
        practicalMark = int(input("Enter Practical Mark (0 - 50) :"))
    #end while
    return name, examMark, practicalMark
#end getData()


def getMarkAndPercentage():
    totalMark = examMark + practicalMark
    percepercentage = round(totalMark/150*100,0)
    return totalMark, percentage
    #End getMarkAndPercentage


def getGrade():
    if percentage < 40:
        grade = "E"
    elif percentage < 49:
        grade = "D"
    elif percentage < 60:
        grade = "C"
    elif percentage < 70:
        grade = "B"
    elif percentage < 90:
        grade = "A"
    else:
        grade = "A*"
    #end if


#get grade
def getGrade():
    if percentage < 40:
      grade = "E"
    elif percentage < 49:
        grade = "D"
    elif percentage < 60:
        grade = "C"
    elif percentage < 70:
        grade = "B"
    elif percentage < 90:
        grade = "A"
    else:
        grade = "A*"
#end if
    return grade

#display Results
def displayResults(name, percentage):
    print(name, "Scored", percentage,"%. That's Grade",grade)
#end displayResults

#variables
name          = ""
examMark      = 0   
practicalMark = 0
totalMark     = 0
percentage    = 0
grade         = ""


#Main prog
name, examMark, practicalMark=getData()
mark, percentage = getMarkAndPercentage()
grade = getGrade()
displayResults(name, percentage)
