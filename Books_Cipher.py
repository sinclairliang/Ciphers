# Sinclair Liang
import time
import copy
import re
import sys
import pyprind
import os

def banner():
    banner = '''
    
             oooooooooo.                      oooo                 
             `888'   `Y8b                     `888                 
              888     888  .ooooo.   .ooooo.   888  oooo   .oooo.o 
              888oooo888' d88' `88b d88' `88b  888 .8P'   d88(  "8 
              888    `88b 888   888 888   888  888888.    `"Y88b.  
              888    .88P 888   888 888   888  888 `88b.  o.  )88b 
             o888bood8P'  `Y8bod8P' `Y8bod8P' o888o o888o 8""888P' 
                                                                   
                                                                   
                                                                   
           .oooooo.    o8o             oooo                           
          d8P'  `Y8b   `"'             `888                           
         888          oooo  oo.ooooo.   888 .oo.    .ooooo.  oooo d8b 
         888          `888   888' `88b  888P"Y88b  d88' `88b `888""8P 
         888           888   888   888  888   888  888ooo888  888     
         `88b    ooo   888   888   888  888   888  888    .o  888     
          `Y8bood8P'  o888o  888bod8P' o888o o888o `Y8bod8P' d888b    
                             888                                      
                            o888o                                     
                                                                      
    '''
    return banner


def cleaning_text(book_address):
    """
    :param book_address: the address of the book used as the key
    :return: words without any special characters
    """
    original_text = open(book_address).read()
    new_text = re.sub('[^a-zA-Z0-9]', r' ', original_text)
    re.sub(' +', ' ', new_text).strip()
    return new_text


def cleaning_cipher(cipher_file_address):
    """
    :param cipher_file_address: the address of the encrypted file
    :return: a list of integers
    """
    cipher_text = open(cipher_file_address).read()
    cipher_text_list = cipher_text[1:-1].split(",")
    for i in range(0, len(cipher_text_list)):
        cipher_text_list[i] = int(cipher_text_list[i])
    return cipher_text_list


def get_words(text):
    """
    :param text: words without any special characters
    :return: a list of words
    """
    list_of_words = list()
    words = re.split(r'\s+', text)
    for word in words:
        list_of_words.append(word.upper())
    return list_of_words


def get_numbers(words):
    """
    :param words: a list of words
    :return: a list containing numbers indicating the position of words
    """
    numbers = dict()
    for i in range(0, len(words) - 1):
        if len(words[i]) > 0:

            current_letter = words[i][0]
            sys.stdout.write('\r')
            sys.stdout.write("Now encrypting word: " + current_letter)
            sys.stdout.flush()
            if current_letter in numbers:
                numbers[current_letter].append(i + 1)
            else:
                numbers[current_letter] = list()
                numbers[current_letter].append(i + 1)
    return numbers


def encode(plaintext, numbers):
    """
    :param plaintext: plaintext
    :param numbers: a list containing numbers indicating the position of words
    :return: A list of numbers after encryption
    """
    length = len(plaintext)
    bar = pyprind.ProgBar(length, width=40)

    numbers_to_use = copy.deepcopy(numbers)
    output_list = list()
    for i in range(0, length):
        current_letter = plaintext[i].upper()
        if current_letter in numbers_to_use:
            output_list.append(numbers_to_use[current_letter].pop(0))
        bar.update()
    return output_list


def decode(ciphertext, numbers):
    """

    :param ciphertext: ciphertext
    :param numbers: a list containing numbers indicating the position of words
    :return: plaintext without space nor special characters
    """
    length = len(ciphertext)
    bar = pyprind.ProgBar(length, width=40)

    numbers_to_use = copy.deepcopy(numbers)
    output_list = list()
    for i in range(0, length):
        current_number = int(ciphertext[i])
        for letter, number_list in numbers_to_use.items():
            if current_number in number_list:
                output_list.append(letter)
        bar.update()
    return ''.join(output_list)


def main():
    ENCODE = False
    DECODE = False
    while ENCODE is False and DECODE is False:
        mode = input("Would you like to (E)ncode ot (D)ecode a file?\n")
        if mode == 'E':
            ENCODE = True
            DECODE = False

        if mode == 'D':
            ENCODE = False
            DECODE = True

    if ENCODE:
        plaintext_file_address = input("Please enter the address of the file you would like to encrypt\n")
        key_file = input("Please enter the address of the key file you would like to use\n")
        start_time = time.time()
        file = open("encrypted_file", "w")
        plaintext = cleaning_text(plaintext_file_address)
        words = get_words(cleaning_text(key_file))
        numbers = get_numbers(words)
        l = encode(plaintext, numbers)
        file.write(str(l))
        file.close()
        end_time = time.time()
        print("Your encrypted file has been generated! " + "%s %d m %.2f s " % (
            "Finish encrypting! Time elapsed:", int((end_time - start_time) / 60), (end_time - start_time) % 60))
        os.system("open encrypted_file")

    if DECODE:
        cipher_file_address = input("Please enter the address of the file you would like to decrypt\n")
        key_file = input("Please enter the address of the key file you would like to use\n")
        start_time = time.time()
        file = open("decrypted_file", "w")
        cipher_list = cleaning_cipher(cipher_file_address)
        words = get_words(cleaning_text(key_file))
        numbers = get_numbers(words)
        d = decode(cipher_list, numbers)
        file.write(d)
        file.close()
        end_time = time.time()
        print("Your decrypted file has been generated! " + "%s %d m %.2f s " % (
            "Finish decrypting! Time elapsed:", int((end_time - start_time) / 60), (end_time - start_time) % 60))
        os.system("open decrypted_file")

if __name__ == '__main__':
    sys.stdout.write(banner())
    main()
