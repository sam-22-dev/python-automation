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

days_since_birth = datetime.datetime.date(datetime.datetime.now()) - read_date()
print(f'The days since birthday ---> {days_since_birth}')


