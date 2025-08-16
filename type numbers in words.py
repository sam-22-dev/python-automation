# Task 1 
# Type Numbers In Words
# ------------------------------------------------------------------------



import inflect

def type_numbers_in_words(Number):
    p = inflect.engine()
    print(p.number_to_words(Number))



Num = int(input('Enter a number: '))

type_numbers_in_words(Num)