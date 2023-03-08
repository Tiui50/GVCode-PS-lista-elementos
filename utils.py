import string
import sort

def get_chars(word):
    return [*word]

def chars_to_number(chars):
    value = []

    for char in chars:
        value.append(ord(char))
    return  value

def number_to_chars(numbers):
    value = []

    for number in numbers:
        value.append(chr(number))
    return  value

def get_words(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation)).split()

def sort_characters(characters, dedupe=False):
    if dedupe:
        expression = list(dict.fromkeys(characters))

    # Converter os caracteres em números
    expression = chars_to_number(characters)
    # Fazer o sort
    sort.merge_sort(expression)
    # Converter de volta para caracteres
    expression = number_to_chars(expression)
    return expression

def sort_words(sentence, dedupe=False):
    value = get_words(sentence)
    if dedupe:
        value = list(dict.fromkeys(value))

    sort.merge_sort_words(value)
    return value

# def sort_sentence(sentence):

         