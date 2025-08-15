# 06 - Tasks ---> Task 3
# Make a temperature/measurement converter
# -------------------------------------------------------------


class Converting:
    def __init__(self):
        while True:
            print('''\n\nMeasurements Converters
\t1: Fahrenheit  ---> Celsius
\t2: Celsius     ---> Fahrenheit
\t3: Centimeters ---> Inches
\t4: Inches      ---> Centimeters
\t5: Kilograms   ---> Pounds
\t6: Pounds      ---> Kilograms
\t7:EXIT...''')
            
            choice = int(input('\nChoose your conversion: '))
            print('-------------------------------------')

            if choice == 7:
                print('\nGOODBYE....')
                break
            elif choice == 1:
                self.F_to_C()
            elif choice == 2:
                self.C_to_F()
            elif choice == 3:
                self.cm_to_in()
            elif choice == 4:
                self.in_to_cm()
            elif choice == 5:
                self.kg_to_pound()
            elif choice == 6:
                self.pound_to_kg()
            
            
            convert_more = input('\nDo you want to convert more time? y/n: ')
            if convert_more == 'n':
                break

        print('\n*******************************************')



    def F_to_C(self):
        fahrenheit = int(input('Enter the temperature by fahrenheit: '))
        celsius = (fahrenheit - 32) / 1.8
        print(f'The temperature by celsius = {celsius}')
    
    def C_to_F(self):
        celsius = int(input('Enter the temperature by celsius: '))
        fahrenheit = (celsius * 1.8) + 32
        print(f'The temperature by fahrenheit = {fahrenheit}')


    def cm_to_in(self):
        centimeters = int(input('Enter the length by centimeters: '))
        inches = centimeters / 2.54
        print(f'The length in inches = {inches}')

    def in_to_cm(self):
        inches = int(input('Enter the length in inches: '))
        centimeters = inches * 2.54
        print(f'The length in centimeters = {centimeters}')

    def kg_to_pound(self):
        kg = int(input('Enter the mass by kilograms: '))
        pound = kg / 0.45359237
        print(f'The mass by pounds = {pound}')

    def pound_to_kg(self):
        pound = int(input('Enter the mass by pounds: '))
        kg = pound * 0.45359237
        print(f'The mass by kilograms = {kg}')


C1 = Converting()

