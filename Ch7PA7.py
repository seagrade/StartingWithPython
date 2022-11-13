#This is my solution to this assignment.
#Chapter 7. Exercise 7, "Driver's License Exam"
#Programming Assignment 9
#Fall, November 2022.
#This Program will read the student's exam answers from a text file and store them on a list.
#The program will then use the correct answers from a seperate list to display whether:
#The student passed, number of correct and incorrect questions, and the exact incorrect questions.
#Correct Exam Answers: A, C, A, A, D, B, C, A, C, B, A, D, C, A, D, C, B, B, D, A
#Student must get at least 15 questions correct to pass.

totalQuestions = 20
studentAnswers = []
incorrectAnswers = []
examSolutions = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C',
                 'B', 'B', 'D', 'A']
 

#Define Main Function
def main():
    #Create function to open and strip students answers.
    studentAnswers = process_student_ans()
    
    #Create function to compare student answers to exam.
    grade(examSolutions, studentAnswers)

#Define process_student_ans() function.
def process_student_ans():
    #Open the Student Answers file
    infile = open('student_solution.txt', 'r')
    #Remove '\n' using strip method
    for index in infile:
        index = index.strip('\n')
        #Append stripped index into a list.
        studentAnswers.append(index)
    #Close the File
    infile.close()
    #Return the processed list to be used in grade() function.
    return studentAnswers
    
#Define the grade function:
def grade(examSolutions, studentAnswers):
    pass_requirement = 15
    counter = 0
    #For the index in the 20 quesitons.
    for index in range(totalQuestions):
        #If the exam answer matches the student answer.
        if examSolutions[index] == studentAnswers[index]:
            #Add 1 counter to represent total amount of correct answers
            counter += 1
        else:
            #Otherwise, the question is wrong and is added to the incorrect answers list to be displayed.
            counter += 0
            index += 1
            incorrectAnswers.append(index)
            
        #Write if else to determine whether the student passed or not based on correct answer count.
    if counter < pass_requirement:
        #If less than 15 answers are correct, display message for exam fail.
        print('Unfortunately you have failed the exam.')
        
    #else: (if 15 or more answers are correct, display exam is passed.
    else:
        print('Congratulations!! You passed the exam.')

        #Print functions; displays pass, correct and incorrect count, and which incorrect questions.
        #Number of correct questions = counter as it only counts correct questions.
        print('Number of questions you answered correctly: ', counter)
        #Number of incorrect questions = the total amount of questions less the amount of correct questions.
        print('Number of questions you answered incorrectly: ', totalQuestions - counter)
        #Print the list with the incorrect answers that was appended in the else: under grade() function.
        print('Questions you answered incorrectly: ', incorrectAnswers)
#Call main
main()

#Errors:
#Error 1 in line 59 & 64. if/else statement was under line 52 else statement
#Error 1 solution: Reformatted line 59 & 64 if/else statement to be under line 47 for loop.

#Error 2 in line 52 and output. Programming outputted incorrect values for wrong answers.
#Error 2 Solution: Added 'index += 1' before the append on line 55 to fix issue as index begins with 0.
