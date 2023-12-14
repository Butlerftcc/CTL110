# CTI-110
# P2HW2 - List
# Alexander Butler
# 9/19/23
#
#ask user for first grade
#ask user for second grade
#ask user for third grade
#ask user for fourth grade
#ask user for fifth grade
#ask user for sixth grade
#add grades to a list
#find the minimum value in that list
#find the maximum value in that list
#find the sum of all the values in that list
#find the average of that list
#display the lowest grade
#display the highest grade
#display the sum of the grades
#display the average grade

Module1 = float(input('Enter grade for Module 1:'))
Module2 = float(input('Enter grade for Module 2:'))
Module3 = float(input('Enter grade for Module 3:'))
Module4 = float(input('Enter grade for Module 4:'))
Module5 = float(input('Enter grade for Module 5:'))
Module6 = float(input('Enter grade for Module 6:'))
Grades = [Module1, Module2, Module3, Module4, Module5, Module6]

LowestScore = min(Grades)
HighestScore = max(Grades)
SumOfScore = sum(Grades)
GradeAverage = sum(Grades)/len(Grades)

print('------------Results------------')
print('Lowest Grade:', '     ', LowestScore)
print('Highest Grade:', '    ', HighestScore)
print('Sum of Grades:', '    ', SumOfScore)
print('Average:', '          ', f'{GradeAverage:.2f}')
print('-------------------------------')
