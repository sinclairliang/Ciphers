import re

text = "Apple Banana Cherry Dog Elephant Ferry Goose Gray "


def get_book_text(book_aadress):
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


def encode(text, numbers):
    output_list = list()
    for i in range(0, len(text) - 1):
        current_letter = text[i].upper()
        if current_letter in numbers:
            output_list.append(numbers[current_letter].pop(0))
    return output_list


def main():
    new_text = get_book_text('test.txt')
    words = get_words(new_text)
    numbers = get_numbers(words)
    message = "Hello"
    l = encode(message, numbers)
    print(l)



main()
