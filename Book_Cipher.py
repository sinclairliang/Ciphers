import re

text = "Apple Banana Cherry Dog Elephant Ferry Goose Gray "


def cleaning_text(book_aadress):
    original_text = open(book_aadress).read()
    new_text = re.sub('[^a-zA-Z0-9]', r' ', original_text)
    re.sub(' +', ' ', new_text).strip()
    return new_text


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


def encode(message, numbers):
    output_list = list()
    for i in range(0, len(message)):
        current_letter = message[i].upper()
        if current_letter in numbers:
            output_list.append(numbers[current_letter].pop(0))
    return output_list


def decode(message, numbers):
    output_list = list()
    for i in range(0, len(message)):
        current_number = message[i]
        for letter, number_list in numbers.items():
            if current_number in number_list:
                output_list.append(letter)
    return output_list


def main():
    new_text = cleaning_text('test.txt')
    words = get_words(new_text)
    numbers = get_numbers(words)
    # print(numbers)
    message = "SillyIdiot"
    cipher = [5, 6, 62, 117, 798, 15, 60, 32, 16, 3]
    # l = encode(message, numbers)
    d = decode(cipher, numbers)
    # print(l)
    print(d)
    # print(numbers)


main()
