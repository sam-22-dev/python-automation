# 06 - Tasks ---> Task 2
# Build a countdown calculator
# --------------------------------------------------------------

import datetime

def read_date():
    while True:
        try:
            Year = int(input('Enter the year : ')) 
            Month = int(input('Enter the month : '))
            Day = int(input('Enter the day : '))
            Date_ = datetime.date(Year,Month,Day)
            
            return Date_

        except ValueError:
            print('INVALID DATE!! Please enter a valid date.\n')




print('\n\nFirst Date \n --------------------------')
first_date = read_date()
print('\n\nSecond Date \n --------------------------')
second_date = read_date()

diff = first_date - second_date
print(f'\nThe difference is {abs(diff.days)} days')