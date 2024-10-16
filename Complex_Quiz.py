from numpy.f2py.auxfuncs import options

print("WELCOME TO IYKE's QUIZ GAME!")

def my_Quiz(quiz):
    score = 0 # Initial user score.
    for question in quiz: # Loop through each question
        print(f"\n {question['question']}")

        # Display the options
        for option in question['options']:
            print(option)

        # Get the user's answer
        answer = input("Your Answer (A/B/C): ").strip().upper()

        if answer == question['answer']:
            print('CORRECT!\n')
            score += 1
        else:
            print(f"WRONG! The correct answer is {question['answer']}.\n")

    # Display the final score
    print(f"QUIZ Completed! You scored {score} out of {len(quiz)}.")
    print("You got " + str((score / 5) * 100) + "%. ")

if __name__ == "__main__":
   # Defining the quiz questions;
   questions = [
       {
           "question": "Is Python skills required for Advanced Data Analysis?",
           "options": [" A) YES", " B) NO", " C) N/A"],
           "answer": "A"
       },
       {
           "question": "A List in Python cannot be altered",
           "options": [" A) TRUE", " B) FALSE", " C) N/A"],
           "answer": "B"
       },
       {
           "question": "A TEXT data type is classified as a String",
           "options": [" A) TRUE", " B) FALSE", " C) N/A"],
           "answer": "A"
       },
       {
           "question": "A List, Tuple, and Range are all Sequence types",
           "options": [" A) TRUE", " B) FALSE", " C) N/A"],
           "answer": "A"
       },
       {
           "question": "What is the answer to the equation 15 x 4 / 8 + 3",
           "options": [" A) 8.20", " B) 27", " C) 10.5"],
           "answer": "C"
       }
   ]

   # Run the quiz
   my_Quiz(questions)