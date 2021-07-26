from math import floor
from random import sample

def encrypt(character, key):
    reverse_morse = ""

    index = key.index(character)

    j = index
    while j > 0:
        if j % 2 == 0:
            reverse_morse += '-'
        else:
            reverse_morse += '.'
        j = floor((j - 1) / 2)

    encrypted_str = reverse_morse[::-1] + ' '
    return encrypted_str

def decrypt(string, key):
    j = 0
    for character in string:
        if character == '-':
            j = 2*j + 2
        else:  # character == '.'
            j = 2*j + 1

    decrypted_letter = key[j]
    return decrypted_letter


if __name__ == "__main__":
    init_char_tree = " ETIANMSURWDKGOHVF L PJBXCYZQ  54 3   2  +    16-/     7   8 90"

    print("Session started...")
    live_session = True

    key = ''.join(sample(init_char_tree, len(init_char_tree)))

    while live_session:
        type = input("Would you like to (e)ncrypt, (d)ecrypt, or e(x)it: ")

        if type.lower()[0] == 'e':
            text = input("Enter text to be encrypted: ")

            morse_translation = ""
            for character in text.upper():
                if character == ' ':
                    morse_translation += ' '
                else:
                    morse_translation += encrypt(character, key)

            print(morse_translation)
        elif type.lower()[0] == 'd':
            encrypted_text = input("Enter text to be decrypted: ")

            decrypted_text = ""
            for word in encrypted_text.split("  "):
                for letter in word.split(" "):
                    decrypted_text += decrypt(letter, key)
                decrypted_text += " "

            print(decrypted_text)
        else:
            live_session = False

