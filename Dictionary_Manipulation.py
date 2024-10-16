# Dictionary Manipulation
#Objective: Work with dictionaries.
#Instructions: Create a program that maintains a student grade book.
# Allow users to add, remove, and update student grades, and print all student names with their corresponding grades.

student_grades = {
    "Hosanna": 65.2,
    "Busayo": 60.7,
    "Iyke": 94.0,
    "Oluwaseyi": 61.5,
    "Stella": 70.6,
    "Theodore": 60.9
}

# Print All students grades
print(student_grades)
print('-'*30)

# Add a student grade
student_grades['Sahar'] = 98
print(student_grades)
print('-'*30)

# Removing items in the dictionary using Pop method
student_grades.pop('Sahar')
print(student_grades)
print('-'*30)

# Updating student grade
student_grades['Iyke'] = 50
print(student_grades)
print('-'*30)
