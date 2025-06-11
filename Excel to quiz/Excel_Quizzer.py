import pandas as pd#reading the spreadsheet
import random#random selection of questions and answers


sheetnum = 0
questions = []#questions go here
answers = []#answers to questions go here
answer = []#the true answer goes here
currentanswer = ""#answer to the current question
explanation = []#explaining the answer
questionnum = 0#what we show the viewers
totalquestions = 0#total questions... self explanatory
realqnum = 0#the index
infinite = False#infinite questions mode
correct = 0#amount of questions correct
choices = []#choices of current answers given
user_selection = ''
while True:
    while True:
        print("downloading excel spreadsheet")
        
        try:
            sheetnum = int(input("which sheet do you want to use?: "))
            temp = pd.ExcelFile("Quizzes.xlsx")
            quizzes = pd.read_excel("Quizzes.xlsx", sheet_name = sheetnum)
        except:
            print("please type a valid number")
            continue
        if input("is this sheet correct (y/n): " + temp.sheet_names[sheetnum] + " ").lower() != 'n':
            break

    #we now have the correct sheet, time to set up the quiz
    while True:
        try:
            if input("go until stopped? (y/n): ") == 'y':
                infinite = True
                #with so many questions, there's no need to ask how many there are!
                break

            else:
                infinite = False
            totalquestions = int(input("Total questions asked: "))
            while totalquestions > len(quizzes):
                #too many questions requested
                print(f"there are only {len(quizzes)} questions for this sheet. Try again")
                totalquestions = int(input("Total questions asked: "))
                
        except:
            print("that was invalid, try again")
            continue
        #if it got here, everything was valid
        break

    if infinite:
        #infinite question mode
        #fill up the variables
        questionnum = 1
        for i in range (0, len(quizzes)):
            questions.append(quizzes.iloc[i, 0])
            answers.append([quizzes.iloc[i, 1], quizzes.iloc[i, 2], quizzes.iloc[i, 3], quizzes.iloc[i, 4]])
            answer.append(quizzes.iloc[i, 5])
            if quizzes.iloc[i, 6] != "":
                explanation.append(quizzes.iloc[i, 6])
            else:
                explanation.append("...")
            pass
        
        #start asking questions
        while user_selection != "quit":
            print("\ntype \"quit\" to exit out of infinite mode\n")
            realqnum = random.randint(0, len(questions)-1)
            choices = []
            user_selection = ''
            #keep previous questions so they do come back up
            print(f"Question {questionnum}: ")
            questionnum+=1
            print(questions[realqnum])
            currentanswer = answer[realqnum]
            if currentanswer.lower() == "a":
                currentanswer = answers[realqnum][0]
            elif currentanswer.lower() == "b":
                currentanswer = answers[realqnum][1]
            elif currentanswer.lower() == "c":
                currentanswer = answers[realqnum][2]
            else:
                currentanswer = answers[realqnum][3]

            #A-D questions
            print()
            choices = answers[realqnum]
            random.shuffle(choices)
            print(f"A: {str(choices[0])}\n")
           
            print(f"B: {str(choices[1])}\n")
            
            print(f"C: {str(choices[2])}\n")
            
            print(f"D: {str(choices[3])}\n")
            

            #get user response
            while user_selection not in ['a', 'b', 'c', 'd']:
                user_selection = input("Choose the correct letter (A-D): ").lower()
                if user_selection.lower() == "quit":
                    break
            if user_selection == "quit":
                break
            #match the response with the actual answer
            if user_selection.lower() == "a":
                user_selection = choices[0]
            elif user_selection.lower() == "b":
                user_selection = choices[1]
            elif user_selection.lower() == "c":
                user_selection = choices[2]
            else:
                user_selection = choices[3]
            
            if(str(user_selection) == currentanswer):
                print("That is correct!")
            else:
                print(f"That was incorrect. The answer is as follows:\n\n {currentanswer}")
            
            if explanation[realqnum] != '...':
                print(f"explanation: \n{explanation[realqnum]}")
            
            print("\n\n")
        
        #Give grade
        print(f"you have completed {questionnum - 1} amount of questions!")
        pass
    else:
        #go for a select number of questions

        #fill up the variables
        questionnum = 1
        for i in range (0, len(quizzes)):
            questions.append(quizzes.iloc[i, 0])
            answers.append([quizzes.iloc[i, 1], quizzes.iloc[i, 2], quizzes.iloc[i, 3], quizzes.iloc[i, 4]])
            answer.append(quizzes.iloc[i, 5])
            if quizzes.iloc[i, 6] != "":
                explanation.append(quizzes.iloc[i, 6])
            else:
                explanation.append("...")
            pass
        
        #start asking questions
        for i in range(0, totalquestions):
            realqnum = random.randint(0, len(questions)-1)
            choices = []
            user_selection = ''
            #delete previously asked questions so they do not come back up
            print(f"Question {i+1}: ")
            print(questions.pop(realqnum))
            currentanswer = answer.pop(realqnum)
            if currentanswer.lower() == "a":
                currentanswer = answers[realqnum][0]
            elif currentanswer.lower() == "b":
                currentanswer = answers[realqnum][1]
            elif currentanswer.lower() == "c":
                currentanswer = answers[realqnum][2]
            else:
                currentanswer = answers[realqnum][3]

            #A-D questions
            print()
            while len(answers[realqnum]) != 0:
                choices.append({answers[realqnum].pop(random.randint(0, len(answers[realqnum])-1))})
            print(f"A: {str(choices[0])}\n")
           
            print(f"B: {str(choices[1])}\n")
            
            print(f"C: {str(choices[2])}\n")
            
            print(f"D: {str(choices[3])}\n")
            answers.pop(realqnum)

            #get user response
            while user_selection not in ['a', 'b', 'c', 'd']:
                user_selection = input("Choose the correct letter (A-D): ").lower()
            print()
            #match the response with the actual answer
            if user_selection.lower() == "a":
                user_selection = choices[0]
            elif user_selection.lower() == "b":
                user_selection = choices[1]
            elif user_selection.lower() == "c":
                user_selection = choices[2]
            else:
                user_selection = choices[3]
            
            if(str(user_selection)[2:-2] == currentanswer):
                print("That is correct!")
                correct+=1
            else:
                print(f" That was incorrect. The answer is as follows:\n\n {currentanswer}\n\n")
            
            if explanation[realqnum] != '...':
                print(f"explanation: \n{explanation[realqnum]}")
            explanation.pop(realqnum)
            print("\n\n")
        
        #Give grade
        print(f"The quiz is done! you got {correct} out of {totalquestions} correct, that's a {(correct/totalquestions) * 100}%!")

            




    #finished quizzing
    if input("run again? (y/n)") == "n":
        break