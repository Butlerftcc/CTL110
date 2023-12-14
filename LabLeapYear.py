is_leap_year = False
   
input_year = int(input())

def IsLeapYear():
    is_leap_year = True
    print(input_year, '- leap year')
def IsNotLeapYear():
    is_leap_year = False
    print(input_year, '- not a leap year')

if ((input_year % 400) == 0):
    IsLeapYear()
elif((input_year % 100) != 0 and (input_year % 4) == 0):
    IsLeapYear()
else:
    IsNotLeapYear()
