
print("WELCOME TO IYKE's QUIZ GAME!")
# Creating the objectives;

playing = input("Do you what to play?: ")
if playing != "yes":
    print("LOL!...You dey fear to loose?")
    quit()
if playing == "yes":
    print("Okay!...Let's play! :)")
    score = 0

# Creating the Questions;

question1 = input("Is Python skills required for Advanced Data Analysis?: ")
if question1 == "yes":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')
print('-'*30)

question2 = input("A List in Python cannot be altered. True or False?: ")
if question2 == "False":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')
print('-'*30)

question3 = input("A TEXT data type is classified as a String. True or False?: ")
if question3 == "True":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')
print('-'*30)

question4 = input("A List, Tuple,and Range are all Sequence types. True or False?: ")
if question4 == "True":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')
print('-'*30)

question5 = input("15 x 4 / 8 + 3 = ")
if question5 == "10.5":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')
print('-'*30)

# Display the final score
print("You got " + str(score) + " out of " + str(5) + " questions Correct!" )
print("You got " + str((score/5) * 100) + "%. ")