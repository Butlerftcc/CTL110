# CTI-110
# P2HW2 - List
# Alexander Butler
# 9/19/23
#
#ask user how many grades to enter
#ask user for a grade until the desired amount of times has been reached
#add grades to a list
#find the minimum value in that list
#create a modified list with out the lowest value
#find the average of the modified list
#find the grade letter for the average
#display the lowest grade
#display the modified list
#display the average of the modified list
#display the letter grade

Iterations = int(input('How many scores do you want to enter? '))
Grades = []

for i in range(Iterations):
    Score = float(input(f'Enter score #{i+1}: '))

    while Score < 0 or Score > 100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        Score = float(input(f'Enter score #{i+1} again: '))
        
    Grades.append(Score)

LowestScore = min(Grades)
Grades.remove(min(Grades))
GradeAverage = sum(Grades)/len(Grades)

grade = 'null'
if GradeAverage >= 90:
    grade = 'A'
elif GradeAverage >= 80:
    grade = 'B'
elif GradeAverage >= 70:
    grade = 'C'
elif GradeAverage >= 60:
    grade = 'D'
else:
    grade = 'F'

print('------------Results------------')
print('Lowest Grade  : ', LowestScore)
print('Modified List : ', Grades)
print('Scores Average: ', f'{GradeAverage:.2f}')
print('Grade         : ', grade)
print('-------------------------------')
