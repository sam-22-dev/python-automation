# Task 4
# Currency converter
# ------------------------------------------------------------------




def to_EUR(amount):
    print(f'\n{amount} USD = {amount * 0.92} EUR')

def to_GBP(amount):
    print(f'\n{amount} USD = {amount * 0.78} GBP')

def to_JPY(amount):
    print(f'\n{amount} USD = {amount * 156} JPY')

def to_AUD(amount):
    print(f'\n{amount} USD = {amount * 1.52} AUD')




def main():
    while True:
        print(''' Convert From Doller To :
    \t1: EUR
    \t2: GBP
    \t3: JPY
    \t4: AUD
    \t5: CANCEL''')

        choise = int(input('Your Choise: '))
        if choise == 5:
            print('Canceled....')
            break

        amount = int(input('Enter the amount by Doller: '))

        
        if choise == 1:
            to_EUR(amount)
        elif choise == 2:
            to_GBP(amount)
        elif choise == 3:
            to_JPY(amount)
        elif choise == 4:
            to_AUD(amount)

        PlayAgain = input('\nDo you want to do another operation? y/n : ')
        print('---------------------------------------------')

        if PlayAgain == 'n':
            break
    print('****************************************************')






if __name__ == '__main__':
    main()

