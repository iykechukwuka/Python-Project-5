#QUESTION 3: List Basics
#Objective: Understand and manipulate lists.
#Instructions: Create a list of ten numbers, then compute and print the sum, average, minimum, and maximum values.
from numpy.ma.extras import average

myList = [4, 19, 45, 27, 93, 60, 83, 100, 41, 33]

#Computing sum;
sum_myList = sum(myList)

#Computing Average;
avg_myList = average(myList)

#Computing Minimum;
min_myList = min(myList)

#Computing Maximum;
max_myList = max(myList)

#print( sum_myList,',' ,avg_myList,',',min_myList,',', max_myList)
print(f"sum = {sum_myList}\nAverage = {avg_myList}\nMinimum = {min_myList}\nMaximum = {max_myList}")
