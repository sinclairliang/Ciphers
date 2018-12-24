import copy
import re
import sys


def cleaning_text(book_aadress):
    original_text = open(book_aadress).read()
    new_text = re.sub('[^a-zA-Z0-9]', r' ', original_text)
    re.sub(' +', ' ', new_text).strip()
    return new_text


def cleaning_cipher(cipher_file_address):
	cipher_text = open(cipher_file_address).read()
	cipher_text_list = cipher_text[1:-1].split(",")
	for i in range(0,len(cipher_text_list)):
		cipher_text_list[i] = int(cipher_text_list[i])
	return cipher_text_list



def get_words(text):
    list_of_words = list()
    words = re.split(r'\s+', text)
    # return list_of_words
    for word in words:
        list_of_words.append(word.upper())
    return list_of_words


def get_numbers(words):
    numbers = dict()
    for i in range(0, len(words) - 1):
        if len(words[i]) > 0:
            current_letter = words[i][0]
            if current_letter in numbers:
                numbers[current_letter].append(i + 1)
            else:
                numbers[current_letter] = list()
                numbers[current_letter].append(i + 1)
    return numbers


def encode(plaintext, numbers):
    numbers_to_use = copy.deepcopy(numbers)
    output_list = list()
    for i in range(0, len(plaintext)):
        current_letter = plaintext[i].upper()
        if current_letter in numbers_to_use:
            output_list.append(numbers_to_use[current_letter].pop(0))
    return output_list


def decode(ciphertext, numbers):
    numbers_to_use = copy.deepcopy(numbers)
    output_list = list()
    for i in range(0, len(ciphertext)):
        current_number = int(ciphertext[i])
        for letter, number_list in numbers_to_use.items():
            if current_number in number_list:
                output_list.append(letter)
    return ''.join(output_list)


def main():
    ENCODE = False
    DECODE = False
    while ENCODE is False and DECODE is False:
        mode = input("Would you like to (E)ncode ot (D)ecode a file?")
        if mode == 'E':
            ENCODE = True
            DECODE = False

        if mode == 'D':
            ENCODE = False
            DECODE = True

    if ENCODE:
        plaintext_file_address = input("Please enter the address of the file you would like to encrypt\n")
        key_file = input("Please enter the address of the key file you would like to use\n")
        file = open("encrypted_file", "w")
        plaintext = cleaning_text(plaintext_file_address)
        words = get_words(cleaning_text(key_file))
        numbers = get_numbers(words)
        l = encode(plaintext, numbers)
        file.write(str(l))
        file.close()
        print("Your encrypted file has been generated! ")

    if DECODE:
        cipher_file_address = input("Please enter the address of the file you would like to decrypt\n")
        key_file = input("Please enter the address of the key file you would like to use\n")
        file = open("decrypted_file", "w")
        cipher_list = cleaning_cipher(cipher_file_address)
        words = get_words(cleaning_text(key_file))
        numbers = get_numbers(words)
        d = decode(cipher_list, numbers)
        file.write(d)
        file.close()
        print("Your decrypted file has been generated! ")


main()
