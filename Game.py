# Game 
# --------------------------------------------------


# 1st Solution  (oob)
# --------------------



import time

class Game:
    def __init__(self):
        while True:
            print('WELCOME... Pick a game to play....')
            time.sleep(0.5)
            print('\t1: Sentence Remove Duplicates')
            time.sleep(0.5)
            print('\t2: Multiplication Table')
            time.sleep(0.5)
            print('\t3: Divided By Numbers')
            time.sleep(0.5)
            print('\t4: EXIT...')
            time.sleep(0.5)

            choice = int(input('Enter your choice : '))

            if choice == 4:
                print('\t\t...GOODBYE...')
                break
            
            elif choice == 1:
                self.sentence_remove_duplicates()
            elif choice == 2:
                self.multiplication_table()
            elif choice == 3:
                self.divided_by_numbers()
            

            PlayAgain = input('''\nPress y to play again
or n to exit... ''')
            
            if PlayAgain == 'n':
                break

        print('******************************')
            




    def sentence_remove_duplicates(self):
        original_sentence = input('Enter a sentence : ')
        sentence_elem = original_sentence.split(' ')
        new_sentence_elem = []

        for word in sentence_elem:
            if word not in new_sentence_elem:
                new_sentence_elem.append(word)

        new_sentence = ' '.join(new_sentence_elem)
        print(new_sentence)

        


    def multiplication_table(self):
        
        start = int(input('Start : '))
        end = int(input('End : '))

        for i in range(start,end + 1):
            print(f'\nNUMBER   {i}\n')
            for j in range(1,13):
                print(f'{i} X {j} = {i*j}')
            
            print('--------------------------')

            


    def divided_by_numbers(self):
        First_Num = int(input('Enter the first number : '))
        Second_Num = int(input('Enter the second number : '))

        Numbers = [x for x in range(1,101) if x % First_Num == 0 and x % Second_Num == 0]
        print(Numbers)



G1 = Game()




# ------------------------------------------------------------------------------------


# 2nd Solution  (functions)
# ---------------------------



import time


def sentence_remove_duplicates():
    original_sentence = input('Enter a sentence : ')
    sentence_elem = original_sentence.split(' ')
    new_sentence_elem = []

    for word in sentence_elem:
        if word not in new_sentence_elem:
            new_sentence_elem.append(word)

    new_sentence = ' '.join(new_sentence_elem)
    print(new_sentence)


def multiplication_table():
    
    start = int(input('Start : '))
    end = int(input('End : '))

    for i in range(start,end + 1):
        print(f'\nNUMBER   {i}\n')
        for j in range(1,13):
            print(f'{i} X {j} = {i*j}')
            
        print('--------------------------')

        


def divided_by_numbers():
    First_Num = int(input('Enter the first number : '))
    Second_Num = int(input('Enter the second number : '))

    Numbers = [x for x in range(1,101) if x % First_Num == 0 and x % Second_Num == 0]
    print(Numbers)




def main():
    while True:
        print('WELCOME... Pick a game to play....')
        time.sleep(0.5)
        print('\t1: Sentence Remove Duplicates')
        time.sleep(0.5)
        print('\t2: Multiplication Table')
        time.sleep(0.5)
        print('\t3: Divided By Numbers')
        time.sleep(0.5)
        print('\t4: EXIT...')
        time.sleep(0.5)

        choice = int(input('Enter your choice : '))

        if choice == 4:
            print('\t\t...GOODBYE...')
            break
        
        elif choice == 1:
            sentence_remove_duplicates()
        elif choice == 2:
            multiplication_table()
        elif choice == 3:
            divided_by_numbers()
        

        PlayAgain = input('''\nPress y to play again
or n to exit... ''')
        
        if PlayAgain == 'n':
            break

    print('******************************')



if __name__ == "__main__":
    main()



