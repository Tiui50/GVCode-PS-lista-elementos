import string
import sort as s

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

def get_words(sentence, numbers):

    sentence = str(sentence)
    if numbers:
        try:
            return sentence.translate(str.maketrans('', '', string.punctuation)).split()
        except:
            return sentence
    else:
        try:
            return sentence.translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits)).split()
        except:
            return sentence

def sort(sentence, dedupe=False,  numbers=True):
    value = get_words(sentence, numbers)
    if dedupe:
        value = list(dict.fromkeys(value))
        
    print("It took " + str(s.merge_sort(value)) + "s to complete the operation.")

    return value

# def sort_sentence(sentence):

         