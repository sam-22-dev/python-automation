# 06 - Tasks ---> Task 1
# Create a code generator
# ---------------------------------------------------

def encoding(text):
    encoded = ''
    for letter in text:
        if letter.isalpha():
            if letter == 'z':
                letter = 'a'
            elif letter == 'Z':
                letter = 'A'
            else:
                encoded += chr(ord(letter)+1)
        else:
            encoded += letter

    return encoded


def decoding(decoded_text):
    decoded = ''
    for letter in decoded_text:
        if letter.isalpha():
            if letter == 'a':
                letter = 'z'
            elif letter == 'A':
                letter = 'Z'
            else:
                decoded += chr(ord(letter)-1)
        else:
            decoded += letter

    return decoded


message = input('Enter a message : ')
print('-------------------------------------------')
print('Encoded text ',encoding(message))
print('Decoded text ',decoding(encoding(message)))