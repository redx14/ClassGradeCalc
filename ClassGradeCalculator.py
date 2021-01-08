#Andrey Ilkiv Assignment 5 Problem 2 Section 01 10/19/2020

#variable for average total
avgtotal = 0

#asks user for number of students in the class
students = int(input("How many students are in your class? "))

#checks to make sure user entered a valid input
while students < 0 :
    print("Invalid # of students, try again." , '\n')
    students = int(input("How many students are in your class? "))

#asks user for number of tests in the class
tests = int(input("How many tests in this class? "))

#checks to make sure user entered a valid input
while tests < 0 :
    print("Invalid # of tests, try again.")
    tests = int(input("How many tests in this class? "))

#buffer
print('\n' , "Here we go!" , '\n')

#for each student the program asks 
for i in range (1, students+1):
    #total score is set to 0 for each student, this is sum of all tests
    totalscore = 0
    #prints header for each student i 
    print("**** Student #" + str(i) + "****")
    for j in range (1 , tests+1):
        score = int(input("Enter score for test #" + str(j) + ": "))
        #checks to make sure valid test score is entered, keeps asksing
        while score < 0 :
            print("Invalid score, try again")
            score = int(input("Enter score for test #" + str(j) + ": "))
            #adds up the scores
        totalscore += score
    #average for each student i
    avg = totalscore/tests
    #sum of all student averages for their test scores
    avgtotal = avgtotal + avg
    #prints average score for each student i and prints their average test grade
    print("Average score for student #" + str(i) + " is " + format(avg, '.2f') , "" , sep='\n')
#get the average of all the students
totalavg = avgtotal / students
#prints class average test grade
print("Average score for all students is: " + format(totalavg, '.2f'))
